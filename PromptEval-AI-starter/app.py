import streamlit as st
import pandas as pd
import plotly.express as px
from evaluation.evaluator import evaluate_dataset

st.set_page_config(page_title="PromptEval AI", page_icon="🧪", layout="wide")
st.title("🧪 PromptEval AI")
st.caption("Compare two assistant prompt versions using a transparent, repeatable evaluation.")

with st.sidebar:
    st.header("Evaluation settings")
    st.write("Scoring uses explainable text-based proxies. It does **not** prove factual correctness.")
    uploaded = st.file_uploader("Upload questions CSV", type=["csv"])
    st.divider()
    st.markdown("**Required columns**")
    st.code("id, topic, question, answer_current, answer_new")

source = uploaded if uploaded else "data/questions.csv"
try:
    df = pd.read_csv(source)
except Exception as e:
    st.error(f"Could not read the CSV: {e}")
    st.stop()

required = ["question", "answer_current", "answer_new"]
missing = [c for c in required if c not in df.columns]
if missing:
    st.error("Missing required columns: " + ", ".join(missing))
    st.stop()
if "id" not in df: df["id"] = [f"Q-{i+1:03}" for i in range(len(df))]
if "topic" not in df: df["topic"] = "Uncategorized"

results = evaluate_dataset(df)
summary = results.attrs["summary"]
current, new = summary["current_mean"], summary["new_mean"]
delta = new-current

c1,c2,c3,c4 = st.columns(4)
c1.metric("Questions evaluated", f"{len(results):,}")
c2.metric("Current proxy score", f"{current:.1f}/100")
c3.metric("New proxy score", f"{new:.1f}/100", f"{delta:+.1f} points")
c4.metric("New version wins", f"{summary['new_wins']} / {len(results)}")

st.info("Scores are automated quality proxies for relevance, completeness, clarity and tone. Accuracy is not inferred from wording: answers require checking against approved company policy / knowledge-base content.")

tab1,tab2,tab3 = st.tabs(["Overview", "Question-level results", "Method & limitations"])
with tab1:
    left,right = st.columns(2)
    with left:
        chart = pd.DataFrame({"Version":["Current","New"],"Score":[current,new]})
        st.plotly_chart(px.bar(chart,x="Version",y="Score",range_y=[0,100],title="Average automated proxy score"),use_container_width=True)
    with right:
        topic = results.groupby("topic",as_index=False)[["current_score","new_score"]].mean()
        topic_long = topic.melt(id_vars="topic",var_name="Version",value_name="Score")
        topic_long["Version"] = topic_long["Version"].map({"current_score":"Current","new_score":"New"})
        st.plotly_chart(px.bar(topic_long,x="topic",y="Score",color="Version",barmode="group",title="Score by topic"),use_container_width=True)
    st.subheader("Decision support")
    if delta >= 2 and summary["new_regressions"] == 0:
        recommendation = "SHIP"
        explanation = "The new version improved the proxy score by at least 2 points and no question-level proxy regression was detected. Complete factual/policy review before release."
    elif delta < -2 or summary["new_regressions"] > len(results)*0.25:
        recommendation = "DO NOT SHIP"
        explanation = "The new version shows a meaningful score decline or regressions on more than 25% of questions."
    else:
        recommendation = "SHIP WITH CONDITIONS"
        explanation = "The evidence is mixed or the improvement is not strong enough. Review flagged questions and validate factual accuracy against approved policies."
    st.subheader(recommendation)
    st.write(explanation)
    st.caption("This is a decision-support rule, not an automatic guarantee of safety or correctness.")
    st.write(f"New version proxy wins: **{summary['new_wins']}** · Losses: **{summary['new_losses']}** · Ties: **{summary['ties']}** · Regressions: **{summary['new_regressions']}**")
with tab2:
    topics = ["All"] + sorted(results["topic"].dropna().astype(str).unique().tolist())
    selected = st.selectbox("Filter by topic", topics)
    view = results if selected=="All" else results[results.topic.astype(str)==selected]
    st.dataframe(view, use_container_width=True, hide_index=True)
    st.download_button("Download evaluation CSV", results.to_csv(index=False).encode("utf-8"), "evaluation_results.csv", "text/csv")
with tab3:
    st.markdown("""
**Scored dimensions (0–100 proxies):**
- Relevance (25%): overlap between meaningful question terms and answer terms.
- Completeness (25%): whether the answer contains enough detail and actionable guidance.
- Clarity (15%): sentence length and readability signals.
- Professional tone (10%): polite/supportive language signals.
- Accuracy (25%): **not automatically scored** because no verified reference answers or policy documents were supplied. It requires human / knowledge-base validation.

The displayed proxy score is normalized across the four automatically measurable dimensions. It is not a factual accuracy score.

**Before production:** add approved reference answers / policy documents, use a blinded LLM-as-judge with a fixed rubric, manually audit a sample, track evaluator agreement, and block release on critical policy violations.
""")
st.caption("Dataset: " + ("uploaded CSV" if uploaded else "data/questions.csv"))

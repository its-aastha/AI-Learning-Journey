import re
import pandas as pd

STOPWORDS = set("""
a an the is are was were be been being to of in on for from with and or but if then
it this that these those my your our their i you we they he she do does did can could
would should how what when where why who which me please tell show get have has had
""".split())
POLITE = {"please","thank","thanks","sorry","happy","help","welcome","appreciate","reach"}
ACTION = {"open","select","choose","click","visit","start","contact","check","go","submit","send","return","cancel","follow","use","find"}
SUPPORTIVE = {"please","thank","thanks","sorry","happy","help","welcome","appreciate"}

def tokens(text):
    words = re.findall(r"[a-zA-Z0-9']+", str(text).lower())
    return [w for w in words if w not in STOPWORDS and len(w)>2]

def relevance(question, answer):
    q=set(tokens(question)); a=set(tokens(answer))
    if not q: return 50.0
    overlap=len(q & a)/len(q)
    return min(100.0, overlap*150)

def completeness(question, answer):
    words=tokens(answer)
    if not words: return 0.0
    # Proxy: sufficient detail plus a concrete next-step signal, not factual verification.
    length_score=min(len(words)/35,1)*70
    action_score=30 if any(w in ACTION for w in words) else 10
    return min(100.0,length_score+action_score)

def clarity(answer):
    text=str(answer).strip()
    words=tokens(text)
    if not words: return 0.0
    sentences=[s for s in re.split(r"[.!?]+",text) if s.strip()]
    avg=len(words)/max(1,len(sentences))
    sentence_score=100 if 8 <= avg <= 22 else max(35,100-abs(avg-15)*3)
    return float(min(100,sentence_score))

def tone(answer):
    words=set(re.findall(r"[a-zA-Z']+",str(answer).lower()))
    hits=len(words & SUPPORTIVE)
    # A neutral answer is not automatically bad; reward a small amount of courteous language.
    return float(min(100,75+hits*8))

def score_answer(question, answer):
    r=relevance(question,answer)
    c=completeness(question,answer)
    cl=clarity(answer)
    t=tone(answer)
    # Normalize the four proxy dimensions to 100; factual accuracy remains a separate human check.
    score=0.25*r+0.25*c+0.15*cl+0.10*t
    return {"relevance_proxy":round(r,1),"completeness_proxy":round(c,1),
            "clarity_proxy":round(cl,1),"tone_proxy":round(t,1),
            "automated_proxy_score":round(score/0.75,1)}

def evaluate_dataset(df):
    rows=[]
    for _,row in df.iterrows():
        q=row["question"]
        old=score_answer(q,row["answer_current"])
        new=score_answer(q,row["answer_new"])
        rows.append({
            "id":row.get("id",""),"topic":row.get("topic","Uncategorized"),"question":q,
            "current_score":old["automated_proxy_score"],"new_score":new["automated_proxy_score"],
            "score_delta":round(new["automated_proxy_score"]-old["automated_proxy_score"],1),
            "current_relevance":old["relevance_proxy"],"new_relevance":new["relevance_proxy"],
            "current_completeness":old["completeness_proxy"],"new_completeness":new["completeness_proxy"],
            "current_clarity":old["clarity_proxy"],"new_clarity":new["clarity_proxy"],
            "current_tone":old["tone_proxy"],"new_tone":new["tone_proxy"],
            "accuracy_review":"Required"
        })
    out=pd.DataFrame(rows)
    wins=int((out.score_delta>0).sum()); losses=int((out.score_delta<0).sum()); ties=int((out.score_delta==0).sum())
    summary={"current_mean":round(out.current_score.mean(),1),"new_mean":round(out.new_score.mean(),1),
             "new_wins":wins,"new_losses":losses,"ties":ties,"new_regressions":losses}
    out.attrs["summary"]=summary
    return out

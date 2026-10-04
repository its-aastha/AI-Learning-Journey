from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier

DATA_FILE = Path(__file__).with_name("messages.csv")


def main():
    data = pd.read_csv(DATA_FILE)
    data["label"] = data["label"].str.strip().str.lower()
    if not {"message", "label"}.issubset(data.columns):
        raise ValueError("CSV must contain 'message' and 'label' columns")

    X_train, X_test, y_train, y_test = train_test_split(
        data["message"], data["label"], test_size=0.25,
        random_state=42, stratify=data["label"]
    )

    models = {
        "Logistic regression": LogisticRegression(max_iter=1000),
        "Decision tree": DecisionTreeClassifier(max_depth=20, random_state=42),
        "Random forest": RandomForestClassifier(n_estimators=200, random_state=42),
        "Support vector machine": LinearSVC(),
    }

    results = []
    for name, classifier in models.items():
        model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2)), classifier)
        model.fit(X_train, y_train)
        predicted = model.predict(X_test)
        results.append((name, f1_score(y_test, predicted, pos_label="spam")))
        print(f"\n=== {name} ===")
        print(f"Accuracy: {accuracy_score(y_test, predicted):.3f}")
        print(classification_report(y_test, predicted, zero_division=0))

    print("\nSpam F1 comparison (higher is better):")
    for name, score in sorted(results, key=lambda row: row[1], reverse=True):
        print(f"{name:24} {score:.3f}")

    print("\nTry your own message (Ctrl+C to stop).")
    # Fit the best model on all available examples for the interactive demo.
    best_name = max(results, key=lambda row: row[1])[0]
    best_classifier = models[best_name]
    final_model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2)), best_classifier)
    final_model.fit(data["message"], data["label"])
    while True:
        message = input("Message: ")
        print("Prediction:", final_model.predict([message])[0])


if __name__ == "__main__":
    main()

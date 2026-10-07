import os
import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# ============================================================
# 1. LOAD DATA
# ============================================================

print("\nLoading TF-IDF features...")

X_train = joblib.load("models/X_train.pkl")
X_test = joblib.load("models/X_test.pkl")

y_train = joblib.load("models/y_train.pkl")
y_test = joblib.load("models/y_test.pkl")

print("X_train:", X_train.shape)
print("X_test :", X_test.shape)


# ============================================================
# 2. DEFINE MODELS
# ============================================================

models = {

    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        C=2.0,
        solver="lbfgs"
    ),

    "Multinomial Naive Bayes": MultinomialNB(
        alpha=0.1
    ),

    "Linear SVM": LinearSVC(
        C=1.0,
        max_iter=2000
    )
}


# ============================================================
# 3. TRAIN AND EVALUATE MODELS
# ============================================================

results = []

print("\n" + "=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

for model_name, model in models.items():

    print(f"\nTraining: {model_name}")
    print("-" * 50)

    # Train
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        y_pred,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        y_pred,
        average="weighted"
    )

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    results.append({
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })


# ============================================================
# 4. CREATE RESULTS DATAFRAME
# ============================================================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="F1 Score",
    ascending=False
).reset_index(drop=True)


# ============================================================
# 5. DISPLAY FINAL RESULTS
# ============================================================

print("\n" + "=" * 70)
print("FINAL MODEL COMPARISON")
print("=" * 70)

print(
    results_df.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)


# ============================================================
# 6. SELECT BEST MODEL
# ============================================================

best_model_name = results_df.iloc[0]["Model"]

print("\n" + "=" * 70)
print("BEST MODEL")
print("=" * 70)

print(f"\nBest Model: {best_model_name}")
print(
    f"Best F1 Score: "
    f"{results_df.iloc[0]['F1 Score']:.4f}"
)


# ============================================================
# 7. SAVE RESULTS
# ============================================================

os.makedirs("models", exist_ok=True)

results_path = "models/model_comparison.csv"

results_df.to_csv(
    results_path,
    index=False
)

print(f"\nComparison results saved to:")
print(results_path)


# ============================================================
# 8. SAVE BEST MODEL
# ============================================================

best_model = models[best_model_name]

best_model_path = "models/best_news_classifier.pkl"

joblib.dump(
    best_model,
    best_model_path
)

print(f"\nBest model saved to:")
print(best_model_path)

print("\nStep 5 completed successfully!")
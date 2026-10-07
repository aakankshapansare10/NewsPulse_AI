import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)


# ============================================================
# 1. LOAD DATA
# ============================================================

print("\nLoading test data...")

X_test = joblib.load("models/X_test.pkl")
y_test = joblib.load("models/y_test.pkl")

print("Test data loaded successfully.")
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)


# ============================================================
# 2. LOAD BEST MODEL
# ============================================================

print("\nLoading best trained model...")

model_path = "models/best_news_classifier.pkl"

model = joblib.load(model_path)

print("Best model loaded successfully.")


# ============================================================
# 3. MAKE PREDICTIONS
# ============================================================

print("\nGenerating predictions...")

y_pred = model.predict(X_test)

print("Predictions generated successfully.")


# ============================================================
# 4. CALCULATE ACCURACY
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL ACCURACY")
print("=" * 60)

print(f"\nAccuracy: {accuracy:.4f}")
print(f"Accuracy: {accuracy * 100:.2f}%")


# ============================================================
# 5. CLASSIFICATION REPORT
# ============================================================

target_names = [
    "World",
    "Sports",
    "Business",
    "Sci-Tech"
]

report = classification_report(
    y_test,
    y_pred,
    target_names=target_names,
    output_dict=True
)

report_df = pd.DataFrame(report).transpose()

print("\n" + "=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)

print(report_df)


# ============================================================
# 6. SAVE CLASSIFICATION REPORT
# ============================================================

os.makedirs("models/evaluation", exist_ok=True)

report_path = "models/evaluation/classification_report.csv"

report_df.to_csv(report_path)

print(f"\nClassification report saved to:")
print(report_path)


# ============================================================
# 7. CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(y_test, y_pred)

print("\n" + "=" * 60)
print("CONFUSION MATRIX")
print("=" * 60)

print(cm)


# ============================================================
# 8. PLOT CONFUSION MATRIX
# ============================================================

fig, ax = plt.subplots(figsize=(8, 6))

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=target_names
)

display.plot(
    ax=ax,
    xticks_rotation=45
)

plt.title("NewsPulse AI - News Classification Confusion Matrix")

plt.tight_layout()


# ============================================================
# 9. SAVE CONFUSION MATRIX IMAGE
# ============================================================

cm_path = "models/evaluation/confusion_matrix.png"

plt.savefig(
    cm_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(f"\nConfusion matrix saved to:")
print(cm_path)


# ============================================================
# 10. SAVE METRICS SUMMARY
# ============================================================

metrics_summary = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Weighted Precision",
        "Weighted Recall",
        "Weighted F1 Score"
    ],
    "Score": [
        accuracy,
        report["weighted avg"]["precision"],
        report["weighted avg"]["recall"],
        report["weighted avg"]["f1-score"]
    ]
})

metrics_path = "models/evaluation/metrics_summary.csv"

metrics_summary.to_csv(
    metrics_path,
    index=False
)

print(f"\nMetrics summary saved to:")
print(metrics_path)


# ============================================================
# 11. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("STEP 6 COMPLETED SUCCESSFULLY!")
print("=" * 60)

print("\nGenerated files:")

print("1. models/evaluation/classification_report.csv")
print("2. models/evaluation/confusion_matrix.png")
print("3. models/evaluation/metrics_summary.csv")
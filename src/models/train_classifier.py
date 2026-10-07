import os
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# 1. LOAD TF-IDF FEATURES
# ============================================================

print("\nLoading TF-IDF features...")

X_train = joblib.load("models/X_train.pkl")
X_test = joblib.load("models/X_test.pkl")

y_train = joblib.load("models/y_train.pkl")
y_test = joblib.load("models/y_test.pkl")

print("X_train shape:", X_train.shape)
print("X_test shape :", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape :", y_test.shape)


# ============================================================
# 2. CREATE LOGISTIC REGRESSION MODEL
# ============================================================

print("\nCreating Logistic Regression model...")

model = LogisticRegression(
    max_iter=1000,
    C=2.0,
    solver="lbfgs"
)


# ============================================================
# 3. TRAIN MODEL
# ============================================================

print("\nTraining model...")
print("This may take some time...\n")

model.fit(X_train, y_train)

print("Model training completed!")


# ============================================================
# 4. MAKE PREDICTIONS
# ============================================================

print("\nMaking predictions...")

y_pred = model.predict(X_test)


# ============================================================
# 5. CALCULATE ACCURACY
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"\nAccuracy: {accuracy:.4f}")
print(f"Accuracy: {accuracy * 100:.2f}%")


# ============================================================
# 6. CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report:")
print("-" * 60)

target_names = [
    "World",
    "Sports",
    "Business",
    "Sci-Tech"
]

print(
    classification_report(
        y_test,
        y_pred,
        target_names=target_names
    )
)


# ============================================================
# 7. CONFUSION MATRIX
# ============================================================

print("\nConfusion Matrix:")
print("-" * 60)

cm = confusion_matrix(y_test, y_pred)

print(cm)


# ============================================================
# 8. SAVE TRAINED MODEL
# ============================================================

os.makedirs("models", exist_ok=True)

model_path = "models/news_classifier.pkl"

joblib.dump(model, model_path)

print("\n" + "=" * 60)
print("MODEL SAVED SUCCESSFULLY")
print("=" * 60)

print(f"\nSaved model: {model_path}")

print("\nStep 4 completed successfully!")
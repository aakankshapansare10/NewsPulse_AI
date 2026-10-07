import pandas as pd
import joblib

from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer


# ============================================================
# NEWSPULSE AI
# TF-IDF Feature Engineering
# ============================================================

print("=" * 60)
print("              NEWSPULSE AI")
print("        TF-IDF FEATURE ENGINEERING")
print("=" * 60)


# ------------------------------------------------------------
# 1. Project paths
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

TRAIN_PATH = BASE_DIR / "data" / "processed" / "train_cleaned.csv"
TEST_PATH = BASE_DIR / "data" / "processed" / "test_cleaned.csv"

MODEL_DIR = BASE_DIR / "models"

MODEL_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# 2. Load processed datasets
# ------------------------------------------------------------

print("\nLoading cleaned datasets...")

train = pd.read_csv(TRAIN_PATH)
test = pd.read_csv(TEST_PATH)

print(f"Train records: {len(train):,}")
print(f"Test records : {len(test):,}")


# ------------------------------------------------------------
# 3. Prepare text
# ------------------------------------------------------------

X_train_text = train["clean_text"]
X_test_text = test["clean_text"]

y_train = train["category"]
y_test = test["category"]


# ------------------------------------------------------------
# 4. Create TF-IDF vectorizer
# ------------------------------------------------------------

print("\nCreating TF-IDF vectorizer...")

vectorizer = TfidfVectorizer(
    max_features=20000,
    min_df=2,
    max_df=0.95,
    ngram_range=(1, 2),
    sublinear_tf=True
)


# ------------------------------------------------------------
# 5. Fit on training data
# ------------------------------------------------------------

print("Fitting TF-IDF on training data...")

X_train = vectorizer.fit_transform(X_train_text)


# ------------------------------------------------------------
# 6. Transform test data
# ------------------------------------------------------------

print("Transforming test data...")

X_test = vectorizer.transform(X_test_text)


# ------------------------------------------------------------
# 7. Display matrix information
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("TF-IDF RESULTS")
print("=" * 60)

print(f"Training matrix shape: {X_train.shape}")
print(f"Testing matrix shape : {X_test.shape}")

print(f"\nNumber of TF-IDF features: {len(vectorizer.get_feature_names_out())}")


# ------------------------------------------------------------
# 8. Display sample features
# ------------------------------------------------------------

print("\nSample TF-IDF features:")

features = vectorizer.get_feature_names_out()

for feature in features[:30]:
    print(feature)


# ------------------------------------------------------------
# 9. Save vectorizer
# ------------------------------------------------------------

vectorizer_path = MODEL_DIR / "tfidf_vectorizer.pkl"

joblib.dump(vectorizer, vectorizer_path)

print("\nTF-IDF vectorizer saved:")
print(vectorizer_path)


# ------------------------------------------------------------
# 10. Save feature matrices
# ------------------------------------------------------------

joblib.dump(X_train, MODEL_DIR / "X_train.pkl")
joblib.dump(X_test, MODEL_DIR / "X_test.pkl")

joblib.dump(y_train, MODEL_DIR / "y_train.pkl")
joblib.dump(y_test, MODEL_DIR / "y_test.pkl")


# ------------------------------------------------------------
# 11. Final message
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("TF-IDF FEATURE ENGINEERING COMPLETED!")
print("=" * 60)
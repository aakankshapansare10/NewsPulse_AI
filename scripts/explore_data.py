import pandas as pd
from pathlib import Path


# ============================================================
# NEWSPULSE AI
# Dataset Exploration
# ============================================================

print("=" * 60)
print("              NEWSPULSE AI")
print("          DATASET EXPLORATION")
print("=" * 60)


# ------------------------------------------------------------
# 1. Define dataset paths
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

TRAIN_PATH = BASE_DIR / "data" / "raw" / "train.csv"
TEST_PATH = BASE_DIR / "data" / "raw" / "test.csv"


# ------------------------------------------------------------
# 2. Check whether files exist
# ------------------------------------------------------------

if not TRAIN_PATH.exists():
    raise FileNotFoundError(f"Training dataset not found: {TRAIN_PATH}")

if not TEST_PATH.exists():
    raise FileNotFoundError(f"Testing dataset not found: {TEST_PATH}")


# ------------------------------------------------------------
# 3. Load datasets
# ------------------------------------------------------------

train = pd.read_csv(
    TRAIN_PATH,
    header=None,
    names=["category", "title", "description"]
)

test = pd.read_csv(
    TEST_PATH,
    header=None,
    names=["category", "title", "description"]
)


# ------------------------------------------------------------
# 4. Dataset shapes
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET SIZE")
print("=" * 60)

print(f"\nTrain dataset: {train.shape}")
print(f"Test dataset : {test.shape}")


# ------------------------------------------------------------
# 5. Dataset columns
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("COLUMNS")
print("=" * 60)

print(train.columns.tolist())


# ------------------------------------------------------------
# 6. First five records
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FIRST 5 TRAINING RECORDS")
print("=" * 60)

print(train.head().to_string(index=False))


# ------------------------------------------------------------
# 7. Data types
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(train.dtypes)


# ------------------------------------------------------------
# 8. Missing values
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(train.isnull().sum())


# ------------------------------------------------------------
# 9. Duplicate records
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

print(f"Duplicate rows: {train.duplicated().sum()}")


# ------------------------------------------------------------
# 10. Category mapping
# ------------------------------------------------------------

category_names = {
    1: "World",
    2: "Sports",
    3: "Business",
    4: "Sci/Tech"
}

train["category_name"] = train["category"].map(category_names)
test["category_name"] = test["category"].map(category_names)


# ------------------------------------------------------------
# 11. Category distribution
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CATEGORY DISTRIBUTION")
print("=" * 60)

category_counts = train["category_name"].value_counts()

print(category_counts)


# ------------------------------------------------------------
# 12. Percentage distribution
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CATEGORY PERCENTAGE")
print("=" * 60)

category_percentage = (
    train["category_name"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print(category_percentage)


# ------------------------------------------------------------
# 13. Text length analysis
# ------------------------------------------------------------

train["text"] = (
    train["title"].fillna("") +
    " " +
    train["description"].fillna("")
)

train["text_length"] = train["text"].str.len()


print("\n" + "=" * 60)
print("TEXT LENGTH STATISTICS")
print("=" * 60)

print(train["text_length"].describe())


# ------------------------------------------------------------
# 14. Shortest and longest articles
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("SHORTEST ARTICLE")
print("=" * 60)

shortest = train.loc[train["text_length"].idxmin()]

print(shortest["text"])


print("\n" + "=" * 60)
print("LONGEST ARTICLE")
print("=" * 60)

longest = train.loc[train["text_length"].idxmax()]

print(longest["text"][:1000])


# ------------------------------------------------------------
# 15. Final summary
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("EXPLORATION SUMMARY")
print("=" * 60)

print(f"Total training articles : {len(train):,}")
print(f"Total testing articles  : {len(test):,}")
print(f"Total articles          : {len(train) + len(test):,}")
print(f"Number of categories    : {train['category'].nunique()}")
print(f"Duplicate records       : {train.duplicated().sum()}")
print(
    f"Missing values          : "
    f"{train[['category', 'title', 'description']].isnull().sum().sum()}"
)

print("\nCategories:")

for category, count in category_counts.items():
    print(f"  {category:<12} : {count:,}")

print("\n" + "=" * 60)
print("Exploration completed successfully!")
print("=" * 60)
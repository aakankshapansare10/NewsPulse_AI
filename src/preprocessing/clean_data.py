import os
import re
import html
import pandas as pd


# ============================================================
# PATHS
# ============================================================

TRAIN_PATH = "data/raw/train.csv"
TEST_PATH = "data/raw/test.csv"

OUTPUT_DIR = "data/processed"

TRAIN_OUTPUT = os.path.join(
    OUTPUT_DIR,
    "train_cleaned.csv"
)

TEST_OUTPUT = os.path.join(
    OUTPUT_DIR,
    "test_cleaned.csv"
)


# ============================================================
# CATEGORY MAPPING
# ============================================================

CATEGORY_NAMES = {
    1: "World",
    2: "Sports",
    3: "Business",
    4: "Sci-Tech"
}


# ============================================================
# TEXT CLEANING FUNCTION
# ============================================================

def clean_text(text):

    if pd.isna(text):
        return ""

    # Convert to string
    text = str(text)

    # Decode HTML entities
    # Example: &quot; -> "
    #          &amp;  -> &
    text = html.unescape(text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove common HTML / webpage artifacts
    artifact_patterns = [
        r"\blt\b",
        r"\bgt\b",
        r"\bquot\b",
        r"\bhref\b",
        r"\bquickinfo\b",
        r"\bfullquote\b",
        r"\btarget\b",
    ]

    for pattern in artifact_patterns:
        text = re.sub(pattern, " ", text, flags=re.IGNORECASE)

    # Remove URLs
    text = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text,
        flags=re.IGNORECASE
    )

    # Remove email addresses
    text = re.sub(
        r"\S+@\S+",
        " ",
        text
    )

    # Convert everything to lowercase
    text = text.lower()

    # Keep only letters and numbers
    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    # Remove extra whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# ============================================================
# LOAD DATA
# ============================================================

def load_dataset(path):

    df = pd.read_csv(
        path,
        header=None,
        names=[
            "category",
            "title",
            "description"
        ]
    )

    return df


# ============================================================
# PROCESS DATA
# ============================================================

def process_dataset(df):

    # Map numeric categories to names
    df["category_name"] = df["category"].map(
        CATEGORY_NAMES
    )

    # Handle missing values
    df["title"] = df["title"].fillna("")
    df["description"] = df["description"].fillna("")

    # Combine title and description
    df["text"] = (
        df["title"].astype(str)
        + " "
        + df["description"].astype(str)
    )

    # Clean text
    print("Cleaning article text...")

    df["clean_text"] = df["text"].apply(
        clean_text
    )

    # Remove empty articles
    df = df[
        df["clean_text"].str.len() > 0
    ].copy()

    # Remove duplicate articles
    before_duplicates = len(df)

    df = df.drop_duplicates(
        subset=["clean_text"]
    ).copy()

    duplicates_removed = (
        before_duplicates - len(df)
    )

    # Reset index
    df = df.reset_index(drop=True)

    return df, duplicates_removed


# ============================================================
# MAIN
# ============================================================

def main():

    print("\n" + "=" * 70)
    print("                 NEWSPULSE AI")
    print("              DATA CLEANING PIPELINE")
    print("=" * 70)

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    # --------------------------------------------------------
    # TRAIN DATA
    # --------------------------------------------------------

    print("\nLoading training dataset...")

    train_df = load_dataset(
        TRAIN_PATH
    )

    print(
        f"Original training samples: "
        f"{len(train_df):,}"
    )

    train_cleaned, train_duplicates = process_dataset(
        train_df
    )

    print(
        f"Training duplicates removed: "
        f"{train_duplicates:,}"
    )

    print(
        f"Final training samples: "
        f"{len(train_cleaned):,}"
    )

    train_cleaned.to_csv(
        TRAIN_OUTPUT,
        index=False
    )

    # --------------------------------------------------------
    # TEST DATA
    # --------------------------------------------------------

    print("\nLoading testing dataset...")

    test_df = load_dataset(
        TEST_PATH
    )

    print(
        f"Original testing samples: "
        f"{len(test_df):,}"
    )

    test_cleaned, test_duplicates = process_dataset(
        test_df
    )

    print(
        f"Testing duplicates removed: "
        f"{test_duplicates:,}"
    )

    print(
        f"Final testing samples: "
        f"{len(test_cleaned):,}"
    )

    test_cleaned.to_csv(
        TEST_OUTPUT,
        index=False
    )

    # --------------------------------------------------------
    # FINAL SUMMARY
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("             CLEANING COMPLETED")
    print("=" * 70)

    print(
        f"\nTraining output: {TRAIN_OUTPUT}"
    )

    print(
        f"Testing output : {TEST_OUTPUT}"
    )

    print(
        "\nHTML/web artifacts removed:"
    )

    print("  ✓ lt")
    print("  ✓ gt")
    print("  ✓ quot")
    print("  ✓ href")
    print("  ✓ quickinfo")
    print("  ✓ fullquote")
    print("  ✓ target")

    print("\nStep 13A completed successfully!")


if __name__ == "__main__":
    main()
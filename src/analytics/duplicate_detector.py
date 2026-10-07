import os
import pandas as pd


INPUT_PATH = "data/processed/similar_news.csv"

OUTPUT_DIR = "data/processed"
OUTPUT_PATH = os.path.join(
    OUTPUT_DIR,
    "duplicate_news.csv"
)


def classify_similarity(score):

    if score >= 0.85:
        return "Likely Duplicate"

    elif score >= 0.70:
        return "Highly Similar"

    elif score >= 0.60:
        return "Related News"

    return "Low Similarity"


def main():

    print("\n" + "=" * 70)
    print("                 NEWSPULSE AI")
    print("              DUPLICATE DETECTOR")
    print("=" * 70)

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    print("\nLoading similarity results...")

    df = pd.read_csv(INPUT_PATH)

    if df.empty:
        print("\nNo similar articles found.")
        print("Nothing to classify.")
        return

    if "similarity_score" not in df.columns:
        raise ValueError(
            "Column 'similarity_score' not found."
        )

    # Classify similarity
    df["similarity_type"] = df[
        "similarity_score"
    ].apply(classify_similarity)

    # Sort highest similarity first
    df = df.sort_values(
        by="similarity_score",
        ascending=False
    ).reset_index(drop=True)

    # Add duplicate flag
    df["is_duplicate"] = (
        df["similarity_score"] >= 0.85
    )

    # Save
    df.to_csv(
        OUTPUT_PATH,
        index=False
    )

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("             DUPLICATE ANALYSIS")
    print("=" * 70)

    print(
        f"\nTotal similar pairs: "
        f"{len(df):,}"
    )

    duplicate_count = (
        df["similarity_type"]
        == "Likely Duplicate"
    ).sum()

    highly_similar_count = (
        df["similarity_type"]
        == "Highly Similar"
    ).sum()

    related_count = (
        df["similarity_type"]
        == "Related News"
    ).sum()

    print(
        f"Likely duplicates : "
        f"{duplicate_count:,}"
    )

    print(
        f"Highly similar    : "
        f"{highly_similar_count:,}"
    )

    print(
        f"Related news      : "
        f"{related_count:,}"
    )

    # --------------------------------------------------------
    # TOP DUPLICATES
    # --------------------------------------------------------

    duplicates = df[
        df["is_duplicate"] == True
    ]

    if not duplicates.empty:

        print("\nTop likely duplicate articles:")

        display_columns = [
            "similarity_score",
            "article_1_title",
            "article_2_title",
            "similarity_type"
        ]

        print(
            duplicates[
                display_columns
            ].head(10).to_string(
                index=False
            )
        )

    else:

        print(
            "\nNo highly likely duplicates "
            "were detected."
        )

    print("\nOutput saved to:")

    print(
        f"  {OUTPUT_PATH}"
    )

    print("\n" + "=" * 70)
    print("Step 14C completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
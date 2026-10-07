import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# PATHS
# ============================================================

INPUT_PATH = "data/processed/train_cleaned.csv"

OUTPUT_DIR = "data/processed"
OUTPUT_PATH = os.path.join(
    OUTPUT_DIR,
    "similar_news.csv"
)


# ============================================================
# SETTINGS
# ============================================================

MAX_ARTICLES = 5000
TOP_K = 5
SIMILARITY_THRESHOLD = 0.60


# ============================================================
# MAIN
# ============================================================

def main():

    print("\n" + "=" * 70)
    print("                 NEWSPULSE AI")
    print("             NEWS SIMILARITY ENGINE")
    print("=" * 70)

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    # --------------------------------------------------------
    # LOAD DATA
    # --------------------------------------------------------

    print("\nLoading cleaned news dataset...")

    df = pd.read_csv(INPUT_PATH)

    print(
        f"Total articles available: "
        f"{len(df):,}"
    )

    if "clean_text" not in df.columns:
        raise ValueError(
            "Column 'clean_text' not found."
        )

    # Use limited number for efficient pairwise comparison
    df = df.head(MAX_ARTICLES).copy()

    print(
        f"Articles used for similarity: "
        f"{len(df):,}"
    )

    # Remove empty text
    df = df[
        df["clean_text"].fillna("").str.strip() != ""
    ].copy()

    df = df.reset_index(drop=True)

    # --------------------------------------------------------
    # TF-IDF
    # --------------------------------------------------------

    print("\nCreating TF-IDF representation...")

    vectorizer = TfidfVectorizer(
        max_features=15000,
        min_df=2,
        max_df=0.95,
        ngram_range=(1, 2),
        stop_words="english",
        sublinear_tf=True
    )

    tfidf_matrix = vectorizer.fit_transform(
        df["clean_text"]
    )

    print(
        f"TF-IDF matrix shape: "
        f"{tfidf_matrix.shape}"
    )

    # --------------------------------------------------------
    # COSINE SIMILARITY
    # --------------------------------------------------------

    print("\nCalculating cosine similarity...")

    similarity_matrix = cosine_similarity(
        tfidf_matrix
    )

    print("Similarity calculation completed.")

    # --------------------------------------------------------
    # FIND SIMILAR ARTICLES
    # --------------------------------------------------------

    results = []

    print("\nFinding similar news articles...")

    for i in range(len(df)):

        similarity_scores = similarity_matrix[i].copy()

        # Ignore the article itself
        similarity_scores[i] = 0

        # Get highest similarity scores
        similar_indices = similarity_scores.argsort()[
            -TOP_K:
        ][::-1]

        for j in similar_indices:

            score = similarity_scores[j]

            if score >= SIMILARITY_THRESHOLD:

                results.append({
                    "article_1_id": i,
                    "article_2_id": j,
                    "similarity_score": round(
                        float(score),
                        4
                    ),
                    "article_1_title": str(
                        df.iloc[i]["title"]
                    ),
                    "article_2_title": str(
                        df.iloc[j]["title"]
                    ),
                    "category_1": str(
                        df.iloc[i]["category_name"]
                    ),
                    "category_2": str(
                        df.iloc[j]["category_name"]
                    )
                })

    # --------------------------------------------------------
    # SAVE RESULTS
    # --------------------------------------------------------

    results_df = pd.DataFrame(results)

    if not results_df.empty:

        results_df = results_df.sort_values(
            by="similarity_score",
            ascending=False
        ).reset_index(drop=True)

    results_df.to_csv(
        OUTPUT_PATH,
        index=False
    )

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("             SIMILARITY ANALYSIS")
    print("=" * 70)

    print(
        f"\nSimilar article pairs found: "
        f"{len(results_df):,}"
    )

    if not results_df.empty:

        print(
            f"Highest similarity score: "
            f"{results_df['similarity_score'].max():.4f}"
        )

        print("\nTop similar article pairs:")

        print(
            results_df.head(10).to_string(
                index=False
            )
        )

    else:

        print(
            "\nNo article pairs found above "
            f"the threshold of {SIMILARITY_THRESHOLD}."
        )

    print("\nOutput saved to:")

    print(
        f"  {OUTPUT_PATH}"
    )

    print("\n" + "=" * 70)
    print("Step 14A completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
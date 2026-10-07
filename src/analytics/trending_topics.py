import os
import pandas as pd


# ============================================================
# NEWSPULSE AI
# TRENDING TOPICS ANALYSIS
# ============================================================


# ============================================================
# 1. FILE PATHS
# ============================================================

INPUT_PATH = "models/topics/article_topics.csv"

OUTPUT_DIR = "data/processed"

OUTPUT_PATH = os.path.join(
    OUTPUT_DIR,
    "trending_topics.csv"
)


# ============================================================
# 2. MEANINGFUL TOPIC LABELS
# ============================================================

TOPIC_LABELS = {

    1: "Stock Market & Financial Data",

    2: "Corporate Earnings & Business",

    3: "Oil & Energy Markets",

    4: "US General & Political News",

    5: "War & Middle East Conflict",

    6: "Sports",

    7: "Technology & Software",

    8: "General News & Reports",

    9: "New York & US Markets",

    10: "Global Politics & International Affairs"
}


# ============================================================
# 3. CREATE OUTPUT DIRECTORY
# ============================================================

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


# ============================================================
# 4. LOAD ARTICLE TOPIC ASSIGNMENTS
# ============================================================

print("\n" + "=" * 70)
print("                 NEWSPULSE AI")
print("                TRENDING TOPICS")
print("=" * 70)

print("\nLoading article topic assignments...")

df = pd.read_csv(INPUT_PATH)

print(
    f"Loaded {len(df):,} article assignments."
)


# ============================================================
# 5. VALIDATE DATA
# ============================================================

if "topic_id" not in df.columns:

    raise ValueError(
        "The input file does not contain a 'topic_id' column."
    )


print(
    "\nAvailable columns:",
    list(df.columns)
)


# ============================================================
# 6. COUNT ARTICLES PER TOPIC
# ============================================================

print("\nCalculating topic frequencies...")

topic_counts = (
    df["topic_id"]
    .value_counts()
    .sort_index()
)


# ============================================================
# 7. CREATE DATAFRAME
# ============================================================

trending_df = pd.DataFrame({

    "topic_id": topic_counts.index,

    "article_count": topic_counts.values
})


# ============================================================
# 8. CALCULATE PERCENTAGE
# ============================================================

total_articles = (
    trending_df["article_count"].sum()
)


trending_df["percentage"] = (
    trending_df["article_count"]
    / total_articles
    * 100
)


# ============================================================
# 9. ADD MEANINGFUL TOPIC NAMES
# ============================================================

trending_df["topic_name"] = (
    trending_df["topic_id"]
    .map(TOPIC_LABELS)
)


# ============================================================
# 10. HANDLE UNKNOWN TOPICS
# ============================================================

trending_df["topic_name"] = (
    trending_df["topic_name"]
    .fillna(
        "Unknown Topic"
    )
)


# ============================================================
# 11. SORT BY TRENDING SCORE
# ============================================================

trending_df = trending_df.sort_values(

    by="article_count",

    ascending=False

).reset_index(drop=True)


# ============================================================
# 12. ADD RANK
# ============================================================

trending_df.insert(

    0,

    "rank",

    range(
        1,
        len(trending_df) + 1
    )
)


# ============================================================
# 13. ROUND PERCENTAGE
# ============================================================

trending_df["percentage"] = (
    trending_df["percentage"]
    .round(2)
)


# ============================================================
# 14. REORDER COLUMNS
# ============================================================

trending_df = trending_df[
    [
        "rank",
        "topic_id",
        "topic_name",
        "article_count",
        "percentage"
    ]
]


# ============================================================
# 15. DISPLAY TRENDING TOPICS
# ============================================================

print("\n" + "=" * 70)
print("                 TRENDING TOPICS")
print("=" * 70)

print(
    trending_df.to_string(
        index=False
    )
)


# ============================================================
# 16. SAVE RESULTS
# ============================================================

trending_df.to_csv(

    OUTPUT_PATH,

    index=False
)


# ============================================================
# 17. DISPLAY TOP 5
# ============================================================

print("\n" + "=" * 70)
print("                TOP 5 TRENDING TOPICS")
print("=" * 70)

top_5 = trending_df.head(5)

for _, row in top_5.iterrows():

    print(
        f"{int(row['rank'])}. "
        f"{row['topic_name']} "
        f"→ {int(row['article_count']):,} articles "
        f"({row['percentage']:.2f}%)"
    )


# ============================================================
# 18. FINAL OUTPUT
# ============================================================

print("\n" + "=" * 70)
print("TRENDING TOPICS SAVED SUCCESSFULLY")
print("=" * 70)

print(
    f"\nFile: {OUTPUT_PATH}"
)

print(
    f"Total articles analyzed: "
    f"{total_articles:,}"
)

print(
    f"Total topics discovered: "
    f"{len(trending_df)}"
)

print("\nStep 12 completed successfully!")
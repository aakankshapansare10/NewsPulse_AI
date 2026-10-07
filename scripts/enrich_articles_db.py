import sys
import os

import psycopg2
import pandas as pd

# Allow imports from project root
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.nlp.sentiment import analyze_sentiment


# ============================================================
# DATABASE CONFIGURATION
# ============================================================

DB_CONFIG = {
    "dbname": "newspulse_db",
    "user": "postgres",
    "password": "Postgres@5100",
    "host": "localhost",
    "port": "5100"
}


# ============================================================
# TOPIC LABELS
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
# LOAD ARTICLES
# ============================================================

def load_articles():

    conn = psycopg2.connect(**DB_CONFIG)

    query = """
        SELECT
            article_id,
            title,
            description
        FROM articles
        ORDER BY article_id;
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return df


# ============================================================
# ENRICH ARTICLES
# ============================================================

def enrich_articles(df):

    sentiments = []
    sentiment_scores = []

    for index, row in df.iterrows():

        title = str(row["title"] or "")
        description = str(
            row["description"] or ""
        )

        text = f"{title} {description}"

        result = analyze_sentiment(text)

        sentiments.append(
            result["sentiment"]
        )

        sentiment_scores.append(
            result["compound"]
        )

        if (index + 1) % 500 == 0:

            print(
                f"Processed {index + 1}/{len(df)} articles..."
            )

    df["sentiment"] = sentiments

    df["sentiment_score"] = sentiment_scores

    return df


# ============================================================
# UPDATE DATABASE
# ============================================================

def update_database(df):

    conn = psycopg2.connect(**DB_CONFIG)

    cursor = conn.cursor()

    print("\nUpdating PostgreSQL database...")

    for _, row in df.iterrows():

        cursor.execute(
            """
            UPDATE articles
            SET
                sentiment = %s,
                sentiment_score = %s
            WHERE article_id = %s;
            """,
            (
                row["sentiment"],
                float(row["sentiment_score"]),
                int(row["article_id"])
            )
        )

    conn.commit()

    cursor.close()
    conn.close()

    print("Database updated successfully.")


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 60)
    print("NewsPulse AI - Article Enrichment")
    print("=" * 60)

    print("\nLoading articles from PostgreSQL...")

    df = load_articles()

    print(
        f"Articles loaded: {len(df):,}"
    )

    if df.empty:

        print(
            "No articles found in database."
        )

        return

    print(
        "\nRunning sentiment analysis..."
    )

    df = enrich_articles(df)

    print(
        "\nSentiment distribution:"
    )

    print(
        df["sentiment"].value_counts()
    )

    update_database(df)

    print("\n" + "=" * 60)
    print("ARTICLE ENRICHMENT COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
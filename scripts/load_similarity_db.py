import getpass
import pandas as pd
import psycopg2


# ============================================================
# CONFIGURATION
# ============================================================

CSV_PATH = "data/processed/duplicate_news.csv"

DB_NAME = "newspulse_db"
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5100"


# ============================================================
# LOAD DATA
# ============================================================

print("\n" + "=" * 70)
print("                 NEWSPULSE AI")
print("          SIMILARITY DB LOADER")
print("=" * 70)

print("\nLoading duplicate/similarity data...")

df = pd.read_csv(CSV_PATH)

print(
    f"Similarity records loaded: {len(df):,}"
)


# ============================================================
# DATABASE CONNECTION
# ============================================================

print("\nConnecting to PostgreSQL...")

password = getpass.getpass(
    "Enter PostgreSQL password for user 'postgres': "
)

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=password,
    host=DB_HOST,
    port=DB_PORT
)

cursor = conn.cursor()

print("PostgreSQL connection successful.")


# ============================================================
# CLEAR EXISTING DATA
# ============================================================

print("\nClearing existing similarity records...")

cursor.execute(
    "TRUNCATE TABLE similar_articles RESTART IDENTITY;"
)

conn.commit()


# ============================================================
# INSERT DATA
# ============================================================

print("\nInserting similarity records...")

insert_query = """
INSERT INTO similar_articles
(
    article_1_id,
    article_2_id,
    similarity_score,
    similarity_type
)
VALUES
(
    %s,
    %s,
    %s,
    %s
)
"""

inserted = 0

for _, row in df.iterrows():

    cursor.execute(
        insert_query,
        (
            int(row["article_1_id"]) + 1,
            int(row["article_2_id"]) + 1,
            float(row["similarity_score"]),
            str(row["similarity_type"])
        )
    )

    inserted += 1

conn.commit()

print(
    f"{inserted:,} similarity records inserted successfully."
)


# ============================================================
# VERIFY
# ============================================================

cursor.execute(
    "SELECT COUNT(*) FROM similar_articles;"
)

count = cursor.fetchone()[0]

print("\nDatabase verification:")

print(
    f"Similarity records currently in database: "
    f"{count:,}"
)


# ============================================================
# SHOW TOP RECORDS
# ============================================================

cursor.execute(
    """
    SELECT
        similarity_id,
        article_1_id,
        article_2_id,
        similarity_score,
        similarity_type
    FROM similar_articles
    ORDER BY similarity_score DESC
    LIMIT 10;
    """
)

rows = cursor.fetchall()

print("\nTop similarity records:")

for row in rows:
    print(
        f"ID {row[0]} | "
        f"Article {row[1]} ↔ Article {row[2]} | "
        f"Score: {row[3]} | "
        f"{row[4]}"
    )


# ============================================================
# CLOSE CONNECTION
# ============================================================

cursor.close()
conn.close()

print("\n" + "=" * 70)
print("        SIMILARITY DATA LOADING COMPLETED")
print("=" * 70)

print("\nStep 15E completed successfully!")
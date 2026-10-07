import getpass
import pandas as pd
import psycopg2


# ============================================================
# CONFIGURATION
# ============================================================

CSV_PATH = "data/processed/trending_topics.csv"

DB_NAME = "newspulse_db"
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5100"


# ============================================================
# LOAD DATA
# ============================================================

print("\n" + "=" * 70)
print("                 NEWSPULSE AI")
print("               TOPIC DB LOADER")
print("=" * 70)

print("\nLoading trending topics...")

df = pd.read_csv(CSV_PATH)

print(
    f"Topics loaded: {len(df)}"
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
# CLEAR EXISTING TOPICS
# ============================================================

print("\nClearing existing topics...")

cursor.execute(
    "TRUNCATE TABLE topics CASCADE;"
)

conn.commit()


# ============================================================
# INSERT TOPICS
# ============================================================

print("\nInserting topics...")

insert_query = """
INSERT INTO topics
(
    topic_id,
    topic_name,
    article_count,
    percentage
)
VALUES
(
    %s,
    %s,
    %s,
    %s
)
"""

for _, row in df.iterrows():

    cursor.execute(
        insert_query,
        (
            int(row["topic_id"]),
            str(row["topic_name"]),
            int(row["article_count"]),
            float(row["percentage"])
        )
    )

conn.commit()

print(
    f"{len(df)} topics inserted successfully."
)


# ============================================================
# VERIFY
# ============================================================

cursor.execute(
    """
    SELECT
        topic_id,
        topic_name,
        article_count,
        percentage
    FROM topics
    ORDER BY article_count DESC;
    """
)

rows = cursor.fetchall()

print("\nTopics currently in database:\n")

for row in rows:
    print(
        f"{row[0]}. {row[1]} "
        f"→ {row[2]:,} articles "
        f"({row[3]}%)"
    )


# ============================================================
# CLOSE
# ============================================================

cursor.close()
conn.close()

print("\n" + "=" * 70)
print("             TOPIC LOADING COMPLETED")
print("=" * 70)

print("\nStep 15D completed successfully!")
import getpass
import pandas as pd
import psycopg2


# ============================================================
# CONFIGURATION
# ============================================================

CSV_PATH = "data/processed/train_cleaned.csv"

DB_NAME = "newspulse_db"
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5100"

MAX_ARTICLES = 5000


# ============================================================
# LOAD DATA
# ============================================================

print("\n" + "=" * 70)
print("                 NEWSPULSE AI")
print("              DATABASE LOADER")
print("=" * 70)

print("\nLoading cleaned news data...")

df = pd.read_csv(CSV_PATH)

# Use same 5,000 articles as similarity engine
df = df.head(MAX_ARTICLES).copy()

print(
    f"Articles selected for database: "
    f"{len(df):,}"
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

print("\nClearing existing article records...")

cursor.execute(
    "TRUNCATE TABLE articles RESTART IDENTITY CASCADE;"
)

conn.commit()


# ============================================================
# INSERT ARTICLES
# ============================================================

print("\nInserting articles...")

insert_query = """
INSERT INTO articles
(
    title,
    description,
    category
)
VALUES
(
    %s,
    %s,
    %s
)
"""

for _, row in df.iterrows():

    cursor.execute(
        insert_query,
        (
            str(row["title"]),
            str(row["description"]),
            str(row["category_name"])
        )
    )

conn.commit()

print(
    f"{len(df):,} articles inserted successfully."
)


# ============================================================
# VERIFY
# ============================================================

cursor.execute(
    "SELECT COUNT(*) FROM articles;"
)

count = cursor.fetchone()[0]

print("\nDatabase verification:")
print(
    f"Articles currently in database: {count:,}"
)


# ============================================================
# CLOSE CONNECTION
# ============================================================

cursor.close()
conn.close()

print("\n" + "=" * 70)
print("          DATABASE LOADING COMPLETED")
print("=" * 70)

print("\nStep 15C completed successfully!")
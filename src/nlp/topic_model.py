import os
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF


# ============================================================
# PATHS
# ============================================================

INPUT_PATH = "data/processed/train_cleaned.csv"

MODEL_DIR = "models/topics"

VECTORIZER_PATH = os.path.join(
    MODEL_DIR,
    "topic_vectorizer.pkl"
)

NMF_MODEL_PATH = os.path.join(
    MODEL_DIR,
    "nmf_topic_model.pkl"
)

TOPIC_WORDS_PATH = os.path.join(
    MODEL_DIR,
    "topic_keywords.csv"
)


# ============================================================
# CREATE MODEL DIRECTORY
# ============================================================

os.makedirs(
    MODEL_DIR,
    exist_ok=True
)


# ============================================================
# 1. LOAD CLEANED DATA
# ============================================================

print("\nLoading cleaned news dataset...")

df = pd.read_csv(INPUT_PATH)

print(
    f"Loaded {len(df):,} articles."
)

print(
    "Columns:",
    list(df.columns)
)


# ============================================================
# 2. CHECK TEXT COLUMN
# ============================================================

if "clean_text" in df.columns:

    text_column = "clean_text"

elif "text" in df.columns:

    text_column = "text"

else:

    raise ValueError(
        "Could not find clean_text or text column."
    )


texts = (
    df[text_column]
    .fillna("")
    .astype(str)
)


# Remove empty documents

texts = texts[
    texts.str.strip() != ""
]


print(
    f"Usable articles: {len(texts):,}"
)


# ============================================================
# 3. CREATE TF-IDF FEATURES FOR TOPIC MODEL
# ============================================================

print("\nCreating TF-IDF representation...")

vectorizer = TfidfVectorizer(
    max_features=10000,
    min_df=5,
    max_df=0.95,
    ngram_range=(1, 2),
    stop_words="english"
)


X = vectorizer.fit_transform(texts)


print(
    "TF-IDF matrix shape:",
    X.shape
)


# ============================================================
# 4. CREATE NMF TOPIC MODEL
# ============================================================

NUMBER_OF_TOPICS = 10

print(
    f"\nCreating NMF model with "
    f"{NUMBER_OF_TOPICS} topics..."
)

nmf = NMF(
    n_components=NUMBER_OF_TOPICS,
    random_state=42,
    init="nndsvda",
    max_iter=300
)


# ============================================================
# 5. TRAIN NMF
# ============================================================

print("\nTraining topic model...")
print("This may take some time...\n")

W = nmf.fit_transform(X)

print("Topic model training completed!")


# ============================================================
# 6. EXTRACT TOP WORDS FOR EACH TOPIC
# ============================================================

feature_names = vectorizer.get_feature_names_out()

topic_rows = []

print("\n" + "=" * 70)
print("DISCOVERED TOPICS")
print("=" * 70)


for topic_number, topic in enumerate(nmf.components_):

    top_indices = topic.argsort()[-15:][::-1]

    top_words = [
        feature_names[index]
        for index in top_indices
    ]

    print(
        f"\nTopic {topic_number + 1}:"
    )

    print(
        ", ".join(top_words)
    )


    topic_rows.append({
        "topic_id": topic_number + 1,
        "keywords": ", ".join(top_words)
    })


# ============================================================
# 7. CREATE TOPIC DATAFRAME
# ============================================================

topic_df = pd.DataFrame(
    topic_rows
)


# ============================================================
# 8. SAVE TOPIC KEYWORDS
# ============================================================

topic_df.to_csv(
    TOPIC_WORDS_PATH,
    index=False
)


print(
    f"\nTopic keywords saved to:"
)

print(
    TOPIC_WORDS_PATH
)


# ============================================================
# 9. SAVE TF-IDF VECTORIZER
# ============================================================

joblib.dump(
    vectorizer,
    VECTORIZER_PATH
)


print(
    f"\nTopic vectorizer saved to:"
)

print(
    VECTORIZER_PATH
)


# ============================================================
# 10. SAVE NMF MODEL
# ============================================================

joblib.dump(
    nmf,
    NMF_MODEL_PATH
)


print(
    f"\nNMF model saved to:"
)

print(
    NMF_MODEL_PATH
)


# ============================================================
# 11. SAVE TOPIC ASSIGNMENTS
# ============================================================

topic_assignments = W.argmax(
    axis=1
) + 1


topic_assignment_df = pd.DataFrame({
    "article_index": range(
        len(topic_assignments)
    ),
    "topic_id": topic_assignments
})


topic_assignment_path = os.path.join(
    MODEL_DIR,
    "article_topics.csv"
)


topic_assignment_df.to_csv(
    topic_assignment_path,
    index=False
)


print(
    f"\nArticle topic assignments saved to:"
)

print(
    topic_assignment_path
)


# ============================================================
# 12. FINAL OUTPUT
# ============================================================

print("\n" + "=" * 70)
print("STEP 10 COMPLETED SUCCESSFULLY!")
print("=" * 70)

print("\nGenerated files:")

print(
    "1. models/topics/topic_vectorizer.pkl"
)

print(
    "2. models/topics/nmf_topic_model.pkl"
)

print(
    "3. models/topics/topic_keywords.csv"
)

print(
    "4. models/topics/article_topics.csv"
)
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from src.api.database import get_connection
from src.nlp.news_intelligence import analyze_news


app = FastAPI(
    title="NewsPulse AI",
    description="AI-powered News Intelligence API",
    version="1.0.0"
)


# ==========================================
# FRONTEND
# ==========================================

app.mount(
    "/static",
    StaticFiles(directory="frontend"),
    name="static"
)


@app.get("/dashboard")
def dashboard():
    return FileResponse("frontend/index.html")


# ==========================================
# REQUEST MODEL
# ==========================================

class NewsRequest(BaseModel):
    text: str


# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Welcome to NewsPulse AI API",
        "status": "running",
        "version": "1.0.0"
    }


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health_check():

    try:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT 1;")

        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result[0] == 1:

            return {
                "status": "healthy",
                "database": "connected"
            }

    except Exception as e:

        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }


# ==========================================
# ARTICLES
# ==========================================

@app.get("/articles")
def get_articles(limit: int = 20):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            article_id,
            title,
            description,
            category,
            created_at
        FROM articles
        ORDER BY article_id
        LIMIT %s;
    """

    cursor.execute(query, (limit,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    articles = []

    for row in rows:

        articles.append({
            "article_id": row[0],
            "title": row[1],
            "description": row[2],
            "category": row[3],
            "created_at": row[4]
        })

    return {
        "count": len(articles),
        "articles": articles
    }


# ==========================================
# TRENDING TOPICS
# ==========================================

@app.get("/trending")
def get_trending_topics():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            topic_id,
            topic_name,
            article_count,
            percentage
        FROM topics
        ORDER BY article_count DESC;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    topics = []

    for row in rows:

        topics.append({
            "topic_id": row[0],
            "topic_name": row[1],
            "article_count": row[2],
            "percentage": float(row[3])
        })

    return {
        "count": len(topics),
        "trending_topics": topics
    }


# ==========================================
# SIMILAR ARTICLES
# ==========================================

@app.get("/similar/{article_id}")
def get_similar_articles(article_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            s.article_2_id,
            a.title,
            a.category,
            s.similarity_score,
            s.similarity_type
        FROM similar_articles s
        JOIN articles a
            ON s.article_2_id = a.article_id
        WHERE s.article_1_id = %s
        ORDER BY s.similarity_score DESC
        LIMIT 5;
    """

    cursor.execute(query, (article_id,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    similar_articles = []

    for row in rows:

        similar_articles.append({
            "article_id": row[0],
            "title": row[1],
            "category": row[2],
            "similarity_score": float(row[3]),
            "similarity_type": row[4]
        })

    return {
        "article_id": article_id,
        "count": len(similar_articles),
        "similar_articles": similar_articles
    }


# ==========================================
# AI NEWS PREDICTION
# ==========================================

@app.post("/predict")
def predict_news(request: NewsRequest):

    result = analyze_news(request.text)

    return {
        "article": request.text,
        "prediction": result
    }


# ==========================================
# DASHBOARD STATISTICS
# ==========================================

@app.get("/stats")
def get_statistics():

    conn = get_connection()
    cursor = conn.cursor()

    # Total articles
    cursor.execute(
        "SELECT COUNT(*) FROM articles;"
    )

    total_articles = cursor.fetchone()[0]


    # Total categories
    cursor.execute("""
        SELECT COUNT(DISTINCT category)
        FROM articles
        WHERE category IS NOT NULL;
    """)

    total_categories = cursor.fetchone()[0]


    # Total topics
    cursor.execute(
        "SELECT COUNT(*) FROM topics;"
    )

    total_topics = cursor.fetchone()[0]


    # Sentiment distribution
    cursor.execute("""
        SELECT sentiment, COUNT(*)
        FROM articles
        WHERE sentiment IS NOT NULL
        GROUP BY sentiment
        ORDER BY COUNT(*) DESC;
    """)

    sentiment_rows = cursor.fetchall()

    sentiment_distribution = {}

    for row in sentiment_rows:

        sentiment_distribution[row[0]] = row[1]


    # Category distribution
    cursor.execute("""
        SELECT category, COUNT(*)
        FROM articles
        WHERE category IS NOT NULL
        GROUP BY category
        ORDER BY COUNT(*) DESC;
    """)

    category_rows = cursor.fetchall()

    category_distribution = {}

    for row in category_rows:

        category_distribution[row[0]] = row[1]


    cursor.close()
    conn.close()


    return {

        "total_articles": total_articles,

        "total_categories": total_categories,

        "total_topics": total_topics,

        "sentiment_distribution":
            sentiment_distribution,

        "category_distribution":
            category_distribution

    }
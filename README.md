# NewsPulse AI

## AI-Powered News Intelligence & Trend Detection Platform

NewsPulse AI is an end-to-end Machine Learning and Natural Language Processing platform that transforms raw news articles into structured, searchable intelligence.

The platform combines text classification, sentiment analysis, topic modeling, trending-topic detection, similarity analysis, PostgreSQL, FastAPI, and an interactive web dashboard into one complete data science application.

---

## Overview

NewsPulse AI follows a complete data-to-application pipeline:

```text
Raw News Dataset
       ↓
Data Cleaning & Preprocessing
       ↓
TF-IDF Feature Engineering
       ↓
Machine Learning Classification
       ↓
NLP Intelligence
 ┌─────┼─────────────┐
 ↓     ↓             ↓
Sentiment  Topic     Similarity
Analysis   Modeling  & Duplicates
 └─────┼─────────────┘
       ↓
PostgreSQL
       ↓
FastAPI REST API
       ↓
Interactive Dashboard
```

---

## Key Features

- **News Classification** — classifies articles into World, Sports, Business, and Sci-Tech.
- **Sentiment Analysis** — identifies positive, neutral, and negative sentiment with VADER.
- **Topic Modeling** — discovers hidden themes using NMF.
- **Trending Topics** — ranks the most frequent news topics.
- **Similar News Detection** — finds related articles using TF-IDF and cosine similarity.
- **Duplicate Detection** — identifies likely duplicate and highly similar stories.
- **AI News Analyzer** — analyzes a user-provided headline or article instantly.
- **PostgreSQL Storage** — stores articles, topics, sentiment, and similarity relationships.
- **FastAPI Backend** — exposes the intelligence layer through REST endpoints.
- **Interactive Dashboard** — visualizes news statistics, trends, sentiment, and predictions.

---

## Tech Stack

| Layer | Technologies |
|---|---|
| Language | Python, SQL, JavaScript, HTML, CSS |
| Data Science | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF, VADER, NMF |
| Similarity | Cosine Similarity |
| Backend | FastAPI, Uvicorn, Pydantic |
| Database | PostgreSQL, psycopg2 |
| Frontend | HTML5, CSS3, JavaScript, Chart.js |
| Development | VS Code, Git, GitHub |

---

## Dataset

NewsPulse AI uses the **AG News dataset** for news classification and NLP experimentation.

### Categories

| Label | Category |
|---:|---|
| 1 | World |
| 2 | Sports |
| 3 | Business |
| 4 | Sci-Tech |

The raw dataset is intentionally excluded from GitHub using `.gitignore`.

---

## Machine Learning Pipeline

### 1. Data Cleaning

The preprocessing pipeline:

- loads the raw AG News files
- maps category labels
- handles missing values
- combines title and description
- removes HTML artifacts
- removes URLs and emails
- normalizes text
- removes duplicate articles
- removes empty records

Generated files:

```text
data/processed/train_cleaned.csv
data/processed/test_cleaned.csv
```

### 2. TF-IDF Feature Engineering

The project uses TF-IDF with:

- unigrams
- bigrams
- minimum document frequency filtering
- maximum document frequency filtering
- sublinear term frequency scaling

The trained vectorizer is reused during inference.

### 3. Model Comparison

The following classifiers are evaluated:

- Logistic Regression
- Multinomial Naive Bayes
- Linear SVM

Models are compared using:

- Accuracy
- Precision
- Recall
- F1 Score

The best-performing model is selected for inference.

---

## NLP Intelligence

### Sentiment Analysis

VADER generates:

- sentiment label
- compound score
- positive score
- negative score
- neutral score

### Topic Modeling

NMF is used to discover hidden themes across the news corpus.

The current topic labels include:

1. Stock Market & Financial Data
2. Corporate Earnings & Business
3. Oil & Energy Markets
4. US General & Political News
5. War & Middle East Conflict
6. Sports
7. Technology & Software
8. General News & Reports
9. New York & US Markets
10. Global Politics & International Affairs

### Trending Topics

Topic frequencies are aggregated and ranked to identify the most prominent themes.

### Similarity & Duplicate Detection

Cosine similarity is calculated between TF-IDF representations.

Current similarity interpretation:

| Score | Classification |
|---:|---|
| >= 0.85 | Likely Duplicate |
| 0.70–0.85 | Highly Similar |
| 0.60–0.70 | Related News |

---

## Database Design

PostgreSQL is used for persistent storage.

### `articles`

Stores analyzed news articles.

```text
article_id
title
description
category
sentiment
sentiment_score
topic_id
topic_name
created_at
```

### `topics`

Stores topic-level analytics.

```text
topic_id
topic_name
article_count
percentage
```

### `similar_articles`

Stores relationships between similar articles.

```text
similarity_id
article_1_id
article_2_id
similarity_score
similarity_type
```

Indexes are created for commonly queried fields such as category, sentiment, topic, and similarity score.

---

## FastAPI Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | API and database health |
| GET | `/articles` | Retrieve stored articles |
| GET | `/trending` | Retrieve trending topics |
| GET | `/similar/{article_id}` | Retrieve similar articles |
| POST | `/predict` | Analyze a news article with AI |
| GET | `/stats` | Retrieve dashboard statistics |

### Example AI Request

```json
{
  "text": "Apple announced a major investment in artificial intelligence technology."
}
```

The `/predict` endpoint returns category prediction, confidence, sentiment, and sentiment score.

---

## Dashboard

The dashboard is served directly through FastAPI.

### Dashboard URL

```text
http://127.0.0.1:8000/dashboard
```

### Main Dashboard Components

- Total article count
- Number of categories
- Number of detected topics
- AI system status
- Category distribution chart
- Sentiment distribution chart
- Trending topic cards
- News feed
- AI News Analyzer

### AI News Analyzer

Users can paste any news headline or article and receive:

```text
Predicted Category
Category Confidence
Sentiment
Sentiment Score
```

---

## Project Structure

```text
NewsPulse_AI/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── models/
│   └── evaluation/
│
├── scripts/
│   ├── explore_data.py
│   ├── load_articles_db.py
│   ├── load_topics_db.py
│   ├── load_similarity_db.py
│   └── enrich_articles_db.py
│
├── src/
│   ├── ingestion/
│   ├── preprocessing/
│   │   └── clean_data.py
│   │
│   ├── nlp/
│   │   ├── tfidf_features.py
│   │   ├── predict.py
│   │   ├── sentiment.py
│   │   ├── news_intelligence.py
│   │   └── topic_model.py
│   │
│   ├── analytics/
│   │   ├── trending_topics.py
│   │   ├── similarity.py
│   │   └── duplicate_detector.py
│   │
│   ├── models/
│   │   ├── train_classifier.py
│   │   ├── compare_models.py
│   │   └── evaluate_model.py
│   │
│   └── api/
│       ├── main.py
│       └── database.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── tests/
│
├── download_dataset.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/aakankshapansare10/NewsPulse_AI.git
cd NewsPulse_AI
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## PostgreSQL Setup

Create a PostgreSQL database named:

```text
newspulse_db
```

Configure your local PostgreSQL credentials in:

```text
src/api/database.py
```

Do not commit database passwords or other secrets to GitHub.

---

## Running the Project

### Download the dataset

```bash
python download_dataset.py
```

### Clean the dataset

```bash
python src/preprocessing/clean_data.py
```

### Generate TF-IDF features

```bash
python src/nlp/tfidf_features.py
```

### Train the classifier

```bash
python src/models/train_classifier.py
```

### Compare models

```bash
python src/models/compare_models.py
```

### Evaluate the best model

```bash
python src/models/evaluate_model.py
```

### Run topic modeling

```bash
python src/nlp/topic_model.py
```

### Generate trending topics

```bash
python src/analytics/trending_topics.py
```

### Generate similarity data

```bash
python src/analytics/similarity.py
```

### Detect duplicate news

```bash
python src/analytics/duplicate_detector.py
```

### Load articles into PostgreSQL

```bash
python scripts/load_articles_db.py
```

### Load topics

```bash
python scripts/load_topics_db.py
```

### Load similarity data

```bash
python scripts/load_similarity_db.py
```

### Enrich articles with sentiment

```bash
python scripts/enrich_articles_db.py
```

---

## Running the API

Start FastAPI:

```bash
uvicorn src.api.main:app --reload
```

### API

```text
http://127.0.0.1:8000
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

### Dashboard

```text
http://127.0.0.1:8000/dashboard
```

---

## Model Evaluation Artifacts

The project generates evaluation files including:

```text
models/model_comparison.csv
models/evaluation/classification_report.csv
models/evaluation/confusion_matrix.png
models/evaluation/metrics_summary.csv
```

Topic modeling artifacts:

```text
models/topics/topic_vectorizer.pkl
models/topics/nmf_topic_model.pkl
models/topics/topic_keywords.csv
models/topics/article_topics.csv
```

Generated analytics include:

```text
data/processed/trending_topics.csv
data/processed/similar_news.csv
data/processed/duplicate_news.csv
```

Large datasets and trained binary models are excluded from version control where appropriate.

---

## Screenshots

Screenshots can be added to the repository under:

```text
screenshots/
├── dashboard.png
├── ai-analyzer.png
└── api-docs.png
```

Recommended screenshots:

1. Main NewsPulse AI dashboard
2. Trending Topics and charts
3. AI News Analyzer result
4. FastAPI Swagger documentation

---

## Engineering Decisions

### Why TF-IDF?

TF-IDF provides a fast and interpretable representation for traditional machine learning text classification.

### Why compare multiple models?

Model comparison allows the system to select a classifier using measured performance rather than relying on a single algorithm.

### Why PostgreSQL?

PostgreSQL provides reliable structured storage and supports efficient querying of articles, topics, sentiment, and similarity relationships.

### Why FastAPI?

FastAPI provides a lightweight API layer with automatic OpenAPI/Swagger documentation and strong Python integration.

### Why a separate frontend?

Separating the frontend from the ML and database layers keeps the application modular and easier to maintain.

---

## Project Results

The completed system supports:

- 4-category news classification
- sentiment analysis
- 10-topic NMF topic modeling
- trending topic analysis
- article similarity analysis
- duplicate detection
- PostgreSQL persistence
- REST API access
- interactive dashboard
- real-time article prediction through the trained ML pipeline

Actual model metrics are generated automatically and stored under:

```text
models/model_comparison.csv
models/evaluation/
```

This keeps the README accurate without hard-coding unverified performance numbers.

---

## Future Improvements

Planned improvements include:

- Live news API ingestion
- Scheduled news collection
- Real-time trend monitoring
- Named Entity Recognition
- AI-powered article summarization
- LLM integration
- News credibility scoring
- Event detection
- Semantic search
- Vector database integration
- Personalized news recommendations
- User authentication
- Real-time dashboard updates
- Docker containerization
- Cloud deployment
- CI/CD pipeline
- Automated model retraining

---

## Skills Demonstrated

This project demonstrates practical experience in:

- Python
- Data Science
- Machine Learning
- Natural Language Processing
- Text Classification
- Feature Engineering
- Topic Modeling
- Sentiment Analysis
- Similarity Analysis
- SQL
- PostgreSQL
- REST API Development
- FastAPI
- Data Visualization
- Frontend Development
- Git
- GitHub
- Software Project Architecture

---

## Author

**Aakanksha Pansare**

BSc Data Science & Big Data Analysis  
MIT World Peace University, Pune

GitHub:  
https://github.com/aakankshapansare10

---

## License

This project is developed for educational, portfolio, and demonstration purposes.

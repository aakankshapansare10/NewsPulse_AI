Haan bhai, samajh gaya. Tum README mein exactly kya-kya hona chahiye, ek saath complete structure chahte ho — baar-baar sections add nahi karne.

For NewsPulse AI, README mein ye complete sections hone chahiye:

README complete structure
Project Title
NewsPulse AI
One-line tagline
Project Overview
Project kya karta hai
Problem kya solve karta hai
AI/ML ka use kaha hai
Key Features
News classification
Sentiment analysis
Topic modeling
Trending topics
Similar/duplicate news detection
AI analyzer
PostgreSQL storage
FastAPI API
Dashboard
Demo / Screenshots
Dashboard screenshot
AI Analyzer screenshot
Swagger/API screenshot
Charts screenshot

System Architecture

Dataset
   ↓
Data Cleaning
   ↓
TF-IDF
   ↓
ML + NLP
   ↓
PostgreSQL
   ↓
FastAPI
   ↓
Dashboard
Tech Stack
Python
Pandas / NumPy
Scikit-learn
VADER
PostgreSQL
FastAPI
HTML/CSS/JavaScript
Chart.js
Git/GitHub
Dataset
AG News
Number of categories
Category names
Dataset source
Dataset intentionally excluded from GitHub
Data Processing Pipeline
Raw data
Cleaning
Duplicate removal
Text normalization
TF-IDF
Machine Learning
Logistic Regression
Multinomial Naive Bayes
Linear SVM
Model comparison
Best model selection
Model Evaluation
Accuracy
Precision
Recall
F1-score
Confusion matrix
Actual model results
NLP Features
Sentiment analysis
Topic modeling
Trending topics
Similarity detection
Duplicate detection
Database Design
articles
topics
similar_articles
Important columns/relationships
API Documentation
GET /
GET /health
GET /articles
GET /trending
GET /similar/{article_id}
POST /predict
GET /stats
Dashboard
Dashboard overview
News feed
Trending topics
Category chart
Sentiment chart
AI analyzer
Project Structure
NewsPulse_AI/
├── data/
├── models/
├── scripts/
├── src/
├── frontend/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
Installation
Clone repository
Create virtual environment
Activate environment
Install requirements
Database Setup
PostgreSQL requirement
Database name
Tables
Configuration
Running the Project
Download dataset
Run preprocessing
Generate features
Train model
Evaluate model
Run API
Open dashboard
API / Dashboard URLs
API:
http://127.0.0.1:8000

Swagger:
http://127.0.0.1:8000/docs

Dashboard:
http://127.0.0.1:8000/dashboard
Results
Dataset size
Model performance
Number of topics
Articles stored
Similarity results
Screenshots
Engineering Decisions
Why TF-IDF
Why multiple ML models
Why PostgreSQL
Why FastAPI
Why separate frontend/backend
Future Improvements
Live news APIs
Real-time ingestion
LLM summarization
NER
News credibility scoring
Vector database
Docker
Cloud deployment
CI/CD
Skills Demonstrated
Python
Data Science
Machine Learning
NLP
SQL
PostgreSQL
REST APIs
Frontend
Git/GitHub
Author
Your name
Degree
University
License
One important thing

README mein fake results nahi daalenge. For example, model accuracy agar 92.4% actually nahi aayi hai, toh hum 92.4% nahi likhenge.

Tumhare project ke actual results jo files mein hain:

models/model_comparison.csv
models/evaluation/metrics_summary.csv
models/evaluation/classification_report.csv

unse exact numbers README mein daalenge.

Best approach

Main tumhare liye ek single final README.md bana sakta hoon jisme upar ke saare sections already properly written honge, including professional formatting, badges, architecture, API table, installation, results placeholders, screenshots section, etc.

Tumhe bas:

Ctrl+A → paste → Ctrl+S → git add → commit → push

karna padega.

That's the cleanest way for your GitHub portfolio.

cope paste ka de de

Haan bhai, ye complete final README.md hai. Existing README ko Ctrl+A → paste → Ctrl+S kar dena.

# NewsPulse AI

## AI-Powered News Intelligence & Trend Detection Platform

NewsPulse AI is an end-to-end Machine Learning and Natural Language Processing platform designed to transform raw news articles into meaningful intelligence.

The platform automatically classifies news articles, analyzes sentiment, discovers hidden topics, identifies trending subjects, detects similar or duplicate news, stores results in PostgreSQL, and exposes the intelligence through a FastAPI backend and interactive web dashboard.

---

## Project Overview

NewsPulse AI demonstrates a complete Data Science and Machine Learning workflow:

```text
Raw News Data
      ↓
Data Cleaning & Preprocessing
      ↓
TF-IDF Feature Engineering
      ↓
Machine Learning Classification
      ↓
NLP Analysis
      ↓
Topic Modeling
      ↓
Similarity & Duplicate Detection
      ↓
PostgreSQL Database
      ↓
FastAPI REST API
      ↓
Interactive Web Dashboard

The project combines Data Science, Machine Learning, NLP, Database Engineering, Backend Development, and Frontend Development into a single production-style application.

Key Features
News Classification

Automatically classifies news articles into:

World
Sports
Business
Sci-Tech
Sentiment Analysis

Analyzes the emotional tone of news articles:

Positive
Neutral
Negative

Also generates a compound sentiment score.

Topic Modeling

Discovers hidden topics and themes from thousands of news articles using NMF.

Trending Topics

Ranks the most frequently occurring topics to identify major news trends.

Similar News Detection

Uses TF-IDF and cosine similarity to identify articles discussing similar stories.

Duplicate Detection

Categorizes articles based on similarity:

Likely Duplicate
Highly Similar
Related News
AI News Analyzer

Users can paste any headline or article into the dashboard and receive:

Predicted category
Prediction confidence
Sentiment
Sentiment score
PostgreSQL Database

Stores:

News articles
Categories
Sentiment information
Topics
Similarity relationships
FastAPI Backend

Provides REST API endpoints for accessing the NewsPulse AI intelligence layer.

Interactive Dashboard

Provides:

News statistics
Category distribution
Sentiment distribution
Trending topics
News feed
AI article analyzer
System Architecture
                         ┌─────────────────────┐
                         │     AG News Dataset │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Data Preprocessing  │
                         │ Cleaning & Filtering│
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   TF-IDF Features   │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    │               │                │
                    ▼               ▼                ▼
             ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
             │ ML Models   │ │ Sentiment   │ │ NMF Topic   │
             │             │ │ Analysis    │ │ Modeling    │
             └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
                    │               │                │
                    └───────────────┼────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ News Intelligence   │
                         │     Pipeline        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     PostgreSQL      │
                         │      Database       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      FastAPI        │
                         │      REST API       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Web Dashboard      │
                         │ HTML/CSS/JavaScript │
                         │      Chart.js       │
                         └─────────────────────┘
Technology Stack
Programming Languages
Python
SQL
JavaScript
HTML
CSS
Data Science & Machine Learning
Pandas
NumPy
Scikit-learn
TF-IDF
Logistic Regression
Multinomial Naive Bayes
Linear SVM
NMF
Cosine Similarity
Natural Language Processing
Text preprocessing
TF-IDF
VADER Sentiment Analysis
Topic Modeling
Similarity Analysis
Backend
FastAPI
Uvicorn
Pydantic
psycopg2
Database
PostgreSQL
Frontend
HTML5
CSS3
JavaScript
Chart.js
Development Tools
VS Code
Git
GitHub
Python Virtual Environment
Dataset

NewsPulse AI uses the AG News Dataset.

The dataset contains four major news categories:

Category	Description
World	International and global news
Sports	Sports-related news
Business	Business and financial news
Sci-Tech	Science and technology news

The dataset is used for supervised news classification and NLP experimentation.

The raw dataset is intentionally excluded from the GitHub repository through .gitignore.

Data Processing Pipeline

The preprocessing pipeline performs the following operations:

Load raw news data
Assign category names
Handle missing values
Combine title and description
Decode HTML entities
Remove HTML tags
Remove URLs and emails
Remove unwanted webpage artifacts
Convert text to lowercase
Normalize whitespace
Remove duplicate articles
Remove empty records
Save cleaned datasets

Output:

data/processed/train_cleaned.csv
data/processed/test_cleaned.csv
Machine Learning Pipeline

NewsPulse AI compares multiple machine learning algorithms.

Models
Logistic Regression
Multinomial Naive Bayes
Linear SVM

The models are evaluated using:

Accuracy
Precision
Recall
F1 Score

The best-performing model is selected for production inference.

TF-IDF Feature Engineering

TF-IDF is used to convert news text into numerical feature vectors.

The implementation uses:

Unigrams
Bigrams
Sublinear TF
Minimum Document Frequency
Maximum Document Frequency

The trained vectorizer is saved and reused during prediction.

Sentiment Analysis

NewsPulse AI uses VADER sentiment analysis.

For every article, the system generates:

Sentiment
Compound Score
Positive Score
Negative Score
Neutral Score

The sentiment information is stored in PostgreSQL and visualized in the dashboard.

Topic Modeling

NMF (Non-negative Matrix Factorization) is used to discover hidden topics in the news corpus.

The project currently identifies 10 major topic groups:

Stock Market & Financial Data
Corporate Earnings & Business
Oil & Energy Markets
US General & Political News
War & Middle East Conflict
Sports
Technology & Software
General News & Reports
New York & US Markets
Global Politics & International Affairs

Topic results are used to generate the trending topic dashboard.

Similarity & Duplicate Detection

NewsPulse AI uses TF-IDF vectors and cosine similarity to compare articles.

Similarity categories:

Similarity Score	Classification
>= 0.85	Likely Duplicate
0.70 - 0.85	Highly Similar
0.60 - 0.70	Related News

This allows the system to identify repeated coverage and related stories.

Database Design

NewsPulse AI uses PostgreSQL for persistent storage.

Articles Table

Stores analyzed news articles.

article_id
title
description
category
sentiment
sentiment_score
topic_id
topic_name
created_at
Topics Table

Stores topic analytics.

topic_id
topic_name
article_count
percentage
Similar Articles Table

Stores article similarity relationships.

similarity_id
article_1_id
article_2_id
similarity_score
similarity_type
API Endpoints
Home
GET /

Returns basic API information.

Health Check
GET /health

Checks API and PostgreSQL connectivity.

Articles
GET /articles

Returns stored news articles.

Example:

GET /articles?limit=10
Trending Topics
GET /trending

Returns the most frequently occurring news topics.

Similar Articles
GET /similar/{article_id}

Returns similar articles for a selected article.

Example:

GET /similar/1
AI Prediction
POST /predict

Analyzes a news article using the machine learning and NLP pipeline.

Example request:

{
    "text": "Apple announced a major investment in artificial intelligence technology."
}

Example response structure:

{
    "article": "Apple announced a major investment in artificial intelligence technology.",
    "prediction": {
        "category": "Sci-Tech",
        "category_confidence": 0.95,
        "sentiment": "positive",
        "compound": 0.4
    }
}
Statistics
GET /stats

Returns:

Total articles
Total categories
Total topics
Sentiment distribution
Category distribution
Dashboard

The NewsPulse AI dashboard provides a centralized interface for exploring news intelligence.

Dashboard Overview

Displays:

Total Articles
Total Categories
Topics Detected
AI System Status
Analytics

Includes:

Category distribution chart
Sentiment distribution chart
Trending topic cards
News Feed

Displays articles stored in PostgreSQL.

AI News Analyzer

Allows users to paste any news article and receive AI-powered classification and sentiment analysis.

Project Structure
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
│   │
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
Installation
1. Clone the Repository
git clone https://github.com/aakankshapansare10/NewsPulse_AI.git
cd NewsPulse_AI
2. Create Virtual Environment

Windows:

python -m venv .venv

Activate:

.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
Database Setup

Install PostgreSQL and create a database named:

newspulse_db

The project uses PostgreSQL for storing:

Articles
Topics
Sentiment results
Similar articles

Configure your local PostgreSQL credentials inside:

src/api/database.py

Never commit passwords or secrets to GitHub.

Running the Project
Download Dataset
python download_dataset.py
Clean the Dataset
python src/preprocessing/clean_data.py
Generate TF-IDF Features
python src/nlp/tfidf_features.py
Train Classifier
python src/models/train_classifier.py
Compare Models
python src/models/compare_models.py
Evaluate Model
python src/models/evaluate_model.py
Run Topic Modeling
python src/nlp/topic_model.py
Generate Trending Topics
python src/analytics/trending_topics.py
Generate Similarity Data
python src/analytics/similarity.py
Detect Duplicate News
python src/analytics/duplicate_detector.py
Load Data into PostgreSQL
python scripts/load_articles_db.py
python scripts/load_topics_db.py
python scripts/load_similarity_db.py
python scripts/enrich_articles_db.py
Run FastAPI

Start the backend:

uvicorn src.api.main:app --reload

API:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs

Dashboard:

http://127.0.0.1:8000/dashboard
Model Evaluation

The project compares:

Logistic Regression
Multinomial Naive Bayes
Linear SVM

Evaluation metrics:

Accuracy
Precision
Recall
F1 Score

Generated evaluation files:

models/model_comparison.csv
models/evaluation/classification_report.csv
models/evaluation/confusion_matrix.png
models/evaluation/metrics_summary.csv
Generated Outputs

The project generates the following important artifacts:

models/
├── best_news_classifier.pkl
├── news_classifier.pkl
├── tfidf_vectorizer.pkl
├── model_comparison.csv
└── evaluation/
    ├── classification_report.csv
    ├── confusion_matrix.png
    └── metrics_summary.csv

Topic outputs:

models/topics/
├── topic_vectorizer.pkl
├── nmf_topic_model.pkl
├── topic_keywords.csv
└── article_topics.csv

Analytics outputs:

data/processed/
├── trending_topics.csv
├── similar_news.csv
└── duplicate_news.csv

These generated datasets and model binaries are excluded from GitHub where appropriate using .gitignore.

Screenshots
Dashboard

Add your dashboard screenshot here:

screenshots/dashboard.png
AI News Analyzer

Add your AI analyzer screenshot here:

screenshots/ai-analyzer.png
API Documentation

Add your Swagger screenshot here:

screenshots/api-docs.png

Screenshots can be added to the repository later for a stronger visual presentation.

Key Engineering Decisions
Why TF-IDF?

TF-IDF provides an efficient numerical representation of text and works well for traditional machine learning classification of news articles.

Why Multiple Models?

Multiple models are compared using objective evaluation metrics so that the best-performing model can be selected instead of assuming one algorithm is optimal.

Why PostgreSQL?

PostgreSQL provides reliable structured storage and allows the application to efficiently query articles, topics, sentiment information, and similarity relationships.

Why FastAPI?

FastAPI provides a lightweight, modern REST API framework with automatic Swagger documentation and strong Python integration.

Why Separate Frontend and Backend?

Separating the frontend, API layer, machine learning logic, and database makes the application easier to maintain, test, and extend.

Project Results

The current implementation successfully provides:

News classification
Sentiment analysis
Topic modeling
Trending topic detection
Similar article detection
Duplicate detection
PostgreSQL storage
REST API
Interactive dashboard
Real-time article prediction

The project processes a large-scale news dataset and demonstrates a complete machine learning application lifecycle from raw data to deployed-style application interface.

Future Improvements

Future versions of NewsPulse AI can include:

Live news API ingestion
Real-time news monitoring
Scheduled data ingestion
Automatic model retraining
Named Entity Recognition
AI-powered article summarization
Large Language Model integration
News credibility scoring
Event detection
Semantic search
Vector database integration
Personalized news recommendations
User authentication
Real-time dashboard updates
Docker containerization
Cloud deployment
CI/CD pipeline
Skills Demonstrated

This project demonstrates practical experience in:

Python
Data Science
Machine Learning
Natural Language Processing
Text Classification
Feature Engineering
Topic Modeling
Sentiment Analysis
Similarity Analysis
SQL
PostgreSQL
REST API Development
FastAPI
Frontend Development
Data Visualization
Git
GitHub
Software Project Structure
Author
Aakanksha Pansare

BSc Data Science & Big Data Analysis
MIT World Peace University, Pune

GitHub:

https://github.com/aakankshapansare10

License

This project is developed for educational, portfolio, and demonstration purposes.


### Ab bas ye karo:

```powershell
git add README.md
git commit -m "Improve project documentation"
git push

Phir GitHub refresh karna.

README ka complete professional version ho jayega.

tu hi readme create karke de 

Haan bhai, maine complete professional README.md file khud create kar diya hai. Isme project overview, architecture, features, ML/NLP pipeline, database, API endpoints, installation, running steps, project structure, screenshots section, future improvements, skills, author — sab included hai.

Download the ready-made README.md

Ab tumhe bas apne project ke existing:

NewsPulse_AI/README.md

ko is file se replace karna hai.

Phir:

git add README.md
git commit -m "Improve project documentation"
git push

बस. 

README.md
Document

README.md
NewsPulse AI
AI-Powered News Intelligence & Trend Detection Platform

NewsPulse AI is an end-to-end Machine Learning and Natural Language Processing platform that transforms raw news articles into structured, searchable intelligence.

The platform combines text classification, sentiment analysis, topic modeling, trending-topic detection, similarity analysis, PostgreSQL, FastAPI, and an interactive web dashboard into one complete data science application.

Overview

NewsPulse AI follows a complete data-to-application pipeline:

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
Key Features
News Classification — classifies articles into World, Sports, Business, and Sci-Tech.
Sentiment Analysis — identifies positive, neutral, and negative sentiment with VADER.
Topic Modeling — discovers hidden themes using NMF.
Trending Topics — ranks the most frequent news topics.
Similar News Detection — finds related articles using TF-IDF and cosine similarity.
Duplicate Detection — identifies likely duplicate and highly similar stories.
AI News Analyzer — analyzes a user-provided headline or article instantly.
PostgreSQL Storage — stores articles, topics, sentiment, and similarity relationships.
FastAPI Backend — exposes the intelligence layer through REST endpoints.
Interactive Dashboard — visualizes news statistics, trends, sentiment, and predictions.
Tech Stack
Layer	Technologies
Language	Python, SQL, JavaScript, HTML, CSS
Data Science	Pandas, NumPy
Machine Learning	Scikit-learn
NLP	TF-IDF, VADER, NMF
Similarity	Cosine Similarity
Backend	FastAPI, Uvicorn, Pydantic
Database	PostgreSQL, psycopg2
Frontend	HTML5, CSS3, JavaScript, Chart.js
Development	VS Code, Git, GitHub
Dataset

NewsPulse AI uses the AG News dataset for news classification and NLP experimentation.

Categories
Label	Category
1	World
2	Sports
3	Business
4	Sci-Tech

The raw dataset is intentionally excluded from GitHub using .gitignore.

Machine Learning Pipeline
1. Data Cleaning

The preprocessing pipeline:

loads the raw AG News files
maps category labels
handles missing values
combines title and description
removes HTML artifacts
removes URLs and emails
normalizes text
removes duplicate articles
removes empty records

Generated files:

data/processed/train_cleaned.csv
data/processed/test_cleaned.csv
2. TF-IDF Feature Engineering

The project uses TF-IDF with:

unigrams
bigrams
minimum document frequency filtering
maximum document frequency filtering
sublinear term frequency scaling

The trained vectorizer is reused during inference.

3. Model Comparison

The following classifiers are evaluated:

Logistic Regression
Multinomial Naive Bayes
Linear SVM

Models are compared using:

Accuracy
Precision
Recall
F1 Score

The best-performing model is selected for inference.

NLP Intelligence
Sentiment Analysis

VADER generates:

sentiment label
compound score
positive score
negative score
neutral score
Topic Modeling

NMF is used to discover hidden themes across the news corpus.

The current topic labels include:

Stock Market & Financial Data
Corporate Earnings & Business
Oil & Energy Markets
US General & Political News
War & Middle East Conflict
Sports
Technology & Software
General News & Reports
New York & US Markets
Global Politics & International Affairs
Trending Topics

Topic frequencies are aggregated and ranked to identify the most prominent themes.

Similarity & Duplicate Detection

Cosine similarity is calculated between TF-IDF representations.

Current similarity interpretation:

Score	Classification
>= 0.85	Likely Duplicate
0.70–0.85	Highly Similar
0.60–0.70	Related News
Database Design

PostgreSQL is used for persistent storage.

articles

Stores analyzed news articles.

article_id
title
description
category
sentiment
sentiment_score
topic_id
topic_name
created_at
topics

Stores topic-level analytics.

topic_id
topic_name
article_count
percentage
similar_articles

Stores relationships between similar articles.

similarity_id
article_1_id
article_2_id
similarity_score
similarity_type

Indexes are created for commonly queried fields such as category, sentiment, topic, and similarity score.

FastAPI Endpoints
Method	Endpoint	Purpose
GET	/	API information
GET	/health	API and database health
GET	/articles	Retrieve stored articles
GET	/trending	Retrieve trending topics
GET	/similar/{article_id}	Retrieve similar articles
POST	/predict	Analyze a news article with AI
GET	/stats	Retrieve dashboard statistics
Example AI Request
{
  "text": "Apple announced a major investment in artificial intelligence technology."
}

The /predict endpoint returns category prediction, confidence, sentiment, and sentiment score.

Dashboard

The dashboard is served directly through FastAPI.

Dashboard URL
http://127.0.0.1:8000/dashboard
Main Dashboard Components
Total article count
Number of categories
Number of detected topics
AI system status
Category distribution chart
Sentiment distribution chart
Trending topic cards
News feed
AI News Analyzer
AI News Analyzer

Users can paste any news headline or article and receive:

Predicted Category
Category Confidence
Sentiment
Sentiment Score
Project Structure
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
Installation
1. Clone the repository
git clone https://github.com/aakankshapansare10/NewsPulse_AI.git
cd NewsPulse_AI
2. Create a virtual environment

Windows:

python -m venv .venv

Activate it:

.venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
PostgreSQL Setup

Create a PostgreSQL database named:

newspulse_db

Configure your local PostgreSQL credentials in:

src/api/database.py

Do not commit database passwords or other secrets to GitHub.

Running the Project
Download the dataset
python download_dataset.py
Clean the dataset
python src/preprocessing/clean_data.py
Generate TF-IDF features
python src/nlp/tfidf_features.py
Train the classifier
python src/models/train_classifier.py
Compare models
python src/models/compare_models.py
Evaluate the best model
python src/models/evaluate_model.py
Run topic modeling
python src/nlp/topic_model.py
Generate trending topics
python src/analytics/trending_topics.py
Generate similarity data
python src/analytics/similarity.py
Detect duplicate news
python src/analytics/duplicate_detector.py
Load articles into PostgreSQL
python scripts/load_articles_db.py
Load topics
python scripts/load_topics_db.py
Load similarity data
python scripts/load_similarity_db.py
Enrich articles with sentiment
python scripts/enrich_articles_db.py
Running the API

Start FastAPI:

uvicorn src.api.main:app --reload
API
http://127.0.0.1:8000
Swagger Documentation
http://127.0.0.1:8000/docs
Dashboard
http://127.0.0.1:8000/dashboard
Model Evaluation Artifacts

The project generates evaluation files including:

models/model_comparison.csv
models/evaluation/classification_report.csv
models/evaluation/confusion_matrix.png
models/evaluation/metrics_summary.csv

Topic modeling artifacts:

models/topics/topic_vectorizer.pkl
models/topics/nmf_topic_model.pkl
models/topics/topic_keywords.csv
models/topics/article_topics.csv

Generated analytics include:

data/processed/trending_topics.csv
data/processed/similar_news.csv
data/processed/duplicate_news.csv

Large datasets and trained binary models are excluded from version control where appropriate.

Screenshots

Screenshots can be added to the repository under:

screenshots/
├── dashboard.png
├── ai-analyzer.png
└── api-docs.png

Recommended screenshots:

Main NewsPulse AI dashboard
Trending Topics and charts
AI News Analyzer result
FastAPI Swagger documentation
Engineering Decisions
Why TF-IDF?

TF-IDF provides a fast and interpretable representation for traditional machine learning text classification.

Why compare multiple models?

Model comparison allows the system to select a classifier using measured performance rather than relying on a single algorithm.

Why PostgreSQL?

PostgreSQL provides reliable structured storage and supports efficient querying of articles, topics, sentiment, and similarity relationships.

Why FastAPI?

FastAPI provides a lightweight API layer with automatic OpenAPI/Swagger documentation and strong Python integration.

Why a separate frontend?

Separating the frontend from the ML and database layers keeps the application modular and easier to maintain.

Project Results

The completed system supports:

4-category news classification
sentiment analysis
10-topic NMF topic modeling
trending topic analysis
article similarity analysis
duplicate detection
PostgreSQL persistence
REST API access
interactive dashboard
real-time article prediction through the trained ML pipeline

Actual model metrics are generated automatically and stored under:

models/model_comparison.csv
models/evaluation/

This keeps the README accurate without hard-coding unverified performance numbers.

Future Improvements

Planned improvements include:

Live news API ingestion
Scheduled news collection
Real-time trend monitoring
Named Entity Recognition
AI-powered article summarization
LLM integration
News credibility scoring
Event detection
Semantic search
Vector database integration
Personalized news recommendations
User authentication
Real-time dashboard updates
Docker containerization
Cloud deployment
CI/CD pipeline
Automated model retraining
Skills Demonstrated

This project demonstrates practical experience in:

Python
Data Science
Machine Learning
Natural Language Processing
Text Classification
Feature Engineering
Topic Modeling
Sentiment Analysis
Similarity Analysis
SQL
PostgreSQL
REST API Development
FastAPI
Data Visualization
Frontend Development
Git
GitHub
Software Project Architecture
Author

Aakanksha Pansare

BSc Data Science & Big Data Analysis
MIT World Peace University, Pune

GitHub:
https://github.com/aakankshapansare10

License

This project is developed for educational, portfolio, and demonstration purposes.
import os
import re
import joblib
import numpy as np


# ============================================================
# 1. LOAD MODEL AND TF-IDF VECTORIZER
# ============================================================

MODEL_PATH = "models/best_news_classifier.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"


print("\nLoading NewsPulse AI model...")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

print("Model loaded successfully.")
print("TF-IDF vectorizer loaded successfully.")


# ============================================================
# 2. CATEGORY MAPPING
# ============================================================

CATEGORY_NAMES = {
    1: "World",
    2: "Sports",
    3: "Business",
    4: "Sci-Tech"
}


# ============================================================
# 3. TEXT CLEANING FUNCTION
# ============================================================

def clean_text(text):
    """
    Clean raw news article text before prediction.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Keep only letters and numbers
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text


# ============================================================
# 4. GET CONFIDENCE SCORE
# ============================================================

def get_confidence(model, vectorized_text, predicted_class):
    """
    Calculate confidence score.

    Logistic Regression:
        Uses predict_proba()

    Linear SVM:
        Uses decision_function() and converts scores
        into probability-like confidence values.
    """

    # --------------------------------------------------------
    # Logistic Regression
    # --------------------------------------------------------

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(vectorized_text)[0]

        confidence = np.max(probabilities)

        return confidence * 100


    # --------------------------------------------------------
    # Linear SVM
    # --------------------------------------------------------

    elif hasattr(model, "decision_function"):

        scores = model.decision_function(vectorized_text)

        # Multiclass SVM
        if len(scores.shape) > 1:

            scores = scores[0]

            # Softmax conversion
            exp_scores = np.exp(
                scores - np.max(scores)
            )

            probabilities = (
                exp_scores / np.sum(exp_scores)
            )

            confidence = np.max(probabilities)

            return confidence * 100

        # Binary case
        else:

            score = scores[0]

            confidence = 1 / (
                1 + np.exp(-abs(score))
            )

            return confidence * 100


    return 0.0


# ============================================================
# 5. PREDICTION FUNCTION
# ============================================================

def predict_news(article_text):
    """
    Predict category of a news article.
    """

    # Check empty input
    if not article_text or not article_text.strip():

        return {
            "category": "Unknown",
            "confidence": 0.0
        }


    # Clean text
    cleaned_text = clean_text(article_text)


    # Convert text into TF-IDF features
    vectorized_text = vectorizer.transform(
        [cleaned_text]
    )


    # Predict category
    prediction = model.predict(
        vectorized_text
    )[0]


    # Convert prediction to category name
    category = CATEGORY_NAMES.get(
        int(prediction),
        str(prediction)
    )


    # Calculate confidence
    confidence = get_confidence(
        model,
        vectorized_text,
        prediction
    )


    return {
        "category": category,
        "confidence": round(confidence, 2)
    }


# ============================================================
# 6. INTERACTIVE TERMINAL MODE
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 65)
    print("             NEWSPULSE AI")
    print("        NEWS CATEGORY PREDICTOR")
    print("=" * 65)

    print("\nEnter a news article below.")
    print("Type 'exit' to stop.\n")


    while True:

        article = input(
            "Enter news article: "
        )


        # Exit condition
        if article.lower().strip() == "exit":

            print("\nExiting NewsPulse AI...")
            break


        # Prediction
        result = predict_news(article)


        print("\n" + "-" * 65)
        print("PREDICTION RESULT")
        print("-" * 65)

        print(
            f"Category   : {result['category']}"
        )

        print(
            f"Confidence : {result['confidence']}%"
        )

        print("-" * 65)
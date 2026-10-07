import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# IMPORT OUR EXISTING AI COMPONENTS
# ============================================================

from src.nlp.predict import predict_news
from src.nlp.sentiment import analyze_sentiment


# ============================================================
# UNIFIED NEWS INTELLIGENCE FUNCTION
# ============================================================

def analyze_news(article_text):
    """
    Complete NewsPulse AI analysis.

    Performs:
        1. News category classification
        2. Category confidence estimation
        3. Sentiment analysis

    Returns a combined dictionary.
    """

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    if not article_text or not article_text.strip():

        return {
            "category": "Unknown",
            "category_confidence": 0.0,
            "sentiment": "Neutral",
            "compound": 0.0,
            "positive": 0.0,
            "negative": 0.0,
            "neutral": 0.0
        }


    # --------------------------------------------------------
    # CATEGORY PREDICTION
    # --------------------------------------------------------

    category_result = predict_news(article_text)


    # --------------------------------------------------------
    # SENTIMENT ANALYSIS
    # --------------------------------------------------------

    sentiment_result = analyze_sentiment(article_text)


    # --------------------------------------------------------
    # COMBINE RESULTS
    # --------------------------------------------------------

    result = {
        "category": category_result["category"],
        "category_confidence": category_result["confidence"],

        "sentiment": sentiment_result["sentiment"],
        "compound": sentiment_result["compound"],
        "positive": sentiment_result["positive"],
        "negative": sentiment_result["negative"],
        "neutral": sentiment_result["neutral"]
    }


    return result


# ============================================================
# DISPLAY FUNCTION
# ============================================================

def display_result(result):

    print("\n")
    print("=" * 70)
    print("                  NEWSPULSE AI")
    print("             NEWS INTELLIGENCE RESULT")
    print("=" * 70)

    print("\nNEWS CATEGORY")
    print("-" * 70)

    print(
        f"Category       : {result['category']}"
    )

    print(
        f"Confidence     : {result['category_confidence']}%"
    )


    print("\nSENTIMENT")
    print("-" * 70)

    print(
        f"Sentiment      : {result['sentiment']}"
    )

    print(
        f"Compound Score : {result['compound']}"
    )

    print(
        f"Positive Score : {result['positive']}"
    )

    print(
        f"Negative Score : {result['negative']}"
    )

    print(
        f"Neutral Score  : {result['neutral']}"
    )

    print("\n" + "=" * 70)


# ============================================================
# INTERACTIVE MODE
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 70)
    print("                  NEWSPULSE AI")
    print("        AI-POWERED NEWS INTELLIGENCE")
    print("=" * 70)

    print("\nEnter a news article for complete analysis.")
    print("Type 'exit' to stop.\n")


    while True:

        article = input("Enter news article: ")


        # Exit
        if article.lower().strip() == "exit":

            print("\nExiting NewsPulse AI...")
            break


        # Analyze article
        result = analyze_news(article)


        # Display result
        display_result(result)
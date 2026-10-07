from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# ============================================================
# 1. CREATE SENTIMENT ANALYZER
# ============================================================

analyzer = SentimentIntensityAnalyzer()


# ============================================================
# 2. SENTIMENT ANALYSIS FUNCTION
# ============================================================

def analyze_sentiment(text):
    """
    Analyze the sentiment of a news article.

    Returns:
        Positive / Negative / Neutral
        along with sentiment scores.
    """

    # Handle empty input
    if not text or not text.strip():
        return {
            "sentiment": "Neutral",
            "compound": 0.0,
            "positive": 0.0,
            "negative": 0.0,
            "neutral": 0.0
        }

    # Get VADER sentiment scores
    scores = analyzer.polarity_scores(text)

    compound = scores["compound"]

    # Determine sentiment
    if compound >= 0.05:
        sentiment = "Positive"

    elif compound <= -0.05:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "compound": round(compound, 4),
        "positive": round(scores["pos"], 4),
        "negative": round(scores["neg"], 4),
        "neutral": round(scores["neu"], 4)
    }


# ============================================================
# 3. INTERACTIVE TEST MODE
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 65)
    print("             NEWSPULSE AI")
    print("             SENTIMENT ANALYZER")
    print("=" * 65)

    print("\nEnter a news article.")
    print("Type 'exit' to stop.\n")

    while True:

        text = input("Enter news article: ")

        # Exit
        if text.lower().strip() == "exit":
            print("\nExiting Sentiment Analyzer...")
            break

        # Analyze
        result = analyze_sentiment(text)

        print("\n" + "-" * 65)
        print("SENTIMENT RESULT")
        print("-" * 65)

        print(
            f"Sentiment : {result['sentiment']}"
        )

        print(
            f"Compound  : {result['compound']}"
        )

        print(
            f"Positive  : {result['positive']}"
        )

        print(
            f"Negative  : {result['negative']}"
        )

        print(
            f"Neutral   : {result['neutral']}"
        )

        print("-" * 65)
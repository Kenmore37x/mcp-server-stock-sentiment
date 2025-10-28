from typing import Any
from mcp.server.fastmcp import FastMCP
from transformers import pipeline
import datetime
import requests
import os

# Initialize FastMCP server
mcp = FastMCP("stock_sentiment", dependencies=["requests"])


@mcp.tool()
def get_sentiment(ticker: str) -> dict[str, Any]:
    # Retrieve API key from env variable
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    today = datetime.date.today()
    from_date = today - datetime.timedelta(days=7)

    url = f"https://newsapi.org/v2/everything?q={ticker}&from={from_date}&sortBy=publishedAt&language=en&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])
    headlines = [a["title"] for a in articles]

    if not headlines:
        print(f"No news found for {ticker}.")
    else:
        print(f"Found {len(headlines)} recent headlines about {ticker}.\n")

        # Step 3: Load sentiment analysis model
        sentiment_analyzer = pipeline("sentiment-analysis")

        # Step 4: Analyze each headline
        sentiments = []
        for h in headlines:
            result = sentiment_analyzer(h)[0]
            sentiments.append(result)
            print(f"{h}\n → {result}\n")

    # Step 5: Compute overall sentiment
    positive = sum(1 for s in sentiments if s["label"] == "POSITIVE")
    negative = sum(1 for s in sentiments if s["label"] == "NEGATIVE")
    neutral = len(sentiments) - positive - negative
    total = len(sentiments)

    sentiment_score = (positive - negative) / total

    description = f"Summary for {ticker}: Positive: {positive}, Negative: {negative}, Neutral: {neutral}, Sentiment Score: {sentiment_score:.2f}"

    return {
        "Stock": ticker,
        "Sentiment": sentiment_score,
        "description": description,
    }


if __name__ == "__main__":
    mcp.run()

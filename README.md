# MCP server for Stock Sentiment

This project demonstrates a simple MCP server that returns stock sentiment based on the recent news headlines (last 7 days) about the stock.

## How It Works

* It fetches new headlines from newsapi.org. Alternatively, publicly available headlines can be fetched directly from, for instance, Google News.

* Hugging Face pipeline analyzes the sentiment (positive / negative / neutral).

## Setting Up

This project uses `uv` for package management. Refer [instructions on how to install uv](https://docs.astral.sh/uv/getting-started/installation/) for more details.

```sh
uv venv
```

Activate the virtual environment:

```sh
source .venv/bin/activate
```

Install dependencies:

```sh
uv sync
```

## API Key Setup

Currently, this project uses the news.org API to fetch real headlines. You'll need to:

1. Sign up for a free account at [newsapi.org](https://newsapi.org/).
2. Get your API key from the dashboard.
3. Set the environment variable:

```sh
export NEWS_API_KEY=your_api_key_here
```

## How To Test

To test this MCP server, execute the following command:

```sh
mcp dev src/mcp_stock_sentiment.py
```

Then wait a while for MCP inspector to load. This will give you a UI you can use to test the MCP server right in your browser.

* Click **Connect** button. 
* Under **Tools**, click **List Tools**. When the tools are shown, click _get_sentiment_. 
* Enter a ticker and then click **Run Tool**. 

Sample outputs: 

* AAPL
```commandline
{
  "Stock": "APPL",
  "Sentiment": -0.10256410256410256,
  "description": "Summary for APPL: Positive: 35, Negative: 43, Neutral: 0, Sentiment Score: -0.10"
}
```
* BYND
```commandline
{
Stock:
"BYND"

Sentiment:
-0.6338028169014085

description:
"Summary for BYND: Positive: 13, Negative: 58, Neutral: 0, Sentiment Score: -0.63"

}
```
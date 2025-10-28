# MCP server for Stock Sentiment

This project demonstrates a simple MCP server that returns stock sentiment based on the recent news headlines.

## Setting Up

This project uses `uv` for package management. Go here for [instructions on how to install uv](https://docs.astral.sh/uv/getting-started/installation/).

```sh
uv venv
```

Activate the virtual environment:

```sh
source .venv/bin/activate
```

Install dependencies.

```sh
uv sync
```

## API Key Setup

This project uses the news.org API to fetch real headlines. You'll need to:

1. Sign up for a free account at [NEWSAPI.ORG](https://newsapi.org/)
2. Get your API key from the dashboard
3. Set the environment variable:

```sh
export NEWS_API_KEY=your_api_key_here
```

## How To Run

To test the weather MCP server, execute the following command:

```sh
mcp dev src/mcp_stock_sentiment.py
```

Then wait a while for to load, and click the link to "open inspector with token pre-filled". This will give you a UI you can use to test the MCP server right in your browser.

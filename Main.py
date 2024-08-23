from textblob import TextBlob
import re

# Define keywords for bullish and bearish sentiments
bullish_keywords = ["buy", "bull", "rally", "uptrend", "gain", "long", "increase", "profit"]
bearish_keywords = ["sell", "bear", "drop", "downtrend", "loss", "short", "decrease", "decline"]

# Define a list of stock symbols or names to watch
# For simplicity, we'll use some example stock names.
# This list should be expanded or dynamically loaded from a relevant data source.
stock_symbols = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]

# Placeholder data for stock recommendations (can be replaced with real data and algorithms)
recommendations = {
    "AAPL": {"buy_amount": 100, "sell_amount": 50, "percentage_change": 5},
    "GOOGL": {"buy_amount": 80, "sell_amount": 60, "percentage_change": -3},
    "TSLA": {"buy_amount": 120, "sell_amount": 70, "percentage_change": 2},
    "MSFT": {"buy_amount": 90, "sell_amount": 50, "percentage_change": 4},
    "AMZN": {"buy_amount": 110, "sell_amount": 80, "percentage_change": -1}
}

def analyze_market_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    # Find stock symbols or names in the text
    stocks_in_text = [symbol for symbol in stock_symbols if symbol.lower() in text.lower()]
    
    if not stocks_in_text:
        return "No specific stocks mentioned."
    
    # Check for specific keywords
    text_lower = text.lower()
    bullish_score = sum([text_lower.count(word) for word in bullish_keywords])
    bearish_score = sum([text_lower.count(word) for word in bearish_keywords])
    
    # Determine sentiment for each stock mentioned
    stock_sentiments = {}
    for stock in stocks_in_text:
        if polarity > 0 or bullish_score > bearish_score:
            sentiment = "Bullish Sentiment: Bulls are pushing the stock higher."
            recommendation = recommendations.get(stock, {})
            action = "Buy"
            amount = recommendation.get("buy_amount", "N/A")
            percentage = recommendation.get("percentage_change", "N/A")
        elif polarity < 0 or bearish_score > bullish_score:
            sentiment = "Bearish Sentiment: Bears are pulling the stock down."
            recommendation = recommendations.get(stock, {})
            action = "Sell"
            amount = recommendation.get("sell_amount", "N/A")
            percentage = recommendation.get("percentage_change", "N/A")
        else:
            sentiment = "Neutral Sentiment: Uncertain market direction for this stock."
            action = "Hold"
            amount = "N/A"
            percentage = "N/A"
        
        stock_sentiments[stock] = {
            "Sentiment": sentiment,
            "Action": action,
            "Amount": amount,
            "Percentage Change": percentage
        }
    
    return stock_sentiments

# Example usage
texts = [
    "AAPL is seeing a strong rally as investors buy more shares.",
    "GOOGL is under pressure with many investors selling due to market fears.",
    "TSLA is experiencing mixed signals with some buying while others sell.",
    "MSFT and AMZN are both rising in an uptrend, as bulls dominate the market."
]

for text in texts:
    sentiment = analyze_market_sentiment(text)
    print(f"Text: {text}\nMarket Sentiment: {sentiment}\n")

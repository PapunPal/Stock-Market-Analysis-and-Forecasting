from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import pandas as pd
import requests
from textblob import TextBlob
import os
from flask_cors import CORS


load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://stock-market-analysis-and-forecasti-ten.vercel.app",
    "http://localhost:5500"]
}})

# ----- Helper Functions -----
def normalize_data(values):
    x_min = min(values)
    x_max = max(values)
    normalized = [(x - x_min) / (x_max - x_min) for x in values]
    return normalized, x_min, x_max

def predict_next_value(normalized_values):
    differences = [normalized_values[i] - normalized_values[i - 1] for i in range(1, len(normalized_values))]
    avg_change = sum(differences) / len(differences)
    return normalized_values[-1] + avg_change

def denormalize_value(scaled_value, x_min, x_max):
    return scaled_value * (x_max - x_min) + x_min

def get_stock_news(stock_symbol):
    API_KEY = os.getenv("API_KEY")
    url = f"https://newsapi.org/v2/everything?q={stock_symbol}&sortBy=publishedAt&apiKey={API_KEY}"
    response = requests.get(url)
    news_data = response.json()
    if 'articles' in news_data:
        articles = news_data['articles'][:5]
        return [article['title'] + " " + article.get('description', '') for article in articles]
    return []

def analyze_sentiment(news_articles):
    sentiment_score = 0
    for article in news_articles:
        analysis = TextBlob(article)
        sentiment_score += analysis.sentiment.polarity
    return sentiment_score / len(news_articles) if news_articles else 0

def adjust_prediction(predicted_value, sentiment_score):
    adjustment_factor = 0.01
    return predicted_value * (1 + adjustment_factor * sentiment_score)

# ----- Routes -----
@app.route('/')
def home():
    return jsonify({"message": "Welcome to StockSense API. Use the /predict endpoint to get stock predictions."})

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    stock_symbol = "TATAMOTORS"

    df = pd.read_csv(file)
    if 'close price' not in df.columns:
        return jsonify({"error": "CSV must contain a 'close price' column."})

    df['close price'] = pd.to_numeric(df['close price'], errors='coerce')
    df = df.dropna(subset=['close price'])
    close_prices = df['close price'].tolist()

    normalized_prices, x_min, x_max = normalize_data(close_prices)

    # Predict next 10 normalized values
    future_normalized = []
    for _ in range(10):
        next_value = predict_next_value(normalized_prices + future_normalized)
        future_normalized.append(next_value)

    future_prices = [denormalize_value(v, x_min, x_max) for v in future_normalized]

    # News + Sentiment
    news_articles = get_stock_news(stock_symbol)
    sentiment_score = analyze_sentiment(news_articles)
    adjusted_prices = [adjust_prediction(p, sentiment_score) for p in future_prices]

    return jsonify({
        "predicted_price": round(future_prices[0], 2),
        "sentiment_score": round(sentiment_score, 3),
        "final_predicted_price": round(adjusted_prices[0], 2),
        "adjusted_future_prices": [round(p, 2) for p in adjusted_prices]
    })

if __name__ == '__main__':
    app.run(debug=True)

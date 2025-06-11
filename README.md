# StockSense : Stock Market Analysis and Forecasting

StockSense is a web-based tool that leverages AI and sentiment analysis to predict stock prices. Upload your historical stock data (CSV), and get future price predictions enhanced by real-time news sentiment.

## 🚀 Features

- **Stock Price Prediction:** Upload your CSV file and get instant predictions for the next 10 days.
- **News Sentiment Integration:** The model fetches recent news and analyzes sentiment to adjust predictions.
- **Interactive UI:** Modern, responsive interface with charts and tables for easy analysis.
- **Demo Charts:** Visualize how the prediction works before uploading your own data.

## 🖥️ Live Demo

Open [`Frontend/predict.html`](Frontend/predict.html) directly in your browser, or use the "Open Analysis Tool" button on the homepage (`Frontend/index.html`).

## 📦 Project Structure

```
New folder/
│
├── Backend/
│   ├── app.py            # Flask backend for prediction and sentiment analysis
│   ├── .env              # API keys and environment variables
│   ├── requirements.txt  # Python dependencies
│   └── .gitignore
│
└── Frontend/
    ├── index.html        # Landing page
    ├── predict.html      # Main prediction tool UI
    ├── styles.css        # Main stylesheet
    └── script.js         # Frontend interactivity and charts
```

## 🛠️ Setup & Usage

1. **Install backend dependencies:**
   ```bash
   cd Backend
   pip install -r requirements.txt
   ```

2. **Set up your `.env` file in the `Backend` folder:**
   ```
   API_KEY=your_newsapi_key_here
   ```
   *(Get your API key from [newsapi.org](https://newsapi.org/).)*

3. **Run the Flask backend:**
   ```bash
   python app.py
   ```

4. **Open the frontend:**
   - Open `Frontend/index.html` or `Frontend/predict.html` directly in your browser.
   - The prediction tool will communicate with the backend at `http://127.0.0.1:5000/predict`.

## 📊 How It Works

- **Upload CSV:** The tool expects a CSV with a `close price` column.
- **Prediction:** Uses a simple time-series model to predict the next 10 days.
- **Sentiment Analysis:** Fetches latest news using NewsAPI and analyzes sentiment with TextBlob.
- **Adjustment:** Final predictions are adjusted based on news sentiment.

## 📝 Example CSV Format

```csv
date,open,high,low,close price,volume
2024-06-01,100,110,95,105,10000
2024-06-02,106,112,104,110,12000
...
```

## ⚠️ Notes

- **API Key:** The NewsAPI key is required for fetching news. Get yours at [newsapi.org](https://newsapi.org/).
- **For local use:** The prediction tool fetches from `http://127.0.0.1:5000/predict` by default.

## 📚 Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Chart.js
- **Backend:** Python, Flask, Pandas, TextBlob, requests
- **APIs:** NewsAPI for news sentiment

## 👥 Authors

- Last Benchers (Group 22)

## 📄 License

This project is for educational purposes.

---

*Made with ❤️ by 'Last Benchers'.*
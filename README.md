# 📈 MarketWatch

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**MarketWatch** is a real-time financial analysis dashboard built with Python. It empowers users to track stock market trends, cryptocurrency performance, and historical data through an interactive and responsive user interface.

## 🌟 Key Features

* **Real-Time Data Engine:** Fetches live market data (Stocks, Crypto, Indices) using the `yfinance` API.
* **Interactive Charts:**
    * **Line Charts:** Visualize closing price trends over custom timeframes.
    * **Bar Charts:** Analyze trading volume volatility.
* **Smart Metrics:** Instant dashboard summary showing Current Price, Daily Delta (Change), Volume, and 52-Week Highs.
* **Data Integrity:** Auto-handling of Multi-Index data frames to ensure stability.
* **Raw Data Explorer:** Expandable tabular view for deep-dive analysis of daily records.

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Core Logic** | Python | The backbone of the application. |
| **UI Framework** | Streamlit | Rapid frontend development for data apps. |
| **Data Source** | yfinance | Yahoo Finance API wrapper for market data. |
| **Data Processing** | Pandas | Data manipulation and time-series analysis. |

## 📂 Project Structure

```text
MarketWatch/
│
├── app.py              # The main entry point of the application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Files to exclude from Git (e.g., venv/)

```

##🚀 Getting StartedFollow these instructions to set up the project locally.

###Prerequisites* Python 3.8 or higher installed.
* Git installed.

###Installation1. **Clone the Repository**
```bash
git clone [https://github.com/Dharm3112/MarketWatch.git](https://github.com/Dharm3112/MarketWatch.git)
cd MarketWatch

```


2. **Create a Virtual Environment** (Recommended)
* *Windows:*
```bash
python -m venv venv
venv\Scripts\activate

```


* *macOS/Linux:*
```bash
python3 -m venv venv
source venv/bin/activate

```




3. **Install Dependencies**
```bash
pip install -r requirements.txt

```



###▶️ Running the AppExecute the following command in your terminal:

```bash
streamlit run app.py

```

The application will launch automatically in your default web browser at `http://localhost:8501`.

##🔧 Troubleshooting**Issue: `ModuleNotFoundError**`

* **Fix:** Ensure your virtual environment is activated and you ran `pip install -r requirements.txt`.

**Issue: `KeyError: 'Close'` or Empty Charts**

* **Fix:** This often happens if the `yfinance` library is outdated. Run:
```bash
pip install --upgrade yfinance

```



**Issue: Network Errors**

* **Fix:** Some corporate or school networks block Yahoo Finance. Try switching to a different network or mobile hotspot.

##🤝 ContributingContributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##📄 LicenseThis project is open-source and available under the MIT License.

```

***

### Commit Message

```text
docs: Update README.md with comprehensive project details, badges, and setup guide

```

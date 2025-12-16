import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import date, timedelta

# --- Page Configuration ---
st.set_page_config(
    page_title="MarketWatch",
    page_icon="📈",
    layout="wide"
)

# --- Sidebar: User Inputs ---
st.sidebar.header("🔍 Filter Options")

# Default tickers
ticker_list = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", "BTC-USD", "ETH-USD"]
ticker = st.sidebar.selectbox("Select Ticker", ticker_list)

# Date Range Selection
start_date = st.sidebar.date_input("Start Date", date.today() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", date.today())

# --- Main Page Content ---
st.title(f"📈 {ticker} Market Dashboard")

# 1. Fetch Data
try:
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        st.error("No data found. Please check your inputs.")
    else:
        # 2. Display Key Metrics (Current Price & Delta)
        # Get the latest close price and the one before it to calculate delta
        latest_close = data['Close'].iloc[-1]
        previous_close = data['Close'].iloc[-2]
        delta = latest_close - previous_close

        # Display Metrics in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                label="Current Price (USD)",
                value=f"${latest_close:.2f}",
                delta=f"{delta:.2f}"
            )
        with col2:
            st.metric(
                label="Volume",
                value=f"{int(data['Volume'].iloc[-1]):,}"
            )
        with col3:
            high_52 = data['High'].max()
            st.metric(label="Period High", value=f"${high_52:.2f}")

        # 3. Interactive Charts
        st.markdown("---")
        st.subheader("📊 Price History")

        # Line Chart for Closing Price
        st.line_chart(data['Close'], color="#00aa00")

        # Bar Chart for Volume
        st.subheader("📊 Trading Volume")
        st.bar_chart(data['Volume'])

        # 4. Raw Data View (Optional)
        with st.expander("View Raw Data"):
            st.dataframe(data.sort_index(ascending=False))

except Exception as e:
    st.error(f"An error occurred: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Data provided by Yahoo Finance | Built with Streamlit")
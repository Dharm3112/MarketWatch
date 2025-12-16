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
selected_ticker = st.sidebar.selectbox("Select Ticker", ticker_list)

# Date Range Selection
start_date = st.sidebar.date_input("Start Date", date.today() - timedelta(days=365))
end_date = st.sidebar.date_input("End Date", date.today())

# --- Main Page Content ---
st.title(f"📈 {selected_ticker} Market Dashboard")

# 1. Fetch Data using yf.Ticker (More stable than download for single stocks)
try:
    ticker_obj = yf.Ticker(selected_ticker)
    data = ticker_obj.history(start=start_date, end=end_date)

    # 2. Check if data is empty
    if data.empty:
        st.error(
            f"❌ No data found for {selected_ticker}. Try changing the date range or checking your internet connection.")
    else:
        # 3. Clean Data (Fix for potential timezone issues or MultiIndex)
        # Ensure the index is a datetime object
        data.index = pd.to_datetime(data.index)
        # If columns are MultiIndex (e.g. ('Close', 'AAPL')), flatten them
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        # 4. Display Key Metrics
        # Get latest available close price
        latest_close = data['Close'].iloc[-1]

        # Calculate Delta (handle case where there's only 1 day of data)
        if len(data) > 1:
            previous_close = data['Close'].iloc[-2]
            delta = latest_close - previous_close
        else:
            delta = 0

        # Display Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                label="Current Price",
                value=f"${latest_close:,.2f}",
                delta=f"{delta:,.2f}"
            )
        with col2:
            st.metric(
                label="Volume",
                value=f"{int(data['Volume'].iloc[-1]):,}"
            )
        with col3:
            high_52 = data['High'].max()
            st.metric(label="Period High", value=f"${high_52:,.2f}")

        # 5. Interactive Charts
        st.markdown("---")
        st.subheader("📊 Price History")
        st.line_chart(data['Close'], color="#00aa00")

        st.subheader("📊 Trading Volume")
        st.bar_chart(data['Volume'])

        # 6. Raw Data View
        with st.expander("View Raw Data"):
            st.dataframe(data.sort_index(ascending=False))

except Exception as e:
    st.error(f"An error occurred: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Data provided by Yahoo Finance | Built with Streamlit")
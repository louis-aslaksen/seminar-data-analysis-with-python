import streamlit as st
import yfinance as yf
import random

# Title
st.title("Stock Analytics Dashboard")

# List of stocks for random selection
stock_list = [
    "AAPL", "MSFT", "NVDA", "GOOGL", "AMZN",
    "META", "TSLA", "NOVN.SW", "NESN.SW",
    "ABBN.SW", "UBSG.SW", "ROG.SW"
]

# Initialize ticker
if "ticker" not in st.session_state:
    st.session_state.ticker = "AAPL"

# Random stock selection
if st.button("🎲 Random Stock"):
    st.session_state.ticker = random.choice(stock_list)

# Stock selection
ticker = st.text_input("Enter a stock ticker:", key="ticker")

# Select time period
data_period = st.selectbox(
    "Select time period:",
    ["1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"],
    index=3
)

# Download stock data
stock = yf.Ticker(ticker)
data = stock.history(period=data_period)

# Check if stock data existe
if data.empty:
    st.error("No stock data available. Please check the ticker or try again later.")

# Display chart
else:
    st.subheader("Historical Stock Price")
    st.line_chart(data["Close"])

    #Go to stock detail page
    if st.button("Go to stock detail page"):
        st.session_state.selected_ticker = ticker
        st.session_state.selected_period = data_period
        print("Selected ticker:", st.session_state.selected_ticker)
        st.switch_page("pages/1_Stock_Detail.py")
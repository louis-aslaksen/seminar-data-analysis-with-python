import streamlit as st
import yfinance as yf

#Stock selection
ticker = st.session_state.get("selected_ticker", "AAPL")
data_period = st.session_state.get("selected_period", "1y")

#Download company information
stock = yf.Ticker(ticker)
info = stock.info

#Display company information
st.subheader(info.get("longName", ticker))

st.write("Sector:", info.get("sector", "N/A"))
st.write("Industry:", info.get("industry", "N/A"))
st.write("Market Cap:", info.get("marketCap", "N/A"))
st.write("P/E Ratio:", info.get("trailingPE", "N/A"))
st.write("Dividend Yield:", info.get("dividendYield", "N/A"))
st.write("52-Week High:", info.get("fiftyTwoWeekHigh", "N/A"))
st.write("52-Week Low:", info.get("fiftyTwoWeekLow", "N/A"))

#Historical stock price
st.subheader("Historical Stock Price")

data_period = st.selectbox(
    "Select time period:",
    ["1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"],
    index=3
)

data = stock.history(period=data_period)

if not data.empty:
    st.line_chart(data["Close"])
else:
    st.warning("No historical stock data available.")

if st.button("Back to Stock explorer"):
    st.switch_page("stock_explorer.py")
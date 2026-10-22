import streamlit as st
import yfinance as yf

ticker = st.session_state.get("selected_ticker", "AAPL")

stock = yf.Ticker(ticker)
expiries = stock.options
expiry = st.selectbox("Verfallsdatum", expiries)


if expiries:
    chain = stock.option_chain(expiry)
    st.dataframe(chain.calls)
    st.dataframe(chain.puts)
else:
    st.write("Sorry, no stock options available for this stock")


if st.button("Back to Stock explorer"):
    st.switch_page("stock_explorer.py")

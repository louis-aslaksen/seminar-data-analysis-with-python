import streamlit as st
import yfinance as yf


ticker = st.session_state.get("selected_ticker", "AAPL")

st.title(f"Optionspreise: {ticker}")

stock = yf.Ticker(ticker)
expiries = stock.options

new_cols = {
    "contractSymbol": "Kontraktname",
    "lastTradeDate": "Letzter Trade",
    "lastPrice": "Letzter Preis",
    "strike": "Ausübungspreis",
    "bid": "Geldkurs",
    "ask": "Briefkurs",
    "change": "Veränderung",
    "percentChange": "Prozentuale Veränderung",
    "volume": "Volumen",
    "openInterest": "Offene Kontrakte",
    "impliedVolatility": "Implizite Volatilität",
    "inTheMoney": "Im Geld",
    "contractSize": "Kontraktgrösse",
    "currency": "Währung",
}

if expiries:
    expiry = st.selectbox("Verfallsdatum", expiries)
    chain = stock.option_chain(expiry)
    calls = chain.calls.rename(columns=new_cols)

    puts = chain.puts.rename(columns=new_cols)
    st.subheader("Calls")
    st.dataframe(calls)
    st.subheader("Puts")
    st.dataframe(puts)
else:
    st.write("Sorry, no stock options available for this stock")


if st.button("Back to Stock explorer"):
    st.switch_page("stock_explorer.py")

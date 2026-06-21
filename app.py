import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("📈 Stock Price Prediction App")

ticker = st.text_input("Enter Stock Symbol", "AAPL")

data = yf.download(
    ticker,
    start="2020-01-01",
    end="2025-01-01"
)

st.subheader("Historical Stock Prices")

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(data['Close'])

ax.set_title(f"{ticker} Closing Price")
ax.set_xlabel("Date")
ax.set_ylabel("Price")

st.pyplot(fig)

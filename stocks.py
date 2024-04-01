import streamlit as st
import yfinance as yf
import datetime

st.title("Welcome to Mariya's Stock Wizard")

ticker_symbol = st.text_input("Enter the ticker symbol of the stock", "AAPL")
ticker_data = yf.Ticker(ticker_symbol)

dt1, dt2 = st.columns(2)
with dt1:
    start_date = st.date_input("Start Date", datetime.date(2023, 1, 1))
with dt2:
    end_date = st.date_input("End Date", datetime.date(2023, 12, 31))

ticker_df = ticker_data.history(period='1m', start=start_date, end=end_date)

st.header("Stock Price of {0}".format(ticker_symbol))
st.dataframe(ticker_df, use_container_width=True)
# st.write(ticker_df)

col1, col2 = st.columns(2)
with col1:
    st.write("### Daily Close Price Chart")
    st.line_chart(ticker_df, y='Close')
with col2:
    st.write("### Daily Volume Chart")
    st.line_chart(ticker_df, y='Volume')
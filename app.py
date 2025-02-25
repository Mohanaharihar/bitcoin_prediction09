import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Load Data
df = pd.read_csv('bitcoin.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

# Streamlit App
st.title('Bitcoin Investment Dashboard')
st.sidebar.header('Investment Strategy')

# Feature Engineering
df['open-close'] = df['Open'] - df['Close']
df['low-high'] = df['Low'] - df['High']
df['daily_return'] = df['Close'].pct_change()
df['volatility'] = df['daily_return'].rolling(window=7).std()
df['moving_avg_50'] = df['Close'].rolling(window=50).mean()
df['moving_avg_200'] = df['Close'].rolling(window=200).mean()
df.dropna(inplace=True)

# Buy/Sell Signals
df['signal'] = np.where(df['Close'] > df['moving_avg_50'], 'Buy', 'Sell')

# Display Data
st.subheader('Bitcoin Price Data')
st.dataframe(df.tail())

# Plot Price Trends
fig = px.line(df, x='Date', y=['Close', 'moving_avg_50', 'moving_avg_200'], title='Bitcoin Price with Moving Averages')
st.plotly_chart(fig)

# Signal Plot
fig_signal = px.scatter(df, x='Date', y='Close', color='signal', title='Buy/Sell Signals')
st.plotly_chart(fig_signal)

# Volatility Indicator
fig_volatility = px.line(df, x='Date', y='volatility', title='Bitcoin Volatility Over Time')
st.plotly_chart(fig_volatility)

# Investment Advice
def get_advice():
    latest_signal = df.iloc[-1]['signal']
    if latest_signal == 'Buy':
        return 'It might be a good time to invest! 📈'
    else:
        return 'Consider holding or selling. 📉'

st.sidebar.subheader('Investment Advice')
st.sidebar.write(get_advice())

# Final Notes
st.sidebar.markdown('---')
st.sidebar.text('Built with ❤️ by AI')

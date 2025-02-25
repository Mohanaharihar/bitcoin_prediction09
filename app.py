import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv("bitcoin.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Add indicators
df['Daily Change'] = df['Close'] - df['Open']
df['Rolling Mean'] = df['Close'].rolling(window=7).mean()

# Function to determine the best time to invest
def best_investment_time(df):
    min_price = df['Close'].min()
    max_price = df['Close'].max()
    best_buy = df[df['Close'] == min_price]['Date'].values[0]
    best_sell = df[df['Close'] == max_price]['Date'].values[0]
    return best_buy, best_sell

best_buy, best_sell = best_investment_time(df)

# Streamlit UI
st.title("📈 Bitcoin Investment Dashboard")
st.write("This dashboard provides insights into Bitcoin price movements and investment opportunities.")

# Price Chart
fig = px.line(df, x="Date", y="Close", title="Bitcoin Closing Prices Over Time")
st.plotly_chart(fig)

# Investment Insights
st.subheader("💰 Best Investment Timing")
st.write(f"👉 Best time to **BUY**: {best_buy}")
st.write(f"👉 Best time to **SELL**: {best_sell}")

# Additional Indicators
st.subheader("📊 Daily Price Changes")
fig2 = px.line(df, x="Date", y="Daily Change", title="Daily Price Change")
st.plotly_chart(fig2)

st.subheader("📉 7-Day Moving Average")
fig3 = px.line(df, x="Date", y="Rolling Mean", title="7-Day Rolling Average")
st.plotly_chart(fig3)

st.write("### 📢 Conclusion")
st.write("Monitor Bitcoin trends, and make informed investment decisions based on historical data.")

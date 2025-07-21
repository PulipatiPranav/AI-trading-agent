

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker="AAPL", start="2020-01-01", end="2023-12-31"):
    print(f"Fetching data for {ticker} from {start} to {end}...")
    data = yf.download(ticker, start=start, end=end)
    print("Data fetched successfully!\n")
    print(data.head())  # Display first 5 rows
    return data

def plot_closing_price(data, ticker="AAPL"):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label=f'{ticker} Closing Price', color='blue')
    plt.title(f'{ticker} Stock Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Price in USD')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ticker = "AAPL"
    stock_data = fetch_stock_data(ticker)
    plot_closing_price(stock_data, ticker)

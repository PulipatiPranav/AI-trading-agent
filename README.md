# AI-trading-agent

## Milestone 1: Fetching & Visualizing Stock Data

In this milestone, we used the `yfinance` library to fetch historical stock data for Apple (AAPL) from Yahoo Finance.

### Features
- Fetches daily OHLCV data (Open, High, Low, Close, Volume)
- Plots the closing price from 2020–2023
- Easy to change ticker and date range
  
## Milestone 2: Understanding Reinforcement Learning (RL)

In this milestone, I explored the core concept that powers my trading agent: **Reinforcement Learning (RL)**.

### Key Concepts
 **Agent**       - The AI model (our trading bot) that makes decisions 
 **Environment** - A simulated stock market where the agent can interact and learn 
 **State**       - A snapshot of the current market: stock price, balance, shares held, etc. 
 **Action**      - What the agent chooses to do: Buy, Sell, or Hold 
 **Reward**      - Feedback given to the agent (profit = positive reward, loss = negative reward)

### The RL Loop
1. Agent observes the current **state**.
2. Agent takes an **action** (Buy/Sell/Hold).
3. The **environment** updates the state and gives a **reward**.
4. Agent **learns** from this and improves over time.

This cycle continues across many episodes, helping the agent learn optimal strategies through trial and error — just like a human learning from experience.

## 🏗️ Milestone 3: Trading Environment

We built a custom **Gym environment** that simulates a stock market and allows our agent to:
- Buy (0), Sell (1), or Hold (2) stock
- Track its account balance, shares held, and net worth
- Receive a reward based on portfolio growth (profit)

### 🔍 State Space
The observation returned to the agent includes:
- Current balance
- Current stock price
- Number of shares held

### ✅ Features
- Handles basic trading logic and transaction simulation
- Tracks net worth over time
- Can be used directly with `stable-baselines3` RL models



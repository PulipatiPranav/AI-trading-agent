import gym
from gym import spaces
import numpy as np
import pandas as pd

class TradingEnv(gym.Env):
    """A custom stock trading environment for RL agents."""
    
    metadata = {'render.modes': ['human']}

    def __init__(self, df, initial_balance=10000):
        super(TradingEnv, self).__init__()

        self.df = df.reset_index()
        self.initial_balance = initial_balance

        
        self.action_space = spaces.Discrete(3)

        
        self.observation_space = spaces.Box(
            low=0, high=np.inf, shape=(3,), dtype=np.float32)

        self.reset()

    def reset(self):
        self.current_step = 0
        self.balance = self.initial_balance
        self.shares_held = 0
        self.net_worth = self.initial_balance
        self.trades = []

        return self._next_observation()

    def _next_observation(self):
        current_price = float(self.df.loc[self.current_step, "Close"])
        obs = np.array([self.balance, current_price, self.shares_held], dtype=np.float32)
        return obs

    def step(self, action):
        current_price = float(self.df.loc[self.current_step, "Close"])

        if action == 0:  # Buy
            if self.balance >= current_price:
                self.shares_held += 1
                self.balance -= current_price
                self.trades.append(("buy", self.current_step))

        elif action == 1:  # Sell
            if self.shares_held > 0:
                self.shares_held -= 1
                self.balance += current_price
                self.trades.append(("sell", self.current_step))

        

        self.current_step += 1
        done = self.current_step >= len(self.df) - 1

        self.net_worth = self.balance + self.shares_held * current_price
        reward = self.net_worth - self.initial_balance

        obs = self._next_observation()
        return obs, reward, done, {}

    def render(self, mode='human'):
        profit = self.net_worth - self.initial_balance
        print(f'Step: {self.current_step}')
        print(f'Balance: ₹{self.balance:.2f}')
        print(f'Shares held: {self.shares_held}')
        print(f'Net worth: ₹{self.net_worth:.2f}')
        print(f'Profit: ₹{profit:.2f}\n')

if __name__ == "__main__":
    import yfinance as yf
    df = yf.download('AAPL', start='2020-01-01', end='2020-12-31')
    df = df.dropna().reset_index()

    
    env = TradingEnv(df)
    obs = env.reset()
    
    for _ in range(10):
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        env.render()
        if done:
            break

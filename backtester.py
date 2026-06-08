import pandas as pd
import numpy as np


class Backtester:

    def __init__(
            self,
            prices_df,
            weights,
            initial_capital=10000):

        self.prices_df = prices_df.copy()

        self.weights = weights

        self.initial_capital = (
            initial_capital
        )

    def run(self):

        data = self.prices_df.copy()

        assets = [
            col
            for col in data.columns
            if col != 'Date'
        ]

        normalized = (
            data[assets]
            / data[assets].iloc[0]
        )

        portfolio = (
            normalized
            * self.weights
        ).sum(axis=1)

        portfolio_value = (
            portfolio
            * self.initial_capital
        )

        result = pd.DataFrame(
            {
                'Date': data['Date'],
                'Portfolio':
                portfolio_value
            }
        )

        return result

    def total_return(
            self,
            portfolio_df):

        start_value = (
            portfolio_df[
                'Portfolio'
            ].iloc[0]
        )

        end_value = (
            portfolio_df[
                'Portfolio'
            ].iloc[-1]
        )

        return (
            end_value
            /
            start_value
            - 1
        ) * 100

    def max_drawdown(
            self,
            portfolio_df):

        portfolio = (
            portfolio_df[
                'Portfolio'
            ]
        )

        rolling_max = (
            portfolio.cummax()
        )

        drawdown = (
            portfolio
            -
            rolling_max
        ) / rolling_max

        return (
            drawdown.min()
            * 100
        )
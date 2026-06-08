import pandas as pd
from data_loader import DataLoader


class DataProcessor:

    def __init__(self):

        self.loader = DataLoader()

    # Підготовка доходностей
    def prepare_returns(self):

        assets = {
            'AAPL': 'data/AAPL.csv',
            'MSFT': 'data/MSFT.csv',
            'NVDA': 'data/NVDA.csv',
            'AMZN': 'data/AMZN.csv',
            'GOOGL': 'data/GOOGL.csv'
        }

        returns_df = pd.DataFrame()

        for ticker, path in assets.items():

            df = self.loader.load_asset(path)

            df = df[
                (df['Date'] >= '2017-01-01')
                &
                (df['Date'] <= '2022-12-31')
            ]

            df[ticker] = (
                df['Close']
                .pct_change()
            )

            df = df[
                ['Date', ticker]
            ]

            if returns_df.empty:

                returns_df = df

            else:

                returns_df = returns_df.merge(
                    df,
                    on='Date',
                    how='inner'
                )

        returns_df = (
            returns_df
            .dropna()
        )

        return returns_df

    # Підготовка цін для графіків
    def prepare_prices(self):

        assets = {
            'AAPL': 'data/AAPL.csv',
            'MSFT': 'data/MSFT.csv',
            'NVDA': 'data/NVDA.csv',
            'AMZN': 'data/AMZN.csv',
            'GOOGL': 'data/GOOGL.csv'
        }

        prices_df = pd.DataFrame()

        for ticker, path in assets.items():

            df = self.loader.load_asset(path)

            df = df[
                (df['Date'] >= '2017-01-01')
                &
                (df['Date'] <= '2022-12-31')
            ]

            df = df[
                ['Date', 'Close']
            ]

            df.rename(
                columns={
                    'Close': ticker
                },
                inplace=True
            )

            if prices_df.empty:

                prices_df = df

            else:

                prices_df = prices_df.merge(
                    df,
                    on='Date',
                    how='inner'
                )

        return prices_df
import pandas as pd


class DataLoader:

    def load_asset(
            self,
            path):

        df = pd.read_csv(path)

        df['Date'] = pd.to_datetime(
            df['Date']
        )

        return df
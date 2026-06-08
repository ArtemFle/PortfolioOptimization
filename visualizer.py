import matplotlib.pyplot as plt


class Visualizer:

    # Графік цін
    def prices_chart(
            self,
            prices_df):

        plt.figure(
            figsize=(12, 6)
        )

        for column in prices_df.columns[1:]:

            plt.plot(
                prices_df['Date'],
                prices_df[column],
                label=column
            )

        plt.title(
            'Динаміка цін активів'
        )

        plt.xlabel(
            'Дата'
        )

        plt.ylabel(
            'Ціна закриття'
        )

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        plt.show()

    # Нормований графік
    def normalized_prices_chart(
            self,
            prices_df):

        plt.figure(
            figsize=(12, 6)
        )

        normalized_df = prices_df.copy()

        for column in normalized_df.columns[1:]:

            normalized_df[column] = (
                normalized_df[column]
                /
                normalized_df[column].iloc[0]
                * 100
            )

        for column in normalized_df.columns[1:]:

            plt.plot(
                normalized_df['Date'],
                normalized_df[column],
                label=column
            )

        plt.title(
            'Нормована динаміка активів (2017 = 100%)'
        )

        plt.xlabel(
            'Дата'
        )

        plt.ylabel(
            'Відносна зміна, %'
        )

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        plt.show()

    # Кореляційна матриця
    def correlation_matrix(
            self,
            corr_matrix):

        plt.figure(
            figsize=(8, 6)
        )

        plt.imshow(
            corr_matrix,
            aspect='auto'
        )

        plt.colorbar()

        plt.xticks(
            range(len(corr_matrix.columns)),
            corr_matrix.columns,
            rotation=45
        )

        plt.yticks(
            range(len(corr_matrix.columns)),
            corr_matrix.columns
        )

        plt.title(
            'Кореляційна матриця'
        )

        plt.tight_layout()

        plt.show()

    # Ризик-дохідність
    def risk_return_chart(
            self,
            results_df):

        plt.figure(
            figsize=(10, 6)
        )

        plt.plot(
            results_df['Risk'],
            results_df['Return'],
            marker='o'
        )

        for i in range(
                len(results_df)):

            plt.annotate(
                f"{results_df['wD'][i]:.1f}",
                (
                    results_df['Risk'][i],
                    results_df['Return'][i]
                )
            )

        plt.xlabel(
            'Ризик'
        )

        plt.ylabel(
            'Доходність'
        )

        plt.title(
            'Залежність ризику від доходності'
        )

        plt.grid(True)

        plt.tight_layout()

        plt.show()

    # Бектестинг портфеля
    def portfolio_chart(
            self,
            portfolio_df):

        plt.figure(
            figsize=(12, 6)
        )

        plt.plot(
            portfolio_df['Date'],
            portfolio_df['Portfolio']
        )

        plt.title(
            'Portfolio Backtest'
        )

        plt.xlabel(
            'Date'
        )

        plt.ylabel(
            'Capital, USD'
        )

        plt.grid(True)

        plt.tight_layout()

        plt.show()

    # Порівняння двох стратегій
    def comparison_chart(
            self,
            markowitz_df,
            equal_df):

        plt.figure(
            figsize=(12, 6)
        )

        plt.plot(
            markowitz_df['Date'],
            markowitz_df['Portfolio'],
            label='Markowitz'
        )

        plt.plot(
            equal_df['Date'],
            equal_df['Portfolio'],
            label='Equal Weight'
        )

        plt.title(
            'Порівняння інвестиційних стратегій'
        )

        plt.xlabel(
            'Дата'
        )

        plt.ylabel(
            'Капітал, USD'
        )

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        plt.show()
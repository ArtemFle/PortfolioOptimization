from processor import DataProcessor
from optimizer import PortfolioOptimizer
from visualizer import Visualizer
from backtester import Backtester

import pandas as pd


def main():

    processor = DataProcessor()

    returns = processor.prepare_returns()

    optimizer = PortfolioOptimizer(
        returns
    )

    print("\nСередні доходності")
    print(
        optimizer.mean_returns()
    )

    print("\nРизики")
    print(
        optimizer.volatility()
    )

    results = []

    scenarios = [
        (0.1, 0.9),
        (0.2, 0.8),
        (0.3, 0.7),
        (0.4, 0.6),
        (0.5, 0.5),
        (0.6, 0.4),
        (0.7, 0.3),
        (0.8, 0.2),
        (0.9, 0.1)
    ]

    for wD, wE in scenarios:

        weights = optimizer.optimize(
            wD,
            wE
        )

        portfolio_return = (
            optimizer.portfolio_return(
                weights
            )
        )

        portfolio_risk = (
            optimizer.portfolio_risk(
                weights
            )
        )

        results.append(
            {
                'wD': wD,
                'wE': wE,
                'Return': portfolio_return,
                'Risk': portfolio_risk
            }
        )

        print("\n" + "=" * 50)

        print(
            f"wD = {wD:.1f}, "
            f"wE = {wE:.1f}"
        )

        print(
            f"Доходність: "
            f"{portfolio_return:.6f}"
        )

        print(
            f"Ризик: "
            f"{portfolio_risk:.6f}"
        )

        print("\nВаги активів:")

        for asset, weight in zip(
                optimizer.returns_df.columns,
                weights):

            print(
                f"{asset}: "
                f"{weight:.4f}"
            )

    results_df = pd.DataFrame(
        results
    )

    visualizer = Visualizer()

    prices = (
        processor.prepare_prices()
    )

    # Рисунок 4.1
    visualizer.prices_chart(
        prices
    )

    # Рисунок 4.2
    visualizer.normalized_prices_chart(
        prices
    )

    # Рисунок 4.3
    corr_matrix = (
        optimizer.returns_df
        .corr()
    )

    visualizer.correlation_matrix(
        corr_matrix
    )

    # Рисунок 4.4
    visualizer.risk_return_chart(
        results_df
    )

    # Рисунок 4.5
    best_weights = optimizer.optimize(
        0.9,
        0.1
    )

    backtester = Backtester(
        prices,
        best_weights
    )

    portfolio_df = (
        backtester.run()
    )

    visualizer.portfolio_chart(
        portfolio_df
    )

    print("\n" + "=" * 50)
    print("БЕКТЕСТИНГ")

    print(
        f"Початковий капітал: "
        f"10000 USD"
    )

    print(
        f"Кінцевий капітал: "
        f"{portfolio_df['Portfolio'].iloc[-1]:.2f} USD"
    )

    print(
        f"Загальна доходність: "
        f"{backtester.total_return(portfolio_df):.2f}%"
    )

    print(
        f"Максимальна просадка: "
        f"{backtester.max_drawdown(portfolio_df):.2f}%"
    )

    # ------------------------------------------------
    # 4.4 Порівняння з наївною диверсифікацією
    # ------------------------------------------------

    equal_weights = [
        0.2,
        0.2,
        0.2,
        0.2,
        0.2
    ]

    equal_backtester = Backtester(
        prices,
        equal_weights
    )

    equal_portfolio = (
        equal_backtester.run()
    )

    visualizer.comparison_chart(
        portfolio_df,
        equal_portfolio
    )

    print("\n" + "=" * 50)
    print("НАЇВНИЙ ПОРТФЕЛЬ")

    print(
        f"Кінцевий капітал: "
        f"{equal_portfolio['Portfolio'].iloc[-1]:.2f} USD"
    )

    print(
        f"Доходність: "
        f"{equal_backtester.total_return(equal_portfolio):.2f}%"
    )

    print(
        f"Максимальна просадка: "
        f"{equal_backtester.max_drawdown(equal_portfolio):.2f}%"
    )


if __name__ == "__main__":
    main()
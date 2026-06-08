import numpy as np
from scipy.optimize import minimize


class PortfolioOptimizer:

    def __init__(self, returns_df):

        self.returns_df = returns_df.drop(
            columns=['Date']
        )

    # Середні доходності активів
    def mean_returns(self):
        return self.returns_df.mean()

    # Матриця коваріацій
    def covariance_matrix(self):
        return self.returns_df.cov()

    # Ризики активів
    def volatility(self):
        return self.returns_df.std()

    # Доходність портфеля
    def portfolio_return(
            self,
            weights):

        mean_returns = (
            self.mean_returns()
            .values
        )

        return np.dot(
            mean_returns,
            weights
        )

    # Ризик портфеля
    def portfolio_risk(
            self,
            weights):

        cov_matrix = (
            self.covariance_matrix()
            .values
        )

        variance = np.dot(
            weights.T,
            np.dot(
                cov_matrix,
                weights
            )
        )

        return np.sqrt(
            variance
        )

    # Цільова функція
    def objective_function(
            self,
            weights,
            wD,
            wE):

        risk = self.portfolio_risk(
            weights
        )

        expected_return = (
            self.portfolio_return(
                weights
            )
        )

        # Масштабування доходності
        return (
            wD * risk
            -
            wE * expected_return * 100
        )

    # Пошук оптимальних ваг
    def optimize(
            self,
            wD,
            wE):

        n_assets = len(
            self.returns_df.columns
        )

        initial_weights = (
            np.ones(n_assets)
            / n_assets
        )

        constraints = (
            {
                'type': 'eq',
                'fun': lambda w:
                np.sum(w) - 1
            },
        )

        bounds = tuple(
            (0, 0.4)
            for _ in range(n_assets)
        )

        result = minimize(
            self.objective_function,
            initial_weights,
            args=(wD, wE),
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )

        return result.x
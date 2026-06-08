# PortfolioOptimization
Investment portfolio optimization based on the Markowitz model using Python.

# Markowitz Portfolio Optimization

## Overview

This project was developed as part of a Bachelor's Qualification Thesis in Applied Mathematics.

The software system implements mathematical modeling and optimization of an investment portfolio based on the Markowitz portfolio theory. The application performs financial data processing, statistical analysis of assets, portfolio optimization, visualization of results, and portfolio backtesting.

## Features

* Historical stock data processing
* Calculation of asset returns
* Calculation of expected returns and risks
* Covariance and correlation matrix analysis
* Portfolio optimization using the Markowitz model
* Diversification constraints
* Risk-return analysis
* Portfolio backtesting
* Data visualization

## Technologies

* Python 3
* NumPy
* Pandas
* SciPy
* Matplotlib

## Project Structure

```text
PortfolioOptimization/
│
├── data/
├── main.py
├── data_loader.py
├── processor.py
├── optimizer.py
├── visualizer.py
├── backtester.py
├── requirements.txt
└── README.md
```

## Dataset

The experimental study uses historical stock market data of:

* Apple Inc. (AAPL)
* Microsoft Corporation (MSFT)
* NVIDIA Corporation (NVDA)
* Amazon.com Inc. (AMZN)
* Alphabet Inc. (GOOGL)

The analyzed period covers 2017–2022.

## Optimization Model

The portfolio expected return is calculated as:

E(X) = Σ μᵢxᵢ

The portfolio risk is calculated using the covariance matrix:

σₚ = √(XᵀΣX)

The optimization objective combines return maximization and risk minimization.

Additionally, diversification constraints are applied:

0 ≤ xᵢ ≤ 0.4

Σxᵢ = 1

## Results

The developed system allows:

* construction of diversified portfolios;
* risk-return analysis;
* visualization of financial data;
* historical portfolio performance evaluation.

## Author

Artem Fleisher

Bachelor's Qualification Thesis

Specialty 113 Applied Mathematics

Oles Honchar Dnipro National University

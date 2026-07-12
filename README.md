# Brent Oil Price Analysis Workflow

## Objective

The objective of this project is to identify structural changes in Brent crude oil prices and investigate whether these changes correspond to major geopolitical or economic events.

## Data Collection

* Load the Brent crude oil price dataset from a CSV file.
* Verify successful import by displaying the first and last records.
* Check the dataset dimensions and data types.

## Data Preparation

* Convert the Date column to datetime format.
* Sort the dataset chronologically.
* Handle missing values and duplicate observations if present.
* Set the Date column as the index for time-series analysis.

## Exploratory Data Analysis (EDA)

* Plot historical Brent oil prices.
* Calculate descriptive statistics.
* Compute log returns.
* Visualize log returns to identify volatility clustering.

## Bayesian Change Point Analysis

* Define a Bayesian model using PyMC.
* Estimate the change point (τ).
* Estimate the mean price before and after the change point.
* Perform MCMC sampling to obtain posterior distributions.

## Model Evaluation

* Assess convergence using R-hat statistics and trace plots.
* Examine posterior distributions of the change point and model parameters.
* Estimate the date corresponding to the detected structural break.

## Event Correlation

* Compare the detected change point with major historical events affecting global oil markets.
* Evaluate whether the detected structural break coincides with geopolitical or economic shocks.

## Result Interpretation

* Quantify changes in average oil prices before and after the detected change point.
* Discuss possible economic explanations for the observed structural change.

## Dashboard Development

* Expose analysis results through Flask APIs.
* Develop an interactive React dashboard to visualize prices, detected change points, and historical events.

"""
Visualization functions for Brent Oil Price Analysis.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import arviz as az


def plot_price_series(df):
    """
    Plot historical Brent oil prices.
    """

    plt.figure(figsize=(15, 6))

    plt.plot(df["Date"], df["Price"], color="steelblue")

    plt.title("Historical Brent Oil Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD per Barrel)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def plot_log_returns(df):
    """
    Plot daily log returns.
    """

    log_returns = np.log(df["Price"]).diff()

    plt.figure(figsize=(15, 6))

    plt.plot(df["Date"], log_returns, color="darkorange")

    plt.title("Daily Log Returns")
    plt.xlabel("Date")
    plt.ylabel("Log Return")

    plt.axhline(0, color="black", linestyle="--")

    plt.grid(True)

    plt.tight_layout()
    plt.show()


def plot_price_distribution(df):
    """
    Plot price distribution.
    """

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Price"],
        bins=40,
        edgecolor="black"
    )

    plt.title("Distribution of Brent Oil Prices")
    plt.xlabel("Price")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


def plot_rolling_statistics(df, window=30):
    """
    Plot rolling mean and rolling standard deviation.
    """

    rolling_mean = df["Price"].rolling(window).mean()
    rolling_std = df["Price"].rolling(window).std()

    plt.figure(figsize=(15, 6))

    plt.plot(df["Date"], df["Price"], label="Price", alpha=0.5)

    plt.plot(df["Date"], rolling_mean,
             label=f"{window}-Day Rolling Mean")

    plt.plot(df["Date"], rolling_std,
             label=f"{window}-Day Rolling Std")

    plt.legend()

    plt.title("Rolling Statistics")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def plot_trace(trace):
    """
    Plot MCMC trace plots.
    """

    az.plot_trace(
        trace,
        var_names=["tau", "mu1", "mu2", "sigma"]
    )

    plt.tight_layout()

    plt.show()


def plot_tau_posterior(trace):
    """
    Plot posterior distribution of the change point.
    """

    tau_samples = trace.posterior["tau"].values.flatten()

    plt.figure(figsize=(10, 5))

    plt.hist(
        tau_samples,
        bins=50,
        edgecolor="black"
    )

    plt.title("Posterior Distribution of Tau")
    plt.xlabel("Change Point Index")
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.show()


def plot_mu_posterior(trace):
    """
    Plot posterior distributions of μ1 and μ2.
    """

    mu1 = trace.posterior["mu1"].values.flatten()
    mu2 = trace.posterior["mu2"].values.flatten()

    plt.figure(figsize=(10, 5))

    plt.hist(
        mu1,
        bins=40,
        alpha=0.6,
        label="Before Change"
    )

    plt.hist(
        mu2,
        bins=40,
        alpha=0.6,
        label="After Change"
    )

    plt.legend()

    plt.title("Posterior Means")

    plt.tight_layout()

    plt.show()


def plot_change_point(df, trace):
    """
    Plot estimated Bayesian change point.
    """

    tau = int(trace.posterior["tau"].mean())

    change_date = df.iloc[tau]["Date"]

    plt.figure(figsize=(15, 6))

    plt.plot(
        df["Date"],
        df["Price"],
        label="Price"
    )

    plt.axvline(
        change_date,
        color="red",
        linestyle="--",
        linewidth=3,
        label="Estimated Change Point"
    )

    plt.scatter(
        change_date,
        df.iloc[tau]["Price"],
        color="red"
    )

    plt.legend()

    plt.title("Estimated Bayesian Change Point")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def plot_before_after(df, trace):
    """
    Compare average price before and after change point.
    """

    tau = int(trace.posterior["tau"].mean())

    before = df.iloc[:tau]["Price"].mean()
    after = df.iloc[tau:]["Price"].mean()

    plt.figure(figsize=(6, 5))

    plt.bar(
        ["Before", "After"],
        [before, after]
    )

    plt.ylabel("Average Price")

    plt.title("Average Price Before and After Change Point")

    plt.tight_layout()

    plt.show()
import matplotlib.pyplot as plt

def plot_prices(df):

    plt.figure(figsize=(14,6))

    plt.plot(df["Date"], df["Price"])

    plt.title("Brent Oil Prices")

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.grid(True)

    plt.show()
import pandas as pd

def load_data(path):
    df = pd.read_csv(r"C:\Users\Soret\Downloads\BrentOilPrices.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    df.sort_values("Date", inplace=True)

    return df
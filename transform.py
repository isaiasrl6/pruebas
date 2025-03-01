import pandas as pd
from extract import extract_data

def transform_data(df):
    df["avg_price"] = (df["Open"] + df["Close"]) / 2
    return df[["avg_price", "Volume"]]

if __name__ == "__main__":
    df = extract_data("JPM")
    df_transformed = transform_data(df)
    print(df_transformed.head())

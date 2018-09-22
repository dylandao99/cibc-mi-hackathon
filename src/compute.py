import pandas as pd


def averagePrice(df):
    # Extract prices column
    priceCol = df.iloc[:, 7]
    # Calculate mean and return it
    return priceCol.mean()

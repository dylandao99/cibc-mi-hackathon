import pandas as pd


def averageProcedurePrice(df):
    # Extract procedure code and prices column
    extractedMatrix = df.iloc[:, 6:]
    # Calculate mean price of each procedure and return it
    return extractedMatrix.groupby([6]).mean()


def averageStatePrice(df):
    # Extract state code, prices column
    extractedMatrix = df.iloc[:, [4, 7]]
    # Calculate mean price for each state and return it
    return extractedMatrix.groupby([4]).mean()

from src import filesys, compute, plot
from random import randint
import pandas as pd

# Directory where data is located
# dataDirectory = "./sample.csv"
dataDirectory = "../claims_final.csv"

# Initialize the files class
data = filesys.files(dataDirectory)
df = data.getData()
print (df)
averageProcedurePrice = compute.averageProcedurePrice(df)
averageStatePrice = compute.averageStatePrice(df)

zScores = compute.zScoreByCategory(df, 2)
zS = compute.zScoreByCategory(df, 4)
# plot.plotTest(zScores, zS, 'Provider ID', 'State')

data.genOutput1('output1.csv')

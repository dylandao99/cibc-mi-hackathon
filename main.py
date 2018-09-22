from src import filesys, compute, plot

# Directory where data is located
dataDirectory = "./sample.csv"
# dataDirectory = "../claims_final.csv"

# Initialize the files class
df = filesys.files(dataDirectory)
print (df.getData())
averageProcedurePrice = compute.averageProcedurePrice(df.getData())
averageStatePrice = compute.averageStatePrice(df.getData())

zScores = compute.zScoreByCategory(df.getData(), 4)
zS = compute.zScoreByCategory(df.getData(), 6)
plot.plotTest(zScores, zS, 'State', 'Procedure Type')

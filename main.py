from src import filesys, compute

# Directory where data is located
dataDirectory = "./sample.csv"
# dataDirectory = "../claims_final.csv"

# Initialize the files class
df = filesys.files(dataDirectory)
averagePrice = compute.average(df.getData())

from src import filesys

# Directory where data is located
dataDirectory = "./sample.csv"

# Initialize the files class
data = filesys.files(dataDirectory)
data.processData()
data.printData()

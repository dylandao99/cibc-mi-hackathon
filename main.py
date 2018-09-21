from src import filesys

dataDirectory = "sample.csv"
data = filesys.files(dataDirectory)
data.processData()
data.printData()

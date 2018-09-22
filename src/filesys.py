import pandas as pd
from random import randint


class files:
    # When initializing, read data from a CSV file and store it
    def __init__(self, directory):
        self.data = self.readData(directory)

    def readData(self, directory):
        data = pd.read_csv(directory, header=None)
        # Format dataset as a matrix
        return data

    def printData(self):
        print (self.data)

    def getData(self):
        return self.data

    def genOutput1(self, filename):
        uniqueProviderIDs = self.data[2].unique()
        rankList = []
        for i in range(0, self.data[2].nunique()):
            rankList += [randint(0, 1000000) / 1000000.0]

        d = {'providers': uniqueProviderIDs, 'rank': rankList}

        output1 = pd.DataFrame(d)
        output1.sort_values(by="rank", ascending=False, inplace=True)
        output1.to_csv(filename)

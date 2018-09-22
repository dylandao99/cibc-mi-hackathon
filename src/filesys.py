# files handles reading, processing, printing, and returning data from the CSV file
class files:
    # When initializing, create an empty array and read the raw data into that array
    def __init__(self, directory):
        self.data = self.readData(directory)

    # Fetch raw data from the CSV file and return it
    def readData(self, directory):
        # Open in read mode
        file = open(directory, 'r')
        return file.read()

    # Format the data and place it into a list of lists
    def processData(self):
        self.data = self.data.split('\n')
        length = len(self.data)
        for i in range(0, length):
            self.data[i] = self.data[i].split(',')
            string = ''

            if len(self.data[i]) < 8:
                del self.data[i]
            else:
                for char in range(0, len(self.data[i][4])):
                    char = self.data[i][4][char]
                    if char != '"':
                        string += char
                self.data[i][4] = string

    def getData(self):
        return self.data

    def printData(self):
        for i in range(0, len(self.data)):
            print (self.data[i])

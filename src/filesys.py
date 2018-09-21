class files:
    def __init__(self, directory):
        self.data = []
        self.readData(directory)

    def readData(self, directory):
        file = open(directory, 'r')
        self.data = file.read()

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

    def printData(self):
        for i in range(0, len(self.data)):
            print (self.data[i])

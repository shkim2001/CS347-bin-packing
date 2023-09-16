# class for problem
class Problem():
    # initializing variables for each problem object
    def __init__(self, problemID):
        self.problemID = problemID
        self.encodedBin = "####"
        self.finished = False
        self.bin = {}
        self.lastAddedBin = 0
        self.totalLen = 0
        self.totalSize = 0
    
    # ending problem
    def endProblem(self):
        self.finished = True
    
    # create a new bin for the problem object
    def createNewBin(self, newItem):
        newItem = int(newItem)
        
        self.bin[len(self.bin) + 1] = [newItem]
        self.lastAddedBin = len(self.bin)
    
    # place the new item in the correct bin
    def binPacking(self, newItem):
        newItem = int(newItem)
        
        if len(self.bin) == 0:
            self.createNewBin(newItem)
        else:
            success = False
            for binNum in range(1, len(self.bin)+1):
                if sum(self.bin[binNum]) + newItem <= 100:
                    self.bin[binNum].append(newItem)
                    self.lastAddedBin = binNum
                    success = True
                    break
            
            if success == False:
                self.createNewBin(newItem)
                
        self.totalLen += 1
        self.totalSize += newItem
        
        self.encodeBin()

    # encode the bins to a string format
    def encodeBin(self):
        binVal = list(self.bin.values())
        listAllEncodedBins = ["#", "#"]
        
        for i in range(len(binVal)):
            encodeCurrBin = "!".join(str(val) for val in binVal[i])
            listAllEncodedBins.insert(-1, encodeCurrBin)
        
        self.encodedBin = "#".join(str(encodedCurrBin) for encodedCurrBin in listAllEncodedBins)

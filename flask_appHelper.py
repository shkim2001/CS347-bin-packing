from problem import *
from callableCount import *

initProblemID = CallableCount(1)
listOfProblems = [0]

# helper for newProblem()
def makeNewProblem():
    id = initProblemID()
    newProblem = Problem(id)
    listOfProblems.append(newProblem)
    
    return newProblem

# helper for placeItem()
def addNewItemToProblem(problemID, newItem):
    currProblem = listOfProblems[int(problemID)]
    
    if currProblem.finished == True:
        return False
    
    currProblem.binPacking(newItem)
    
    return currProblem
    
# helper for endProblem
def endProblemByProblemID(problemID):
    currProblem = listOfProblems[int(problemID)]
    currProblem.endProblem()
    
    return currProblem

# calculate the total wasted space when the program tries to end a problem
def calculateWastedSpace(problemID):
    wastedSpace = 0
    currProblem = listOfProblems[int(problemID)]
    binVal = list(currProblem.bin.values())
    
    for currBinVal in binVal:
        wastedSpace += (100 - sum(currBinVal))
    
    return wastedSpace
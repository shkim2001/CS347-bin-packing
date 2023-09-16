from flask import Flask
from problem import *
from flask_appHelper import *


app = Flask(__name__)


@app.route('/newproblem/')
def newProblem():
    """Create new problem for bin packing

    Returns:
        problemID (int) -- integer that can be used to reference a particular set of bins that are being packed
        binEncoding (string) -- string representation of an empty set containing no bins
    """
    newProblemID = makeNewProblem()
    
    return {
        "problemID": newProblemID.problemID,
        "binEncoding": newProblemID.encodedBin,
    }


@app.route('/placeitem/<problemID>/<size>')
def placeItem(problemID, size):
    """Choose which bin to place the item in and then provide an encoding of the bins with the new item now placed within a bin

    Input:
        problemID (int) -- integer that can be used to reference a particular set of bins that are being packed
        size (int) -- size of the new item to be placed in a bin
        
    Returns:
        ID (int) - inputted problemID
        size (int) - inputted size
        loc (int) - number of the bin where the new item was placed
        bins (string) - string encoding the set of bins with the new itemed placed
        
    Error messages:
        "The Problem ID is not recognized" - User tries to place an item to a problem ID that does not exist
        "This problem ID no longer accepts new items" - The problem with the input problem ID was alreay ended
    """
    if int(problemID) >= len(listOfProblems):
        return "The Problem ID is not recognized"
    
    modifiedProblem = addNewItemToProblem(problemID, size)
    
    if modifiedProblem == False:
        return "This problem ID no longer accepts new items"
    
    return {
        "ID": problemID,
        "size": size,
        "loc": modifiedProblem.lastAddedBin,
        "bins": modifiedProblem.encodedBin,
    }

@app.route('/endproblem/<problemID>')
def endProblem(problemID):
    """End the current problem instance and return the ID, Size, Items, Count, and Wasted Space for the problem instance

    Input:
        problemID (int) -- integer that can be used to reference a particular set of bins that are being packed
    
    Returns:
        ID (int) - inputted problemID
        size (int) - total size of all of the items
        items (int) - number of items placed in the collection of bins
        count (int) - number of bins used to store the items
        wasted_space (int) - capacity of all of the bins minus the total size of the items
        bins (string) - string encoding of the final set of packed bins
    """
    
    endedProblem = endProblemByProblemID(problemID)
    wastedSpace = calculateWastedSpace(problemID)

    return {
        "ID": problemID,
        "size": endedProblem.totalSize,
        "items": endedProblem.totalLen,
        "count": len(endedProblem.bin),
        "wasted": wastedSpace,
        "bins": endedProblem.encodedBin,
        
    }


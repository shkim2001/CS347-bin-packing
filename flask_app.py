from flask import Flask
from problemID import *
from bins import *


app = Flask(__name__)


@app.route('/newproblem/')
def newProblem():
    """Create new problem for bin packing

    Returns:
        problemID (int) -- integer that can be used to reference a particular set of bins that are being packed
        binEncoding (string) -- string representation of an empty set containing no bins
    """
    newProblemID = newProblem()
    newBin = newBinInstance()
    
    problemID = newProblemID.createProblemID()
    binEncoding = newBin.createNewBin()
    
    return problemID, binEncoding


@app.route('/placeitem/<problemID>/<size>')
def placeItem(problemID, size):
    """Choose which bin to place the item in and then provide an encoding of the bins with the new item now placed within a bin

    Input:
        problemID (int) -- integer that can be used to reference a particular set of bins that are being packed
        size (int) -- size of the new item to be placed in a bin
        
    Returns:
        { 'ID': problemID 'size' : new_item_size 'loc' : bin_number 'bins' : new_bin_encoding }
    """
    
    

    return 

@app.route('/endproblem/<problemID>')
def endProblem(problemID):
    """End the current problem instance and return the ID, Size, Items, Count, and Wasted Space for the problem instance

    Input:
        problemID (int) -- integer that can be used to reference a particular set of bins that are being packed
    
    Returns:
        { 'ID': problemID 'size' : total_size 'items' : num_items 'count' : num_bins 'wasted' : wasted_space 'bins' : bin_encoding }
    """

    return 


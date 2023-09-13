from callableCount import CallableCount

# class for problemID
class ProblemID():
    def __init__(self):
        self.counter = CallableCount(1)
    
    def createProblemID(self):
        return self.counter()
    
def newProblemID():
    newProblem = ProblemID()
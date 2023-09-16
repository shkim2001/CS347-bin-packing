from flask import *
from flask_app import *
import unittest

class TestBinPack(unittest.TestCase):
    def testNewProblem(self):
        self.app = app.test_client()
        
        # create 100 different new problem IDs and check if they all have the corresponding ID values
        for i in range(1, 100):
            response = self.app.get('/newproblem/', follow_redirects=True)        
            self.assertIn(b"\"binEncoding\":\"####\",\"problemID\":%d" %i, response.data)

    def testPlaceItem(self):
        self.app = app.test_client()
        
        testDict = {
            "/placeitem/1/3": "\"ID\":\"1\",\"bins\":\"##3##\",\"loc\":1,\"size\":\"3\"",
            "/placeitem/1/3": "\"ID\":\"1\",\"bins\":\"##3!3##\",\"loc\":1,\"size\":\"3\"",
            "/placeitem/1/99": "\"ID\":\"1\",\"bins\":\"##3!3#99##\",\"loc\":2,\"size\":\"99\"",
            "/placeitem/8/99": "\"ID\":\"8\",\"bins\":\"##28##\",\"loc\":1,\"size\":\"28\"",
            "/placeitem/101/99": "The Problem ID is not recognized"
        }
        
        # run all test cases in the testdict above
        for responsePair in testDict:
            response = self.app.get(responsePair[0], follow_redirects=True)        
            self.assertIn(responsePair[1].encode(), response.data)
            
    def testEndProblem(self):
        self.app = app.test_client()
        
        testDict = {
            "/endproblem/1": "\"ID\":\"1\",\"bins\":\"##3!3#99##\",\"count\":2,\"items\":3,\"size\":105,\"wasted\":95",
            "/endproblem/20": "\"ID\":\"20\",\"bins\":\"####\",\"count\":0,\"items\":0,\"size\":0,\"wasted\":0",
            "/endproblem/8": "\"ID\":\"20\",\"bins\":\"##28##\",\"count\":1,\"items\":1,\"size\":28,\"wasted\":72",
            "/placeitem/1/19": "This problem ID no longer accepts new items"
        }
        
        # run all test cases in the testdict above
        for responsePair in testDict:
            response = self.app.get(responsePair[0], follow_redirects=True)        
            self.assertIn(responsePair[1].encode(), response.data)
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()
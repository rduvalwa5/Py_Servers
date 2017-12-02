'''
Test the zip_errors() function from the zipcheck module 
'''
import unittest
from zipcheck import zip_errors

class Test(unittest.TestCase):

#    def testName(self):
    def test_zip_errors(self):
        "Tests ensuring errors in data cause validation failures."
#        raise TypeError("No tests yet present.")
        self.assertIsNotNone(zip_errors("1234"), "Accepting length 4")
        self.assertIsNotNone(zip_errors("12345-678"), "Accepting length 9")
        self.assertIsNotNone(zip_errors("1234e"), "Accepting alphabetic 5")
        self.assertIsNotNone(zip_errors("12345-678Y"), "Accepting alphabetic 5+4")
        self.assertIsNotNone(zip_errors("12345/6789"), "Accepting non-hyphen")
        
    def test_zip_successes(self):
        "Test ensuring that valid data passes."
#        pass
        self.assertIsNone(zip_errors("12345"), "Not accepting 5-digit zips")
        self.assertIsNone(zip_errors("12345-6789"), "Not accepting 9-digit zips")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_zip_errors']
    unittest.main()


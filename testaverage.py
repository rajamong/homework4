# imports unittest functionality
import unittest
# imports average class from average program
from average import average

class testCase(unittest.TestCase):
    def setUp(self):
        self.average = average()

    # tests the mean calculation functionality with no errors
    def test1(self):
        self.assertEqual(self.average.findmean([1,2,3]), (2))
    
    # tests the mean calculation functionality with no inputs
    def test2(self):
        self.assertEqual(self.average.findmean([]), ('the list you entered is empty'))
    
    # tests the mean calculation functionality with no errors
    def test3(self):
        self.assertEqual(self.average.findmean([3,4,5,6]), (4.5))


if __name__ == "__main__":
    unittest.main()
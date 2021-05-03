# imports unittest functionality
import unittest
# imports fullname class from fullname program
from fullname import fullname

class testCase(unittest.TestCase):
    def setUp(self):
        self.fullname = fullname()

    # tests the name combining functionality with no errors
    def test1(self):
        self.assertEqual(self.fullname.combine('John', 'Doe'), ('John Doe'))
    
    # tests the combining functionality with no first name input
    def test2(self):
        self.assertEqual(self.fullname.combine('', 'Smith'), ('you are missing a first name'))
    
    # tests the combining functionality with no last name input
    def test3(self):
        self.assertEqual(self.fullname.combine('Jane',''), ('you are missing a last name'))


if __name__ == "__main__":
    unittest.main()
# imports unittest functionality
import unittest
# imports cube class from cubevolume program
from cubevolume import cubevolume

class testCase(unittest.TestCase):
    def setUp(self):
        self.cubevolume = cubevolume()

    # tests the volume calculation functionality with no errors
    def test1(self):
        self.assertEqual(self.cubevolume.volume(3), (27))
    
    # tests the volume calculation functionality with negative inputs
    def test2(self):
        self.assertEqual(self.cubevolume.volume(-7), ('the length you entered is invalid'))
    
    # tests the volume calculation functionality with non-number inputs
    def test3(self):
        self.assertEqual(self.cubevolume.volume('g'), ('the length you entered is invalid'))


if __name__ == "__main__":
    unittest.main()
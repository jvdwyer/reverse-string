import unittest
import main

class test_main(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEquals(main.reverse_string("Hello"), 'olleH')

if __name__ == '__main__':
    unittest.main()
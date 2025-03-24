import unittest

def test_func():
    return 1

class TestQ2(unittest.TestCase):
    def test_func(self):
        self.assertEqual(test_func(), 1)
        
if __name__ == '__main__':
    unittest.main()
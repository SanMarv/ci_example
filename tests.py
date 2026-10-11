import unittest
from fibonacci import fibonacci

class FibonacciTester(unittest.TestCase): 

    def test_0(self): 
        result = fibonacci(0)
        self.assertEqual(result, 0)

    def test_1(self): 
        result = fibonacci(1)
        self.assertEqual(result, 1)

    def test_7(self): 
        result = fibonacci(7)
        self.assertEqual(result, 13)




import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        self.calc = SimpleCalculator()

    
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)

    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertEqual(self.calc.subtract(2.5, 1.2), 1.3)


    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 1000), 0)
        self.assertEqual(self.calc.multiply(2.5, 2.0), 5.0)

    
    def test_division(self):
        """Test the divide method, including division by zero."""
        
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        # Division by zero should return None
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(0, 0), None)

if __name__ == "__main__":
    unittest.main()

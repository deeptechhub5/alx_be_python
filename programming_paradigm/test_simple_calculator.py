import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        self.calc = SimpleCalculator()

    # ---------- add ----------
    def test_addition_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(10**8, 1), 10**8 + 1)

    def test_addition_floats(self):
        # use assertAlmostEqual for float comparisons
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7, places=7)
        self.assertAlmostEqual(self.calc.add(-1.1, 1.1), 0.0, places=7)

    def test_addition_commutative(self):
        self.assertEqual(self.calc.add(7, 3), self.calc.add(3, 7))

    # ---------- subtract ----------
    def test_subtraction_basic(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtraction_floats(self):
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3, places=7)
        self.assertAlmostEqual(self.calc.subtract(-2.0, -3.5), 1.5, places=7)

    # ---------- multiply ----------
    def test_multiplication_basic(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiplication_by_zero_and_floats(self):
        self.assertEqual(self.calc.multiply(0, 1000), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0, places=7)

    def test_multiplication_negatives(self):
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    # ---------- divide ----------
    def test_division_normal(self):
        self.assertAlmostEqual(self.calc.divide(10, 2), 5.0, places=7)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=7)
        self.assertAlmostEqual(self.calc.divide(-9, 3), -3.0, places=7)

    def test_division_with_floats(self):
        self.assertAlmostEqual(self.calc.divide(5, 2.5), 2.0, places=7)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 1.0 / 3.0, places=7)

    def test_division_by_zero_returns_none(self):
        # Specified behavior: return None when denominator is zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    # ---------- non-numeric inputs (type errors) ----------
    def test_non_numeric_inputs_raise_type_error(self):
        # some operations with mixed types raise TypeError in Python (e.g., 'a' + 1)
        with self.assertRaises(TypeError):
            self.calc.add("a", 1)

        with self.assertRaises(TypeError):
            self.calc.subtract("a", "b")

        with self.assertRaises(TypeError):
            # str * str is not supported (raises TypeError)
            self.calc.multiply("2", "3")

        with self.assertRaises(TypeError):
            # division of a string by a number is not supported
            self.calc.divide("10", 2)

if __name__ == "__main__":
    unittest.main()

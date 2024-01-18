import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Initialize the calculator object before each test
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.add(3, 5), 8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(8, 3), 5)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(4, 6), 24)

    def test_division(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calculator.divide(8, 0)

    def test_decimal_input(self):
        self.assertEqual(self.calculator.add(0.1, 0.2), 0.300)

    def test_clear_function(self):
        self.calculator.add(5, 7)
        self.calculator.clear()
        self.assertEqual(self.calculator.display(), 0)

    def test_memory_functionality(self):
        self.calculator.memory_store(10)
        self.assertEqual(self.calculator.memory_recall(), 10)

        self.calculator.memory_store(7)
        self.calculator.memory_store(3)
        self.assertEqual(self.calculator.memory_recall(), 3)

    def test_user_input_validation_large_numbers(self):
        # Test input validation for very large numbers
        with self.subTest():
            with self.assertRaises(ValueError):
                self.calculator.add(2e16, 3)

        with self.subTest():
            with self.assertRaises(ValueError):
                self.calculator.add(2, 3e16)

        with self.subTest():
            with self.assertRaises(ValueError):
                self.calculator.add(2e16, 3e16)

    def test_user_input_negative_numbers(self):
        # Test input handling for negative numbers and correct output
        with self.subTest():
            self.assertEqual(self.calculator.add(-2, 3), 1)

        with self.subTest():
            self.assertEqual(self.calculator.subtract(2, -3), 5)

        with self.subTest():
            self.assertEqual(self.calculator.multiply(-2, -3), 6)

        with self.subTest():
            self.assertEqual(self.calculator.divide(-6, 3), -2)
if __name__ == '_main_':
    unittest.main()
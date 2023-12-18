import unittest
import math
from BLL.lab2.CalculatorCore import CalculatorCore
from unittest.mock import patch


class TestCalculatorCore(unittest.TestCase):

    def setUp(self):
        self.calculator = CalculatorCore()

    def test_add(self):
        result = self.calculator.calculate_number(5, 3, '+')
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calculator.calculate_number(5, 3, '-')
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calculator.calculate_number(5, 3, '*')
        self.assertEqual(result, 15)

    def test_divide(self):
        result = self.calculator.calculate_number(6, 3, '/')
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate_number(5, 0, '/')

    def test_square_root(self):
        result = self.calculator.calculate_number(9, 0, '√')
        self.assertEqual(result, 3)

    def test_power(self):
        result = self.calculator.calculate_number(2, 3, '^')
        self.assertEqual(result, 8)

    def test_modulo(self):
        result = self.calculator.calculate_number(10, 3, '%')
        self.assertEqual(result, 1)

    def test_memory_store_and_retrieve(self):
        self.calculator.store_in_memory(10)
        self.assertEqual(self.calculator.retrieve_from_memory(), 10)

    def test_add_to_history(self):
        self.calculator.add_to_history('5 + 3', 8)
        self.assertIn('5 + 3 - 8', self.calculator.history)

    def test_view_history_empty(self):
        self.assertEqual(self.calculator.view_history(), 'Empty history')

    def test_view_history_non_empty(self):
        self.calculator.add_to_history('5 + 3', 8)
        self.assertEqual(self.calculator.view_history(), '5 + 3 - 8')

    def test_change_decimal_places(self):
        with unittest.mock.patch('builtins.input', return_value='4'):
            self.calculator.change_decimal_places()
            self.assertEqual(self.calculator.settings['decimal_places'], 4)

    def test_toggle_memory_function(self):
        current_status = self.calculator.settings['use_memory']
        self.calculator.toggle_memory_function()
        self.assertNotEqual(self.calculator.settings['use_memory'], current_status)


if __name__ == '__main__':
    unittest.main()

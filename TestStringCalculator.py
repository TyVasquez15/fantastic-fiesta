import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("5"), 5)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("2,3"), 5)

    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("2,3,4"), 9)

    def test_zero_values(self):
        self.assertEqual(self.calculator.add("0,0,0"), 0)

    def test_newline_delimiter(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_custom_asterisk_delimiter(self):
        self.assertEqual(self.calculator.add("//[*]\n1*9"), 10)

    def test_custom_semicolon_delimiter(self):
        self.assertEqual(self.calculator.add("//[;]\n2;3;4"), 9)

    def test_multi_character_delimiter(self):
        self.assertEqual(self.calculator.add("//[***]\n1***2***3"), 6)

    def test_numbers_greater_than_1000_are_ignored(self):
        self.assertEqual(self.calculator.add("2,1001,3"), 5)

    def test_number_equal_to_1000_is_included(self):
        self.assertEqual(self.calculator.add("1000,2"), 1002)

    def test_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.calculator.add("-5")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.calculator.add("-2,-3,-4")

    def test_non_numeric_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.calculator.add("2,a,3")

    def test_mixed_numeric_and_non_numeric_values(self):
        with self.assertRaises(ValueError):
            self.calculator.add("10,hello")

    def test_negative_number_with_other_numbers(self):
        with self.assertRaises(ValueError):
            self.calculator.add("5,-2,3")

    def test_custom_delimiter_with_large_number(self):
        self.assertEqual(self.calculator.add("//[*]\n2*1001*3"), 5)

    def test_newline_and_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//[*]\n1*2*3"), 6)


if __name__ == "__main__":
    unittest.main()

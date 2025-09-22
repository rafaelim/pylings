import unittest
from functools import partial

def arithmetic_operations(op: str, a: int, b: int):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case "//":
            return a // b
        case "**":
            return a ** b
        case _:
            raise Exception("Operation not implemented")
            
    
class TestArithmeticOperations(unittest.TestCase):
    add = partial(arithmetic_operations, "+")
    sub = partial(arithmetic_operations, "-")
    mul = partial(arithmetic_operations, "*")
    div = partial(arithmetic_operations, "/")
    exp = partial(arithmetic_operations, "**")
    floor_div = partial(arithmetic_operations, "//")

    def test_add_positive_numbers(self):
        self.assertEqual(self.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.add(-2, -3), -5)

    def test_sub_positive_numbers(self):
        self.assertEqual(self.sub(8, 3), 5)

    def test_sub_negative_numbers(self):
        self.assertEqual(self.sub(-2, -3), 1)

    def test_mul_positive_numbers(self):
        self.assertEqual(self.mul(2, 3), 6)

    def test_mul_negative_numbers(self):
        self.assertEqual(self.mul(-2, -3), 6)

    def test_div_positive_numbers(self):
        self.assertEqual(self.div(7, 2), 3.5)

    def test_div_negative_numbers(self):
        self.assertEqual(self.div(-7, -2), 3.5)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.div(8, 0)

    def test_div_result_type(self):
        self.assertIsInstance(self.div(4, 2), float)

    def test_exp_positive_numbers(self):
        self.assertEqual(self.exp(2, 3), 8)

    def test_exp_negative_numbers(self):
        self.assertEqual(self.exp(-2, -3), -.125)

    def test_floor_div_positive_numbers(self):
        self.assertEqual(self.floor_div(7, 2), 3)

    def test_floor_div_negative_numbers(self):
        self.assertEqual(self.floor_div(-7, -2), 3)

    def test_invalid_operation(self):
        self.assertRaises(Exception, arithmetic_operations, '%', 8, 2)

    def test_invalid_operation_message(self):
        with self.assertRaises(Exception) as ex:
            arithmetic_operations("%", 8, 2)
        self.assertIn("Operation not implemented", str(ex.exception))

if __name__ == '__main__':
    unittest.main()

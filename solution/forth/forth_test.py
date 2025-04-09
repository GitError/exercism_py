import unittest
from forth import evaluate, StackUnderflowError


class ForthTest(unittest.TestCase):
    def test_numbers_only(self):
        self.assertEqual(evaluate(["1 2 3 4 5"]), [1, 2, 3, 4, 5])
    
    def test_addition(self):
        self.assertEqual(evaluate(["1 2 +"]), [3])
    
    def test_subtraction(self):
        self.assertEqual(evaluate(["3 4 -"]), [-1])
    
    def test_multiplication(self):
        self.assertEqual(evaluate(["2 4 *"]), [8])
    
    def test_division(self):
        self.assertEqual(evaluate(["12 3 /"]), [4])
    
    def test_integer_division(self):
        self.assertEqual(evaluate(["8 3 /"]), [2])
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            evaluate(["4 0 /"])
        self.assertEqual(str(context.exception), "divide by zero")
    
    def test_combined_arithmetic(self):
        self.assertEqual(evaluate(["1 2 + 4 * 5 + 3 -"]), [14])
    
    def test_dup(self):
        self.assertEqual(evaluate(["1 DUP"]), [1, 1])
    
    def test_drop(self):
        self.assertEqual(evaluate(["1 2 DROP"]), [1])
    
    def test_swap(self):
        self.assertEqual(evaluate(["1 2 SWAP"]), [2, 1])
    
    def test_over(self):
        self.assertEqual(evaluate(["1 2 OVER"]), [1, 2, 1])
    
    def test_stack_underflow_dup(self):
        with self.assertRaises(StackUnderflowError) as context:
            evaluate(["DUP"])
        self.assertEqual(str(context.exception), "Insufficient number of items in stack")
    
    def test_stack_underflow_drop(self):
        with self.assertRaises(StackUnderflowError):
            evaluate(["DROP"])
    
    def test_stack_underflow_swap(self):
        with self.assertRaises(StackUnderflowError):
            evaluate(["1 SWAP"])
    
    def test_stack_underflow_over(self):
        with self.assertRaises(StackUnderflowError):
            evaluate(["1 OVER"])
    
    def test_stack_underflow_add(self):
        with self.assertRaises(StackUnderflowError):
            evaluate(["1 +"])
    
    def test_case_insensitivity(self):
        self.assertEqual(evaluate(["1 DUP dup Dup drop DROP"]), [1])
    
    def test_word_definition(self):
        self.assertEqual(evaluate([": double 2 * ;", "1 double"]), [2])
    
    def test_nested_word_definition(self):
        self.assertEqual(evaluate([": double 2 * ;", ": quadruple double double ;", "1 quadruple"]), [4])
    
    def test_redefining_word(self):
        self.assertEqual(evaluate([": foo 5 ;", ": bar foo ;", ": foo 6 ;", "bar foo"]), [5, 6])
    
    def test_cannot_redefine_numbers(self):
        with self.assertRaises(ValueError):
            evaluate([": 1 2 ;"])
    
    def test_invalid_definition(self):
        with self.assertRaises(ValueError):
            evaluate([":"])
    
    def test_undefined_operation(self):
        with self.assertRaises(ValueError) as context:
            evaluate(["foo"])
        self.assertEqual(str(context.exception), "undefined operation")
    
    def test_multiline_input(self):
        self.assertEqual(evaluate(["1 2", "3", "+ *"]), [9])


if __name__ == "__main__":
    unittest.main()

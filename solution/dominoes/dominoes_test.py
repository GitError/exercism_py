import unittest
from dominoes import can_chain


class DominoesTest(unittest.TestCase):
    def test_empty_input_empty_output(self):
        self.assertEqual(can_chain([]), [])

    def test_singleton_input_singleton_output(self):
        self.assertEqual(can_chain([[1, 1]]), [[1, 1]])

    def test_singleton_that_cant_be_chained(self):
        self.assertEqual(can_chain([[1, 2]]), None)

    def test_three_elements(self):
        input_dominoes = [[1, 2], [3, 1], [2, 3]]
        output_chain = can_chain(input_dominoes)
        self.assert_valid_chain(input_dominoes, output_chain)

    def test_can_reverse_dominoes(self):
        input_dominoes = [[1, 2], [1, 3], [2, 3]]
        output_chain = can_chain(input_dominoes)
        self.assert_valid_chain(input_dominoes, output_chain)

    def test_cant_be_chained(self):
        self.assertEqual(can_chain([[1, 2], [4, 1], [2, 3]]), None)

    def test_disconnected_simple(self):
        self.assertEqual(can_chain([[1, 1], [2, 2]]), None)

    def test_disconnected_double_loop(self):
        self.assertEqual(can_chain([[1, 2], [2, 1], [3, 4], [4, 3]]), None)

    def test_disconnected_single_isolated(self):
        self.assertEqual(can_chain([[1, 2], [2, 3], [3, 1], [4, 4]]), None)

    def test_need_backtrack(self):
        input_dominoes = [[1, 2], [2, 3], [3, 1], [2, 4], [2, 4]]
        output_chain = can_chain(input_dominoes)
        self.assert_valid_chain(input_dominoes, output_chain)

    def test_separate_loops(self):
        self.assertEqual(can_chain([[1, 2], [2, 3], [3, 1], [1, 1], [2, 2], [3, 3]]), None)

    def test_nine_elements(self):
        input_dominoes = [[1, 2], [5, 3], [3, 1], [1, 2], [2, 4], [1, 6], [2, 3], [3, 4], [5, 6]]
        output_chain = can_chain(input_dominoes)
        self.assert_valid_chain(input_dominoes, output_chain)

    def assert_valid_chain(self, input_dominoes, output_chain):
        msg = f"Output chain {output_chain} is not a valid chain for input {input_dominoes}"
        
        # Check if output_chain is None - indicating that no valid chain exists
        if output_chain is None:
            self.fail(msg)
        
        # Check that the output chain contains exactly the same dominoes as the input
        self.assertEqual(sorted(input_dominoes), sorted([sorted(d) for d in output_chain]), msg)
        
        # Check that each adjacent domino shares a matching number
        for i in range(len(output_chain) - 1):
            self.assertEqual(output_chain[i][1], output_chain[i + 1][0], msg)
        
        # Check that the chain forms a loop (last value matches first value)
        if len(output_chain) > 0:
            self.assertEqual(output_chain[0][0], output_chain[-1][1], msg)


if __name__ == "__main__":
    unittest.main()

import unittest
from series import slices


class SeriesTest(unittest.TestCase):
    def test_slices_of_one_from_one(self):
        self.assertEqual(slices("1", 1), ["1"])

    def test_slices_of_one_from_two(self):
        self.assertEqual(slices("12", 1), ["1", "2"])

    def test_slices_of_two(self):
        self.assertEqual(slices("35", 2), ["35"])

    def test_slices_of_two_overlap(self):
        self.assertEqual(slices("9142", 2), ["91", "14", "42"])

    def test_slices_of_three(self):
        self.assertEqual(slices("97867", 3), ["978", "786", "867"])

    def test_slices_of_four(self):
        self.assertEqual(slices("01234", 4), ["0123", "1234"])

    def test_slices_of_five(self):
        self.assertEqual(slices("01234", 5), ["01234"])

    def test_slice_length_greater_than_series_length(self):
        with self.assertRaisesRegex(ValueError, "slice length cannot be greater than series length"):
            slices("12345", 6)

    def test_empty_series(self):
        with self.assertRaisesRegex(ValueError, "series cannot be empty"):
            slices("", 1)

    def test_zero_slice_length(self):
        with self.assertRaisesRegex(ValueError, "slice length cannot be zero"):
            slices("12345", 0)

    def test_negative_slice_length(self):
        with self.assertRaisesRegex(ValueError, "slice length cannot be negative"):
            slices("12345", -1)


if __name__ == "__main__":
    unittest.main()

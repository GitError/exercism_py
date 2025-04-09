import unittest
from twelve_days import recite


class TwelveDaysTest(unittest.TestCase):
    def test_first_day_only(self):
        expected = ["On the first day of Christmas my true love gave to me: "
                    "a Partridge in a Pear Tree."]
        self.assertEqual(recite(1, 1), expected)

    def test_second_day_only(self):
        expected = ["On the second day of Christmas my true love gave to me: "
                    "two Turtle Doves, and a Partridge in a Pear Tree."]
        self.assertEqual(recite(2, 2), expected)

    def test_third_day_only(self):
        expected = ["On the third day of Christmas my true love gave to me: "
                    "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."]
        self.assertEqual(recite(3, 3), expected)

    def test_fourth_day_only(self):
        expected = ["On the fourth day of Christmas my true love gave to me: "
                    "four Calling Birds, three French Hens, two Turtle Doves, "
                    "and a Partridge in a Pear Tree."]
        self.assertEqual(recite(4, 4), expected)

    def test_fifth_day_only(self):
        expected = ["On the fifth day of Christmas my true love gave to me: "
                    "five Gold Rings, four Calling Birds, three French Hens, "
                    "two Turtle Doves, and a Partridge in a Pear Tree."]
        self.assertEqual(recite(5, 5), expected)

    def test_twelfth_day_only(self):
        expected = ["On the twelfth day of Christmas my true love gave to me: "
                    "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, "
                    "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, "
                    "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, "
                    "two Turtle Doves, and a Partridge in a Pear Tree."]
        self.assertEqual(recite(12, 12), expected)

    def test_first_three_verses(self):
        expected = [
            "On the first day of Christmas my true love gave to me: "
            "a Partridge in a Pear Tree.",
            "On the second day of Christmas my true love gave to me: "
            "two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the third day of Christmas my true love gave to me: "
            "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(1, 3), expected)

    def test_middle_three_verses(self):
        expected = [
            "On the fourth day of Christmas my true love gave to me: "
            "four Calling Birds, three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree.",
            "On the fifth day of Christmas my true love gave to me: "
            "five Gold Rings, four Calling Birds, three French Hens, "
            "two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the sixth day of Christmas my true love gave to me: "
            "six Geese-a-Laying, five Gold Rings, four Calling Birds, "
            "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(4, 6), expected)

    def test_last_three_verses(self):
        expected = [
            "On the tenth day of Christmas my true love gave to me: "
            "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
            "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
            "four Calling Birds, three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree.",
            "On the eleventh day of Christmas my true love gave to me: "
            "eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, "
            "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
            "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree.",
            "On the twelfth day of Christmas my true love gave to me: "
            "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, "
            "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, "
            "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, "
            "two Turtle Doves, and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(10, 12), expected)

    def test_entire_song(self):
        expected = [
            "On the first day of Christmas my true love gave to me: "
            "a Partridge in a Pear Tree.",
            "On the second day of Christmas my true love gave to me: "
            "two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the third day of Christmas my true love gave to me: "
            "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the fourth day of Christmas my true love gave to me: "
            "four Calling Birds, three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree.",
            "On the fifth day of Christmas my true love gave to me: "
            "five Gold Rings, four Calling Birds, three French Hens, "
            "two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the sixth day of Christmas my true love gave to me: "
            "six Geese-a-Laying, five Gold Rings, four Calling Birds, "
            "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the seventh day of Christmas my true love gave to me: "
            "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
            "four Calling Birds, three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree.",
            "On the eighth day of Christmas my true love gave to me: "
            "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
            "five Gold Rings, four Calling Birds, three French Hens, "
            "two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the ninth day of Christmas my true love gave to me: "
            "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, "
            "six Geese-a-Laying, five Gold Rings, four Calling Birds, "
            "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
            "On the tenth day of Christmas my true love gave to me: "
            "ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
            "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
            "four Calling Birds, three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree.",
            "On the eleventh day of Christmas my true love gave to me: "
            "eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, "
            "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, "
            "five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree.",
            "On the twelfth day of Christmas my true love gave to me: "
            "twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, "
            "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, "
            "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, "
            "two Turtle Doves, and a Partridge in a Pear Tree."
        ]
        self.assertEqual(recite(1, 12), expected)


if __name__ == "__main__":
    unittest.main()

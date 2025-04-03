import unittest
from house import recite


class HouseTest(unittest.TestCase):
    def test_single_verse(self):
        self.assertEqual(
            recite(1, 1),
            ["This is the house that Jack built."]
        )

    def test_two_verses(self):
        self.assertEqual(
            recite(1, 2),
            [
                "This is the house that Jack built.",
                "This is the malt that lay in the house that Jack built."
            ]
        )

    def test_middle_verse(self):
        self.assertEqual(
            recite(6, 6),
            [
                "This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ]
        )

    def test_full_rhyme(self):
        self.assertEqual(
            recite(1, 12),
            [
                "This is the house that Jack built.",
                "This is the malt that lay in the house that Jack built.",
                "This is the rat that ate the malt that lay in the house that Jack built.",
                "This is the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
                "This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
            ]
        )


if __name__ == "__main__":
    unittest.main()
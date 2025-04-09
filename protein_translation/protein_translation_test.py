import unittest
from protein_translation import proteins

class ProteinTranslationTest(unittest.TestCase):
    
    def test_methionine_rna_sequence(self):
        self.assertEqual(proteins("AUG"), ["Methionine"])
    
    def test_phenylalanine_rna_sequence_1(self):
        self.assertEqual(proteins("UUU"), ["Phenylalanine"])
        
    def test_phenylalanine_rna_sequence_2(self):
        self.assertEqual(proteins("UUC"), ["Phenylalanine"])
        
    def test_leucine_rna_sequence_1(self):
        self.assertEqual(proteins("UUA"), ["Leucine"])
        
    def test_leucine_rna_sequence_2(self):
        self.assertEqual(proteins("UUG"), ["Leucine"])
        
    def test_serine_rna_sequence_1(self):
        self.assertEqual(proteins("UCU"), ["Serine"])
        
    def test_serine_rna_sequence_2(self):
        self.assertEqual(proteins("UCC"), ["Serine"])
        
    def test_serine_rna_sequence_3(self):
        self.assertEqual(proteins("UCA"), ["Serine"])
        
    def test_serine_rna_sequence_4(self):
        self.assertEqual(proteins("UCG"), ["Serine"])
        
    def test_tyrosine_rna_sequence_1(self):
        self.assertEqual(proteins("UAU"), ["Tyrosine"])
        
    def test_tyrosine_rna_sequence_2(self):
        self.assertEqual(proteins("UAC"), ["Tyrosine"])
        
    def test_cysteine_rna_sequence_1(self):
        self.assertEqual(proteins("UGU"), ["Cysteine"])
        
    def test_cysteine_rna_sequence_2(self):
        self.assertEqual(proteins("UGC"), ["Cysteine"])
        
    def test_tryptophan_rna_sequence(self):
        self.assertEqual(proteins("UGG"), ["Tryptophan"])
        
    def test_stop_codon_rna_sequence_1(self):
        self.assertEqual(proteins("UAA"), [])
        
    def test_stop_codon_rna_sequence_2(self):
        self.assertEqual(proteins("UAG"), [])
        
    def test_stop_codon_rna_sequence_3(self):
        self.assertEqual(proteins("UGA"), [])
        
    def test_translate_rna_strand_into_correct_protein_list(self):
        strand = "AUGUUUUGG"
        expected = ["Methionine", "Phenylalanine", "Tryptophan"]
        self.assertEqual(proteins(strand), expected)
        
    def test_translation_stops_if_stop_codon_at_beginning_of_sequence(self):
        strand = "UAGUGG"
        expected = []
        self.assertEqual(proteins(strand), expected)
        
    def test_translation_stops_if_stop_codon_in_middle_of_sequence(self):
        strand = "AUGUUUUAAAUGUUU"
        expected = ["Methionine", "Phenylalanine"]
        self.assertEqual(proteins(strand), expected)
        
    def test_translation_stops_if_stop_codon_at_end_of_sequence(self):
        strand = "AUGUUUUAA"
        expected = ["Methionine", "Phenylalanine"]
        self.assertEqual(proteins(strand), expected)
        
    def test_incomplete_rna_sequence(self):
        strand = "AUGUUU"
        expected = ["Methionine", "Phenylalanine"]
        self.assertEqual(proteins(strand), expected)
        
    def test_incomplete_rna_sequence_missing_one_nucleotide(self):
        strand = "AUGUUUU"
        expected = ["Methionine", "Phenylalanine"]
        self.assertEqual(proteins(strand), expected)
        
    def test_multiple_proteins(self):
        strand = "AUGUUUUCUUAAAUG"
        expected = ["Methionine", "Phenylalanine", "Serine"]
        self.assertEqual(proteins(strand), expected)

if __name__ == "__main__":
    unittest.main()

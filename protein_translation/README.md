# Protein Translation

This is a Python implementation that translates RNA sequences into proteins.

## Description

RNA can be broken into three-nucleotide sequences called codons, which are then translated to amino acids to build proteins. This program translates RNA sequences into their corresponding protein sequences according to the RNA codon table.

## RNA Codon Table

| Codon | Amino Acid    |
|-------|---------------|
| AUG   | Methionine    |
| UUU, UUC | Phenylalanine |
| UUA, UUG | Leucine      |
| UCU, UCC, UCA, UCG | Serine       |
| UAU, UAC | Tyrosine     |
| UGU, UGC | Cysteine     |
| UGG   | Tryptophan    |
| UAA, UAG, UGA | STOP         |

## Features

- Translates RNA sequences into their corresponding protein sequences
- Properly handles STOP codons (stops translation at the first STOP codon)
- Handles incomplete sequences (ignores incomplete codons at the end)

## Usage

```python
from protein_translation import proteins

# Translate a simple RNA sequence
result = proteins("AUGUUU")
# Returns: ['Methionine', 'Phenylalanine']

# Translate a sequence with a STOP codon
result = proteins("AUGUUUUAA")
# Returns: ['Methionine', 'Phenylalanine']
```

## Testing

Run the unit tests using:

```
python -m unittest protein_translation_test.py
```

## Notes

- Translation stops if a STOP codon (UAA, UAG, or UGA) is encountered
- All subsequent codons after a STOP codon are ignored
- Incomplete codons at the end of the strand are ignored

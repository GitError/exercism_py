# RNA Transcription

This module provides a function to determine the RNA complement of a given DNA sequence.

---

## 📝 Function

### `to_rna(dna_strand: str) -> str`
Transcribes a DNA strand into its RNA complement.

#### Parameters:
- `dna_strand` (str): A string representing the DNA strand. Contains only the characters `'A'`, `'C'`, `'G'`, and `'T'`.

#### Returns:
- `str`: A string representing the RNA complement of the DNA strand. Contains only the characters `'A'`, `'C'`, `'G'`, and `'U'`.

---

## 🚀 Usage

### Example 1: Transcribe DNA to RNA
```python
from rna_transcription import to_rna

result = to_rna("ACGTGGTCTTAA")
print(result)  # Output: "UGCACCAGAAUU"
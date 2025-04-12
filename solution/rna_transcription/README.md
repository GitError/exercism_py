# RNA Transcription

This module provides a function to determine the RNA complement of a given DNA sequence.

## 🧬 Background

RNA transcription is the process by which DNA is copied to RNA by an enzyme called RNA polymerase. During this process, each DNA nucleotide is matched with its RNA complement:

| DNA | RNA |
|-----|-----|
| G   | C   |
| C   | G   |
| T   | A   |
| A   | U   |

Note that Uracil (U) in RNA replaces Thymine (T) found in DNA.

---

## 📝 Function

### `to_rna(dna_strand: str) -> str`
Transcribes a DNA strand into its RNA complement.

#### Parameters:
- `dna_strand` (str): A string representing the DNA strand. Contains only the characters `'A'`, `'C'`, `'G'`, and `'T'`.

#### Returns:
- `str`: A string representing the RNA complement of the DNA strand. Contains only the characters `'A'`, `'C'`, `'G'`, and `'U'`.

#### Raises:
- `KeyError`: If the input DNA strand contains invalid characters (anything other than 'A', 'C', 'G', 'T').

---

## 🚀 Usage

### Example 1: Transcribe DNA to RNA
```python
from rna_transcription import to_rna

result = to_rna("ACGTGGTCTTAA")
print(result)  # Output: "UGCACCAGAAUU"
```

### Example 2: Single Nucleotide Transcription
```python
from rna_transcription import to_rna

print(to_rna("G"))  # Output: "C"
print(to_rna("C"))  # Output: "G"
print(to_rna("T"))  # Output: "A"
print(to_rna("A"))  # Output: "U"
```

### Example 3: Empty Strand
```python
from rna_transcription import to_rna

print(to_rna(""))  # Output: ""
```

---

## 🛠️ Implementation Details

The function uses Python's `str.maketrans()` and `translate()` methods for efficient character-by-character substitution, creating a mapping from DNA nucleotides to their RNA complements.

## ⚠️ Error Handling

The function will raise a `KeyError` if:
- The input contains lowercase letters (e.g., "AcGt")
- The input contains characters that are not valid DNA nucleotides (e.g., "ACGTX", "1234")

Always ensure the input consists solely of uppercase 'A', 'C', 'G', and 'T' characters.
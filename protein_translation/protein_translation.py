def proteins(strand):
    """
    Translate RNA sequences into proteins.
    
    Args:
        strand (str): A string representing an RNA sequence.
        
    Returns:
        list: A list of protein names translated from the RNA sequence.
              Translation stops when a STOP codon is encountered.
              
    Examples:
        >>> proteins("AUGUUUUCU")
        ['Methionine', 'Phenylalanine', 'Serine']
        >>> proteins("AUGUUUUCUUAAAUG")
        ['Methionine', 'Phenylalanine', 'Serine']
    """
    codon_to_protein = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine", "UUC": "Phenylalanine",
        "UUA": "Leucine", "UUG": "Leucine",
        "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
        "UAU": "Tyrosine", "UAC": "Tyrosine",
        "UGU": "Cysteine", "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
    }
    
    protein_sequence = []
    
    # Process codons (3 nucleotides at a time)
    for i in range(0, len(strand), 3):
        if i + 3 <= len(strand):
            codon = strand[i:i+3]
            amino_acid = codon_to_protein.get(codon)
            
            # Stop translation if STOP codon encountered
            if amino_acid == "STOP":
                break
            
            if amino_acid:
                protein_sequence.append(amino_acid)
    
    return protein_sequence

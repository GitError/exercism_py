def to_rna(dna_strand):
    """Transcribe a DNA strand into its RNA complement.

    :param dna_strand: str - A string representing the DNA strand.
    :return: str - A string representing the RNA complement of the DNA strand.
    """
    return dna_strand.translate(str.maketrans('GCTA', 'CGAU'))

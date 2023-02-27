Nucleotides = ["A", "C", "G", "T"]

# Lets check the sequence to make sure it is valid...



def validateSeq(dna_seq):
    temp_sequence = dna_seq.upper()
    for nuc in temp_sequence:
        if nuc not in Nucleotides:
            return False
    return temp_sequence
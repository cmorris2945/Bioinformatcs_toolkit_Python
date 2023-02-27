Nucleotides = ["A", "C", "G", "T"]
import collections

# Lets check the sequence to make sure it is valid...



def validateSeq(dna_seq):
    temp_sequence = dna_seq.upper()
    for nuc in temp_sequence:
        if nuc not in Nucleotides:
            return False
    return temp_sequence

def countNucFrequency(sequence):
        tempFrequency_Dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        for nucleotide in sequence:
            tempFrequency_Dict[nucleotide] += 1
        return tempFrequency_Dict
      ## **if you want you can use this method from the "collections" module.
      # But you don't have to. This function will work just fine without it.
      # So leave it uncommented.***
      #return dict(collections.Counter(sequence))

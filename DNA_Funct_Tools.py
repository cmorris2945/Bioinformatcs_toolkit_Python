import collections

Nucleotides = ["A", "C", "G", "T"]
DNA_ReversCompliment = {"A": "T", "T": "A",a "G": "C", "C": "G"}

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

## DNA is "transcribed" into RNA, where "T" is replaced with "U"
def transcription(sequence):
    return sequence.replace( "T", "U")

# Reverse compliment DNA Function. This will give the reverse of the string you put in
def reverse_compliment(sequence):
     return ''.join([DNA_ReversCompliment[nuc] for nuc in sequence])[::-1]
     
         
     
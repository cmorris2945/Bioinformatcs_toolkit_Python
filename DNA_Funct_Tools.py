import collections
import structures

Nucleotides = ["A", "C", "G", "T"]
DNA_ReversCompliment = {"A": "T", "T": "A", "G": "C", "C": "G"}

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
#     return ''.join([DNA_ReversCompliment[nuc] for nuc in sequence])[::-1]

##*** This particular approach below, is more "Pythonic" and a little bit faster solution...***

    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]

def gc_content(sequence):
     ## This gets the GC content in a DNA/RNA sequence ###
     return round((sequence.count('C') + sequence.count('G')) /len(sequence) * 100)

def gc_content_subsec(sequence, k = 20):
     ## GC Content in a DNA/RNA sub-seuquence length k. k = 20 by default
    res = []
    for i in range(0, len(sequence) - k +1, k):
         subseq = sequence[i:i + k]
         res.append(gc_content(subseq))
    return res

def translate_seq(sequence, init_pos=0):
     ##translate a DNA sequence into an aminoaid sequence
    return [DNA_Codons[sequence[pos:pos +3]] for pos in range(init_pos, len(sequence) - 2, 3)]


def codon_usage(sequence, aminoacid):
     ### This function will provide a frequency of each codon encoding a given aminoacid
     ## in a DNA Sequence

     tmpList = []
     for i in range(0, len(sequence) - 2, 3):
          if DNA_Codons[sequence[i:i +3]] == aminoacid:
               tmpList.append(sequence[i:i + 3])
     fredDict = dict(Counter(tmpList))
     totalWight = sum(freqDict.values())
     for sequence in freqDict:
          freqDict[sequence] = round(freqDict[sequence] / totalWight, 2)
     return freqDict

def gen_reading_frames(sequence):
     ## This function generates the 6 reading frames of a DNA Sequence, including reverse compliment...
     frames = []
     frames.append(translate_seq(sequence, 0))
     frames.append(translate_seq(sequence, 1))
     frames.append(translate_seq(sequence, 2))
     frames.append(translate_seq(reverse_compliment(sequence), 0))
     frames.append(translate_seq(reverse_compliment(sequence), 1))
     frames.append(translate_seq(reverse_compliment(sequence), 2))
    


     return frames

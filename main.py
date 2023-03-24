## DNA tool set and where we test the code functions and files...
from DNA_Funct_Tools import *
import random
from utilities import colored
import structures

rand_DNA_String1 = "ATTGCCCGTAA"
rand_DNA_String2 = "ATCcCGGX"
random_DNA_String3 = ''.join([random.choice(Nucleotides)
                              for nuc in range(30)])

DNAStr = validateSeq(random_DNA_String3)

#print(f'\nSequence is: colored((rand_DNA_String1)\n')
#print(f'[1] + Sequence Length: {len(DNAStr)}\n')
#print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))

#print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')

#print(f"'[4] + DNA STRING + Reverse Compliment:\n5' {colored(DNAStr)} 3'")

#print(f" {''.join([' |' for c in range(len(DNAStr))])}")
#print(f"3' {colored(reverse_compliment(DNAStr))} s'\n")

#print(f'[5g] + GC Content: {gc_content(random_DNA_String3)}%\n')

#print(f'[6] + GC Content in Subsection k =5: {gc_content_subsec(random_DNA_String3, k=5)}')

#print(f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr, 0)}\n')

#print(f'[8] + Codon Frequency (L): {codon_usage(DNAStr, "L")}\n ')

#print(f'[9] + Reading_frames: ')

#for frame in gen_reading_frames(DNAStr):
#    print(frame)

test_rf_frame = ['L', 'M', 'T', 'A', 'L', 'V', 'V',
                 'L','V', 'R', 'R', 'G', 'S', 'V', '_', 'G', 'H']

print(proteins_from_rf(test_rf_frame))


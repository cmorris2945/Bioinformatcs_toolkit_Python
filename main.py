## DNA tool set and where we test the code functions and files...
from DNA_Funct_Tools import *
import random
from utilities import colored

rand_DNA_String1 = "ATTGCCCGTAA"
rand_DNA_String2 = "ATCcCGGX"
random_DNA_String3 = ''.join([random.choice(Nucleotides)
                              for nuc in range(30)])

DNAStr = validateSeq(random_DNA_String3)

print(f'\nSequence is: colored((rand_DNA_String1)\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))

print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')

print(f"'[4] + DNA STRING + Reverse Compliment:\n5' {colored(DNAStr)} 3'")

print(f" {''.join([' |' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_compliment(DNAStr))} s'\n")
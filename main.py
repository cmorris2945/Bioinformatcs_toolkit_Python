## DNA tool set and where we test the code functions and files...
from DNA_Funct_Tools import *
import random

rand_DNA_String1 = "ATTGCCCGTAA"
rand_DNA_String2 = "ATCcCGGX"
random_DNA_String3 = ''.join([random.choice(Nucleotides)
                              for nuc in range(20)])



print(validateSeq(rand_DNA_String1))

print(validateSeq(rand_DNA_String2))

print(validateSeq(random_DNA_String3))
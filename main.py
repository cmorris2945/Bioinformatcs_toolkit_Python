## DNA tool set and where we test the code functions and files...
from DNA_Funct_Tools import *
import random
from utilities import colored

rand_DNA_String1 = "ATTGCCCGTAA"
#rand_DNA_String2 = "ATCcCGGX"
#random_DNA_String3 = ''.join([random.choice(Nucleotides)
#                              for nuc in range(20)])

DNAStr = validateSeq(rand_DNA_String1)

print(f'\nSequence is: colored((rand_DNA_String1)\n')

#print(validateSeq(rand_DNA_String2))

#print(validateSeq(random_DNA_String3))


#Test_DNA_String = validateSeq(random_DNA_String3)
#print(countNucFrequency(Test_DNA_String))

#print(transcription((random_DNA_String3)))

#DNA_str = "CCATAA"
#print(reverse_compliment(DNA_str))
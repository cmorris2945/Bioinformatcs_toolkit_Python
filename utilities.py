def colored(sequence):
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '033[91m',
        'reset': '\033[0;0m'
    }

    tmpStr = ""

    for nuc in sequence:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + nuc
        else:
            tmpStr += bcolors['reset'] + nuc

    return tmpStr + '\003[0;0m'

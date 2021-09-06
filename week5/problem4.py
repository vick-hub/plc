import os
import sys
import random

"""
Notes:
- Great job!
- You're missing the translation bit.
"""

def main():
    alphabet = list('ACGT')
    dna = [random.choice(alphabet) for i in range(100)]
    dna = ''.join(dna)
    print(f"DNA: {dna}")
    rna = ""
    for i in dna:
        if i == "A":
            rna += "U"
        elif i == "C":
            rna += "G"
        elif i == "G":
            rna += "C"
        else:
            rna += "A"
    print(f"RNA: {rna}")
#    protein_string = ""
#    for i in range(0, len(rna)-(3+len(rna) % 3), 3):
#         if rna[i:i+3] == 'STOP':
#            break
#        protein_string += rna[i+3]
#    print("Protein string:", protein_string)
#    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())

# 1. Two homologous DNA strands of equal length
reference_dna =  input("Enter a Reference DNA sequence: ")
sample_dna    =  input("Enter Sample DNA sequence: ")

# 2. Pair up matching positions and count the differences
mutations = 0
for base1, base2 in zip(reference_dna, sample_dna):
    if base1 != base2:
        mutations += 1

print("Total Point Mutations:", mutations)

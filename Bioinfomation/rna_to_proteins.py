from Bio.Seq import translate

rna_sequence = input("Enter an RNA sequence: ")
protein_sequence = translate(rna_sequence)
print(f"Protein sequence: {protein_sequence}")
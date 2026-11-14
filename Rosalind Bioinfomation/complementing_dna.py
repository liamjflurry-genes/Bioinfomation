dna_sequence = input("Enter a DNA sequence: ")
complementary_sequence = dna_sequence.translate(str.maketrans("ATCG", "TAGC"))
reverse_complementary_sequence = complementary_sequence[::-1]
print(f"Complementary DNA sequence 3' - 5': {reverse_complementary_sequence}")
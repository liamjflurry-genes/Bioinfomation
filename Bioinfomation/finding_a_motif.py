# 1.  main DNA strand and the shorter motif
dna = input("Enter the main DNA strand: ")
motif = input("Enter the motif to search for: ")

positions = []

# 2. Slide a window across the DNA one base at a time
for i in range(len(dna) - len(motif) + 1):
    # Slice out a chunk the exact same length as the motif
    window = dna[i : i + len(motif)]
    
    if window == motif:
        # Add 1 because biology counts starting at 1, while Python starts at 0
        positions.append(str(i + 1))

# 3. Print all matching positions separated by spaces
print(" ".join(positions))
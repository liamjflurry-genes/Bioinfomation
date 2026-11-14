from Bio import Entrez, SeqIO

# 1. Tell NCBI who you are (required by NCBI's server rules)
Entrez.email = "example@example.com"

sequence_id = "NC_000021"
output_filename = "human_chr21.fasta"

# 2. Fetch the sequence
handle = Entrez.efetch(db="nucleotide", id=sequence_id, rettype="fasta", retmode="text")

# 3. Parse the downloaded stream directly into a Biopython SeqRecord
record = SeqIO.read(handle, "fasta")
handle.close()

# 4. Inspect the real human gene
print("Gene ID:", record.id)
print("Description:", record.description)
print("Length:", len(record.seq), "base pairs")
print("First 60 bases:", record.seq[:60])

SeqIO.write(record, output_filename, "fasta")

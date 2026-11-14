from pathlib import Path

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# The input folder is expected to be labeled "to_check_gc_content" and located in the same directory as this script.
input_folder = Path(__file__).resolve().parent / "to_check_gc_content"
if not input_folder.is_dir():
    raise FileNotFoundError(f"Input folder not found: {input_folder}")

fasta_files = sorted(
    path
    for path in input_folder.iterdir()
    if path.is_file() and path.suffix.lower() == ".txt"
)
if not fasta_files:
    raise FileNotFoundError(f"No FASTA files found in: {input_folder}")

for fasta_file in fasta_files:
    record_count = 0
    for record in SeqIO.parse(fasta_file, "fasta"):
        gc_content = gc_fraction(record.seq) * 100
        print(f"{fasta_file.name}:{record.id}: {gc_content:.6f}%")
        record_count += 1
    if record_count == 0:
        raise ValueError(f"No FASTA records found in: {fasta_file}")
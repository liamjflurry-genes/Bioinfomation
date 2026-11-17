from Bio import Entrez

Entrez.email = "liamjflurry@gmail.com"

def search_pdb_codes(protein_name, max_results=5):
    print(f"Searching Protein Data Bank for '{protein_name}'...\n")
    
    # 1. Search NCBI's 3D 'structure' database for human proteins matching your keyword
    search_query = f"{protein_name}[Title] AND Homo sapiens[Organism]"
    search_handle = Entrez.esearch(db="structure", term=search_query, retmax=max_results)
    search_results = Entrez.read(search_handle)
    search_handle.close()
    
    id_list = search_results["IdList"]
    if not id_list:
        print("No structures found. Try a broader protein name!")
        return

    # 2. Fetch the summary details (including the 4-character ChimeraX PDB code)
    summary_handle = Entrez.esummary(db="structure", id=",".join(id_list))
    summaries = Entrez.read(summary_handle)
    summary_handle.close()

    # 3. Print clean, copy-pasteable ChimeraX commands
    for item in summaries:
        pdb_code = item["PdbAcc"]
        title = item["PdbDescr"]
        print(f"ChimeraX Command:  open {pdb_code.lower()}")
        print(f"Structure Title:   {title}\n" + "-" * 50)

# Test it out with any protein name!
protein = input("Enter a protein name (e.g., Huntingtin, Insulin, p53): ")
search_pdb_codes(protein)

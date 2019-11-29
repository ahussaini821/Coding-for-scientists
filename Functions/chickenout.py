aa_count = {'A': 0, 'R': 0, 'N': 0, 'D': 0, 'C': 0, 'Q': 0, 'E': 0, 'G':0,
           'H': 0, 'I': 0, 'L': 0, 'K': 0, 'M': 0, 'F': 0, 'P': 0, 'S': 0,
           'T': 0, 'W': 0, 'Y': 0, 'V': 0}

fasta = open("chick.txt")
lines = fasta.readlines()
protein_count = 0.0
protein_lengths = [] 
for x in lines:
    if ">" in x:
        protein_lengths.append(protein_count)
        protein_count = 0.0
    else:
        for i in x:
            if i in aa_count:
                aa_count[i] += 1
                protein_count += 1.0
            else:
                continue
            
print reduce(lambda x, y: x + y, protein_lengths) / len(protein_lengths)
print aa_count
    
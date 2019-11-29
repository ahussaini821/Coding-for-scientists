file_name1 = raw_input("What is the name of the fasta file? ")
file_name2 = raw_input("What is the name of the second fasta file? ")


def fasta_combine(file_name, fasta_combined):
    
    fasta_combined = open("combined.fas", "a")
    fasta = open(file_name, "r")
    lines = fasta.readlines()
    
    for i in lines:
        fasta_combined.write(i)
    
fasta_combine(file_name1, fasta_combined)
fasta_combine(file_name2, fasta_combined)
import csv

limit = float(raw_input("What is your E-value threshold? "))
print"\n"

fasta = open("blast2.csv", "r")
header = ""
for i in range(7):
    header += fasta.readline()

for line in csv.reader(fasta, delimiter=','):
    
    try:
        if float(line[10]) <= limit:
            print "Accession number: "+line[1]
            print "E-value:          "+line[10]+"\n"
        else:
            pass
    except:
        continue
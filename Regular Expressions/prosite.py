import re

pattern = re.compile(r"[C]\w[H]\w[LIVMFY][C]\w\w[C][LIVMYA]")
infile = open("chick.fasta", "r")

seq = ""
header = ""

for line in infile:
    if line[0] == ">":
        
        if (pattern.search(seq)!=None):
            print header
        header = line.rstrip()
        seq = ""
    else:
        seq+= line.rstrip()
if (rgx.search(seq)!=None):
    print header
infile.close()

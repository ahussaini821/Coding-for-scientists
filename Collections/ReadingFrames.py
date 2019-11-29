nucleotide = "TAATCGTATACCGGG"
nu_list = list(nucleotide)

final =[nu_list[x:] for x in range(len(nu_list)-2)]


count =1 
for i in final:
    x = ''.join(i)
    
    y = list(x)
    
    final2 = [y[x:x+3] for x in range(0,len(y)-2,3)]
    
    for i in final2:
        if count%4 != 0:
            x = ''.join(i)
            print x
        
    count += 1    
    print "\n"
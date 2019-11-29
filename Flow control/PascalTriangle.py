x = int(raw_input("How many lines of Pascal's triangle do you want? "))
trow = [1]
trow_previous = [1,1]

print (" ".join( map(str, trow)))
print (" ".join( map(str, trow_previous)))


for i in range(x):
    
    trow_current = []
    trow_current.append(1)
    
    

    for i in range(len(trow_previous)):
    
    
        if i < (len(trow_previous)-1):
            
            trow_current.append((trow_previous[i]+trow_previous[i+1]))
        
        else:
            trow_current.append(1)
            trow_previous = trow_current[:]
    #final = ''.join(trow_current)
    #print trow_current
    print (" ".join( map(str, trow_current)))
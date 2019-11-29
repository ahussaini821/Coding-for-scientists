answer = "tiger"
guess = "t tpa"
clue = list(guess)
clue2 = list(guess)
clue_test = [0,0,0,0,0]


def is_in(answer,guess, clue_test):
    
    answer = list(answer)
    guess = list(guess)
    
    for i in range(len(guess)):
        if guess[i] in answer:
            
            if clue_test[i] == 2:
                
                pass
            else:
                clue_test[i] = 1

    return clue_test
    
def is_position(answer, guess, clue_test):
    
    answer = list(answer)
    guess = list(guess)
    for i in guess:
        if i in answer and guess.index(i) == answer.index(i):
            
            clue_test[guess.index(i)] = 2
            
        else:
            
            guess[guess.index(i)] = ' '
                
       
    return clue_test
                    

clue_test = is_position(answer, guess, clue_test)

clue_test = is_in(answer, guess, clue_test)


for i in range(len(clue_test)):
    
    if clue_test[i] == 1:
        clue[i] = "("+clue[i]+")"
    
    elif clue_test[i] == 2:
        clue[i] = "["+clue[i]+"]"

 
# Magic one line code

clue=''.join(["["+str(guess[x])+"]" if guess[x]==answer[x] 
      else "("+str(guess[x])+")" if guess[x] in answer   
      else guess[x] for x in range(len(guess))])
        
print clue
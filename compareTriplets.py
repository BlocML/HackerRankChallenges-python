# Complete the compareTriplets function below.
def compareTriplets(a, b):
    #first initialise output values
    alice_score = 0
    bob_score = 0
    countdown = len(a)
    x = 0
    #write comparison control statements
    while countdown > 0:
        if a[x] > b[x]:
            alice_score +=1
        elif a[x] < b[x]:
            bob_score +=1
        elif a[x] == b[x]:
            continue
            
        countdown -=1
        x +=1
        
    return [alice_score,bob_score]

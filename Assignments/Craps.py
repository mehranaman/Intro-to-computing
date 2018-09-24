#File: Craps.py
#Description: Computing the probabilty of winning at Craps.

#Name: Naman Mehra
#UTEID: nm26465
#Course name: CS303E
#Unique number: 51850
#Date created: Feb 24th, 2017
#Date last modified: Feb 24th, 2017



import random


def craps():

    #starting the round- come out phase
    
    m = random.randint(1,6)
    n = random.randint(1,6)
    p = m + n

    #winning in the first roll:
    if p == 7 or p == 11:
        return 1
            
    #losing in the first roll:       
    elif p == 2 or p == 3 or p == 12:
        return 0

     
     
    else: #if p such that (p>= 4 and p <7) or (p>7 and p<=10)
        #point phase begins: 
        q = random.randint(1,6)
        w = random.randint(1,6)
        t = q+w
    
        #assuming that the player can have any number of rolls as long as he/she doesn't hit 7 first.
        if t == 7:
            return 0

        while t != 7:
            if t == p: #once the player has rolled p he/she only needs to keep rolling until hitting a 7, so he/she has practically won the game already. 
                return 1

            else:
                
                q = random.randint(1,6)
                w = random.randint(1,6)
                t = q + w
                if t == 7: #if he hits 7 before the value of p, then he loses automatically.
                    return 0
                
               


        

def main():
    
    num_rounds = int(input("Enter number of rounds: "))
    num_wins = 0
    
    for g in range(0, num_rounds):
        num_wins = num_wins + craps()

    print("Player wins ", num_wins, " out of ", num_rounds, " rounds.")

main ()    
            
        
            
     
        

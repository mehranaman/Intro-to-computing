# Deal.py

#description: Short, efficient code to compute the probability of winning the Monty hall game.

# Student's name: Naman Mehra

# UTEID: nm26465

# Course name: CS 303E

#unique number: 51850

#Date created: Feb 27th, 2017

#Date last modified: 27th Feb, 2017

import random

def monty():

    #defining following random variables
    
    prize = random.randint(1,3)
    guess = random.randint(1,3)
    view = random.randint(1,3)



    #to ensure the view is not the same as prize or guess, I add a while loop.
    #Since the range is short the processor should not take too long in reaching the desired view value.
    while view == prize or view == guess:
        
        view = random.randint(1,3)



    #switching to the other door.
    new_guess = random.randint(1,3)


    #the same concept of while loop to ensure the other door fulfills our enforced restrictons.
    while new_guess == guess or new_guess == view:
        new_guess = random.randint(1,3)


    #the print funtion makes the table, no need to use format.
    print (" ",prize, "       ",guess,"        ",view,"        ",new_guess)


    #winning returns 1 and losing returns 0.
    if new_guess == prize:
        
        return 1
    
    if new_guess != prize:
        
        return 0
          

def main():

    #asking for nuser's input. 
    num_trial = eval(input("Enter the number of trials: "))


    #printing the headers of the table.
    print("Prize      Guess      View      New Guess")
    print()
    num_win = 0


    for i in range(0, num_trial):
        num_win += monty()


    #new assignments for convenience.
        
    prob_win_switch = round (num_win/num_trial, 5) #rounding done for better presentation. 
    prob_win_not_switch = round (1 - prob_win_switch, 5) 

    print()
    print("Probability of winning if you switch =", prob_win_switch)
    print('Probability of winning if you don\'t switch = ', prob_win_not_switch)

main()
    

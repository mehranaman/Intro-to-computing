#  File: GuessingGame.py

#  Description: Dare to guess.

#  Student Name: Naman Mehra

#  Student UT EID: nm26465

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: April, 12th 2017

#  Date Last Modified:April, 12th, 2017


def bin_search():
    count = 1
    
    lo = 1
    hi = 100

    while (lo<=hi):
        mid = (lo + hi)//2
        print("Guess " + str(count)+ " : The number you thought was " + str(mid) )
        count += 1
        enter = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))

        while enter != 1 and enter != 0 and enter != -1 :

            enter = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
            
        if enter == 0:
            print("Thank you for playing the Guessing Game.")
            return 

        elif enter == -1:
            lo = mid + 1
                
   
        elif enter == 1 :
            hi = mid-1

        if count > 7:
            print ("Either you guessed a number out of range or you had an incorrect entry.")
            return

        
def main():
    count = 1
    print("Think of a number between 1 and 100  inclusive.")
    print("And I will guess what it is in 7 tries or less.")
    ready = input("Are you ready? (y/n): ")

    while (ready != 'y' and ready != 'n'):
        ready = input("Are you ready? (y/n): ")
    if ready == 'n':
        print("Bye")
        return

    elif ready == 'y':
        bin_search()


main()
        
    
        

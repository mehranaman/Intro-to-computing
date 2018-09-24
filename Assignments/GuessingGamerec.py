

def bin_search(lo, hi):
    
    while (lo<=hi):
        
        mid = (lo + hi) // 2
        print("Guess " + str(count)+ " : The number you thought was " + str(mid) )
        count += 1

        while enter != 1 and enter != 0 and enter != 0 :


            enter = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
            

        
            if enter == 0:
                print("Thank you for playing the Guessing Game.")
                return 

            elif enter == 1:
                lo = mid + 1
                bin_search(lo, hi)
   
            elif enter == -1:
                hi = mid-1
                bin_search(lo, hi)

            else:
                enter = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
            
        
        if count > 7:
            print ("Either you guessed a number out of range or you had an incorrect entry.")
            return 
            
        
    if lo > hi:
        
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
        bin_search(1, 100)


main()   
    

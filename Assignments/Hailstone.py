#  File: Hailstone.py

#  Description: We are writing a code for Collatz conjecture, that is any number can be reduced to 1 with the same basic computations depending on if the number is even or odd.

#  Student Name: Naman Mehra

#  Student UT EID: nm26465

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: March 3rd, 2017

#  Date Last Modified: March 3rd, 2017

def main():

    #defining variables that I use later in the code.
    greatest_cycle_count = 0
    greatest_num = 0

    #the range of numbers which have to be reduced to 1.
    start_range =  int(input("Enter starting number of the range: "))
    end_range = int(input("Enter ending number of the range: "))


    #prompt if the etries are not within our domain of expectation. 
    while (end_range <= start_range) or (end_range < 1) or (start_range<1):
        
        start_range = int(input("Enter starting number of the range: "))
        end_range = int(input("Enter ending number of the range: "))

    #for loop for reducing each number in the entered range. 
    for i in range(start_range, end_range + 1):
        n = i
        num = 0
        while n > 1:
            if n%2 == 0:
                n = n/2
                
            else:
                n = 3*n + 1

            num += 1
            #this is the part of the loop that commands displaying the number with the greatest cycle counts.
            if num > greatest_cycle_count:
                greatest_cycle_count = num
                greatest_num = i

    
    print("The number ",greatest_num, " has the longest cycle of ",greatest_cycle_count, ".")


main()

    
            

            

                                   
     
                




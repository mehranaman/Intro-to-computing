#  File: Goldbach.py

#  Description: Good, efficient code for computing values to prove the Goldbach conjecture.

#  Student Name: Naman Mehra

#  Student UT EID: nm26465

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: March 24th, 2017

#  Date Last Modified: March 24th, 2017

#the is_prime() function.
def is_prime(n):
    lim = int (n**0.5 + 1)
    is_prime = True
    divisor = 2
    while (divisor<lim):
        if n%divisor == 0:
            is_prime = False
            break
        divisor += 1
    return is_prime


#the beginning of the main body of Goldbach's cojecture's code.

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))



#while loop to ensure conditions for Goldbach's conjecture conditions.

while(lower_limit < 4 or lower_limit%2 == 1 or lower_limit >= upper_limit or upper_limit%2 == 1):
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))

#for loop to range between the entered lower and upper limits.    

for i in range(lower_limit, upper_limit + 1, 2):
    #important use of print function for the correct structure of output.
    print(i,end = '')

    #for loop that ranges between all numbers from 2 to half the current 'i' + 1.
    for j in range (2, i//2 + 1):
        if is_prime(j):
            p = i - j
            if is_prime(p):
                print(" =",j, "+", p, end = '')

    #important use of print function for the correct structure of output.
    print(" ")

    
                    
                    
        
            

    

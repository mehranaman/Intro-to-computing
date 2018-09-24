#  File: recursion1.py 

#  Description:

#  Student Name:

#  Student UT EID:

#  Course Name: CS 303E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# Given n of 1 or more, return the factorial of n, 
# which is n * (n-1) * (n-2) ... 1.
# Compute the result recursively (without loops). 
def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)

# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies 
# recursively (without loops or multiplication).
def bunnyEars(bunnies):
    if (bunnies == 1):
        return 1
    else:
        return 2 + bunnyEars(bunnies-1)


# The fibonacci sequence is a famous bit of mathematics, and it happens 
# to have a recursive definition. The first two values in the sequence 
# are 0 and 1 (essentially 2 base cases). Each subsequent value is the 
# sum of the previous two values, so the whole sequence is: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on.
# Define a recursive fibonacci(n) method that returns the nth fibonacci 
# number, with n=0 representing the start of the sequence.
def fibonacci(n):
    if n == 1 or n == 0 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# We have bunnies standing in a line, numbered 1, 2, ...
# The odd bunnies (1, 3, ..) have the normal 2 ears.
# The even bunnies (2, 4, ..) we'll say have 3 ears, because they each 
# have a raised foot. Recursively return the number of "ears" in the 
# bunny line 1, 2, ... n (without loops or multiplication).
def bunnyEars2(bunnies):
    if n == 1:
        return 2
    if (n%2 == 0):
        return 3 + bunnyEars2(n-1)
    else:
        return 2 + bunnyEars2(n-1)

# We have triangle made of blocks. The topmost row has 1 block, the 
# next row down has 2 blocks, the next row has 3 blocks, and so on.
# Compute recursively (no loops or multiplication) the total number of 
# blocks in such a triangle with the given number of rows. 
def triangle(rows):
    if n == 1:
        return 1
    else:
        return n + triangle(n-1)

# Given a non-negative int n, return the sum of its digits recursively 
# (no loops). Note that mod (%) by 10 yields the rightmost digit 
# (126 % 10 is 6), while divide (//) by 10 removes the rightmost digit 
# (126 / 10 is 12).
def sumDigits(n):
    if n > 0:
        p = n%10
        n = n//10
        reutrn p + sumDigits(n)
    else:
        return 0

# Given a non-negative int n, return the count of the occurrences of 7 
# as a digit, so for example 717 yields 2. (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), 
# while divide (//) by 10 removes the rightmost digit (126 // 10 is 12).
def count7(n):
    if n > 0:
        if n%10 == 7:
            n = n//10
            return 1 + count7(n)
        else:
            n == n//10
            return 0 + count7(n)
    else:
        return 0

# Given a non-negative int n, compute recursively (no loops) the count 
# of the occurrences of 8 as a digit, except that an 8 with
# another 8 immediately to its left counts double, so 8818 yields 4. 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (//) by 10 removes the rightmost digit (126 // 10 is 12).
def count8(n):
    if n > 0:
        if n%10 == 8:
            n = n//10
            if n%10 == 8:
                return 2 + count8(n)
            else:
                return 1 + count8(n)
        else:
            n == n//10
            return 0 + count8(n)
    else:
        return 0


# Given base and n that are both 1 or more, compute recursively (no loops) 
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
def powerN(base, n):
    if n == 1:
        return base
    else:
        n = n-1
        return base * powerN(base, n)


# Given a string, compute recursively (no loops) the number of lowercase 
# 'x' chars in the string.
def countX(str):
    if str[0] == 'x':
        return 1 + countX(str[1:])
    else:
        return countX(str[1:])
    
# Given a string, compute recursively (no loops) the number of times 
# lowercase "hi" appears in the string.
def countHi(str):
    if str[0] == 'h' and str[1] == 'i':
        return 1 + countHi(str[1:len(str)-1])
    else:
        return countHi(str[1:len(str)-1])
    

            
        
    
    
        





    




    

#  File: Grid.py

#  Description:Maximum product of four adjacent numbers in a grid.

#  Student Name: Naman Mehra

#  Student UT EID: nm26465

#  Partner Name:NA

#  Partner UT EID: NA

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: April 21st, 2017

#  Date Last Modified: April 22nd, 2017





def main():
    in_file = open("./grid.txt","r")

    string = in_file.readline().strip()
    dim = int(string)
    grid = []


    for i in range(dim):
        line = in_file.readline()
        line = line.strip()
        row = line.split()
        for j in range(dim):
            row[j] = int(row[j])
        grid.append(row)


    
    
    
    #read each row in blocks of four
    max_prod = 0

    for row in grid:
        for i in range(dim-3):
            prod = 1
            for j in range(i,i+4):
                prod = prod*row[j]
            if prod >= max_prod:
                max_prod = prod

    for j in range (dim):
        for i in range(dim-3):
            prod = 1
            for k in range(i, i+4):
                prod = prod*grid[k][j]
            if prod>= max_prod:
                max_prod = prod
    for i in range(dim-3):
        for j in range(dim-3):
            prod = 1
            for k in range(4):
                prod = prod*grid[i+k][j+k]
            if prod>= max_prod:
                max_prod = prod
    for i in range (dim-3):
        for j in range(3,dim):
            prod = 1
            for k in range(4):
                prod = prod*grid[i+k][j-k]
            if prod >= max_prod:
                max_prod = prod
                
    

    print("The greatest product is " + str(max_prod) + ".")
    in_file.close()

main()

    

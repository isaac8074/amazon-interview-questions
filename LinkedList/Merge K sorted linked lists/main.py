# Python3 program to merge k sorted
# arrays of size n each

# A Linked List node
class Node:
	
	def __init__(self):
		
		self.data = 0
		self.next = None

# Function to print nodes in a
# given linked list
def printList(node):

	while (node != None):
		print(node.data, end = ' ')
		node = node.next
	
# Takes two lists sorted in increasing order,
# and merge their nodes together to make one
# big sorted list. Below function takes
# O(Log n) extra space for recursive calls,
# but it can be easily modified to work with
# same time and O(1) extra space
def SortedMerge(a, b):

	result = None

	# Base cases
	if (a == None):
		return(b)
	elif (b == None):
		return(a)

	# Pick either a or b, and recur
	if (a.data <= b.data):
		result = a
		result.next = SortedMerge(a.next, b)
	else:
		result = b
		result.next = SortedMerge(a, b.next)
	
	return result

# The main function that takes an array of lists
# arr[0..last] and generates the sorted output
def mergeKLists(arr, last):

	# Repeat until only one list is left
	while (last != 0):
		i = 0
		j = last

		# (i, j) forms a pair
		while (i < j):
			
			# Merge List i with List j and store
			# merged list in List i
			arr[i] = SortedMerge(arr[i], arr[j])

			# Consider next pair
			i += 1
			j -= 1
			
			# If all pairs are merged, update last
			if (i >= j):
				last = j

	return arr[0]

# Utility function to create a new node.
def newNode(data):

	temp = Node()
	temp.data = data
	temp.next = None
	return temp

# Driver code
if __name__=='__main__':
	
	# Number of linked lists
	k = 3
	
	# Number of elements in each list
	n = 4

	# An array of pointers storing the
	# head nodes of the linked lists
	arr = [0 for i in range(k)]

	arr[0] = newNode(1)
	arr[0].next = newNode(3)
	arr[0].next.next = newNode(5)
	arr[0].next.next.next = newNode(7)

	arr[1] = newNode(2)
	arr[1].next = newNode(4)
	arr[1].next.next = newNode(6)
	arr[1].next.next.next = newNode(8)

	arr[2] = newNode(0)
	arr[2].next = newNode(9)
	arr[2].next.next = newNode(10)
	arr[2].next.next.next = newNode(11)

	# Merge all lists
	head = mergeKLists(arr, k - 1)

	printList(head)

# This code is contributed by rutvik_56
# Time Complexity: O(N*log(k)) - As outer while loop in function mergeKLists() runs log k times and every time it processes n*k elements
# Space Complexity: O(N) or O(n*k) - b/c recursion is used in sortedmerge() and to merge the final 2 linked lists of size N/2, N recursive calls will be made

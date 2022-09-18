# Python3 program to reverse a queue
from collections import deque
 
# Function to reverse the queue
 
 
def reversequeue(queue):
    Stack = []
 
    while (queue):
        Stack.append(queue[0])
        queue.popleft()
 
    while (len(Stack) != 0):
        queue.append(Stack[-1])
        Stack.pop()
 
 
# Driver code
if __name__ == '__main__':
    queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
 
    reversequeue(queue)
    print(queue)
 
# This code is contributed by PranchalK
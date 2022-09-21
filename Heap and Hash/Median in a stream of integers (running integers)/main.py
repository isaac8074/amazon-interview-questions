# Python code to implement the approach
 
from heapq import heappush, heappop, heapify
import math
 
# Function to find the median of stream of data
def streamMed(arr, N):
     
    # Declaring two min heap
    g = []
    s = []
    for i in range(len(arr)):
       
        # Negation for treating it as max heap
        heappush(s, -arr[i])
        heappush(g, -heappop(s))
        if len(g) > len(s):
            heappush(s, -heappop(g))
 
        if len(g) != len(s):
            print(-s[0])
        else:
            print((g[0] - s[0])/2)
 
 
# Driver code
if __name__ == '__main__':
    A = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    N = len(A)
     
    # Function call
    streamMed(A, N)
'''
Time Complexity: If we omit the way how stream was read, complexity of median finding is O(N*log(N)), as we need to read the stream, and due to heap insertions/deletions.
Space Complexity: O(N) - At first glance the above code may look comlpex. If you read the code carefully, it is simple algorithm
'''
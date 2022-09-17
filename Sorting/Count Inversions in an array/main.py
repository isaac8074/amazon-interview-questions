from heapq import heappush, heappop
from bisect import bisect, insort
  
  
def getNumOfInversions(A):
    N = len(A)
    if N <= 1:
        return 0
  
    sortList = []
    result = 0
  
    # heapsort, O(N*log(N))
    for i, v in enumerate(A):
        heappush(sortList, (v, i))
  
    x = []  # create a sorted list of indexes
    while sortList:  # O(N)
        v, i = heappop(sortList)  # O(log(N))
        # find the current minimum's index
        # the index y can represent how many minimums on the left
        y = bisect(x, i)  # O(log(N))
        # i can represent how many elements on the left
        # i - y can find how many bigger nums on the left
        result += i - y
  
        insort(x, i)  # O(log(N))
  
    return result
  
# Driver Code
# Given array is
A = [-1, 6, 3, 4, 7, 4]
result = getNumOfInversions(A)
print(f'Number of inversions are {result}')
# Time Complexity: O(nlog(n)) - Both heapsort and bisection can perform sorted insertion in log(n) in each element, so the time complexity is O(nlogn)
# Space Complexity: O(n) A heap and a new list are the same length as the original array
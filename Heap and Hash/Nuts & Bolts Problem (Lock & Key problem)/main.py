# Python program to solve nut and bolt
# problem using Quick Sort.
from typing import List
 
# Method to print the array
def printArray(arr: List[str]) -> None:
    for i in range(6):
        print(" {}".format(arr[i]), end=" ")
    print()
 
# Similar to standard partition method.
# Here we pass the pivot element too
# instead of choosing it inside the method.
def partition(arr: List[str], low: int, high: int, pivot: str) -> int:
    i = low
    j = low
    while j < high:
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif (arr[j] == pivot):
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
        j += 1
    arr[i], arr[high] = arr[high], arr[i]
 
    # Return the partition index of
    # an array based on the pivot
    # element of other array.
    return i
 
# Function which works just like quick sort
def matchPairs(nuts: List[str], bolts: List[str], low: int, high: int) -> None:
    if (low < high):
 
        # Choose last character of bolts
        # array for nuts partition.
        pivot = partition(nuts, low, high, bolts[high])
 
        # Now using the partition of nuts
        # choose that for bolts partition.
        partition(bolts, low, high, nuts[pivot])
 
        # Recur for [low...pivot-1] &
        # [pivot+1...high] for nuts and
        # bolts array.
        matchPairs(nuts, bolts, low, pivot - 1)
        matchPairs(nuts, bolts, pivot + 1, high)
 
# Driver code
if __name__ == "__main__":
 
    # Nuts and bolts are represented
    # as array of characters
    nuts = ['@', '#', '$', '%', '^', '&']
    bolts = ['$', '%', '&', '^', '@', '#']
 
    # Method based on quick sort which
    # matches nuts and bolts
    matchPairs(nuts, bolts, 0, 5)
    print("Matched nuts and bolts are : ")
    printArray(nuts)
    printArray(bolts)
 
# This code is contributed by sanjeev2552
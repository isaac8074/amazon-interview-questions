# Python program to merge K
# sorted arrays of size n each.
N = 4
 
# Merge arr1[0..n1-1] and arr2[0..n2-1] into
# arr3[0..n1+n2-1]
 
 
def mergeArrays(arr1, arr2, N1, N2, arr3):
 
    i, j, k = 0, 0, 0
 
    # Traverse both array
    while (i < N1 and j < N2):
 
        # Check if current element of first
        # array is smaller than current element
        # of second array. If yes, store first
        # array element and increment first array
        # index. Otherwise do same with second array
        if (arr1[i] < arr2[j]):
            arr3[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr3[k] = arr2[j]
            k += 1
            j += 1
 
    # Store remaining elements of first array
    while (i < N1):
        arr3[k] = arr1[i]
        k += 1
        i += 1
 
    # Store remaining elements of second array
    while (j < N2):
        arr3[k] = arr2[j]
        k += 1
        j += 1
 
# A utility function to print array elements
 
 
def printArray(arr, size):
 
    for i in range(size):
        print(arr[i], end=" ")
 
# This function takes an array of arrays
# as an argument and all arrays are assumed
# to be sorted. It merges them together
# and prints the final sorted output.
 
 
def mergeKArrays(arr, i, j, output):
 
    global N
 
    # If one array is in range
    if (i == j):
        for p in range(N):
            output[p] = arr[i][p]
 
        return
 
    # If only two arrays are left
    # them merge them
    if (j - i == 1):
        mergeArrays(arr[i], arr[j],
                    N, N, output)
        return
 
    # Output arrays
    out1 = [0 for i in range(N * (((i + j) // 2) - i + 1))]
    out2 = [0 for i in range(N * (j - ((i + j) // 2)))]
 
    # Divide the array into halves
    mergeKArrays(arr, i, (i + j) // 2, out1)
    mergeKArrays(arr, (i + j) // 2 + 1, j, out2)
 
    # Merge the output array
    mergeArrays(out1, out2,
                N * (((i + j) / 2) - i + 1),
                N * (j - ((i + j) / 2)), output)
 
 
# Driver's code
if __name__ == '__main__':
    arr = [[2, 6, 12, 34],
           [1, 9, 20, 1000],
           [23, 34, 90, 2000]]
 
    K = len(arr)
    output = [0 for i in range(N * K)]
 
    # Function call
    mergeKArrays(arr, 0, 2, output)
 
    print("Merged array is ")
    printArray(output, N * K)
 
# This code is contributed by shinjanpatra
# Time Complexity: O(N * K*log(K)) There are log K levels as in each level the K arrays are divided in half and at each leve, the K arrays are traverseed
# Space Complexity: O(N*K*log(K)) in each level O(N*K) space is required
# python implementation of For each element in 1st
# array count elements less than or equal to it
# in 2nd array

# function returns the index of largest element
# smaller than equal to 'x' in 'arr'. For duplicates
# it returns the last index of occurrence of required
# element. If no such element exits then it returns -1
def bin_search(arr, n, x):
    l = 0
    h = n - 1
    while (l <= h):
        mid = int((l + h) // 2)
        # if 'x' is greater than or equal to arr[mid],
        # then search in arr[mid + 1...h]
        if (arr[mid] <= x):
            l = mid + 1
        else:
            # else search in arr[l...mid-1]
            h = mid - 1
    # required index
    return h

# function to count for each element in 1st array,
# elements less than or equal to it in 2nd array


def countElements(arr1, arr2, m, n):
    # sort the 2nd array
    arr2.sort()

    # for each element in first array
    for i in range(m):
        # last index of largest element
        # smaller than or equal to x
        index = bin_search(arr2, n, arr1[i])
        # required count for the element arr1[i]
        print(index + 1, end=" ")


# driver program to test above function
arr1 = [1, 2, 3, 4, 7, 9]
arr2 = [0, 1, 2, 1, 1, 4]
m = len(arr1)
n = len(arr2)
countElements(arr1, arr2, m, n)

# This code is contributed by Aditi Sharma
# Time Complexity: O(mlog(n) + nlog(n)) - Considering arr1[] and arr2[] of sizes m and n respectively
# Space Complexity: O(1)

# Python implementation of simple method to find count of
# pairs with given sum.

# Returns number of pairs in arr[0..n-1] with sum equal to 'sum'


def getPairsCount(arr, n, sum):
    unordered_map = {}
    count = 0
    for i in range(n):
        if sum - arr[i] in unordered_map:
            count += unordered_map[sum - arr[i]]
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
    return count


# Driver code
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print('Count of pairs is', getPairsCount(arr, n, sum))

# This code is contributed by Manish Thapa
# Time Complexity: O(n)
# Space Complexity: O(n)

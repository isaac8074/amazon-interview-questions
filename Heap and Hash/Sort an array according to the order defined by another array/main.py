from collections import Counter
 
# Function to sort arr1
# according to arr2
def solve(arr1, arr2):
    # Our output array
    res = []
     
    # Counting Frequency of each
    # number in arr1
    f = Counter(arr1)
     
    # Iterate over arr2 and append all
    # occurrences of element of
    # arr2 from arr1
    for e in arr2:
       
        # Appending element 'e',
        # f[e] number of times
        res.extend([e]*f[e])
         
        # Count of 'e' after appending is zero
        f[e] = 0
         
    # Remaining numbers in arr1 in sorted
    # order (Numbers with non-zero frequency)
    rem = list(sorted(filter(
      lambda x: f[x] != 0, f.keys())))
     
    # Append them also
    for e in rem:
        res.extend([e]*f[e])
         
    return res
 
 
# Driver Code
if __name__ == "__main__":
    arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    arr2 = [2, 1, 8, 3]
    print(*solve(arr1, arr2))
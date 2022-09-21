
# Python program to rearrange characters in a string
# so that no two adjacent characters are same.
 
from heapq import heappush, heappop
from collections import Counter
 
# A key class for readability
 
 
class Key:
    def __init__(self, character: str, freq: int) -> None:
        self.character = character
        self.freq = freq
 
    def __lt__(self, other: "Key") -> bool:
        return self.freq > other.freq
 
 
# Function to rearrange character of a string
# so that no char repeat twice
def rearrangeString(str: str):
    n = len(str)
    # Creating a frequency hashmap
    count = dict()
    for i in str:
        count[ord(i)] = count.get(ord(i), 0) + 1
 
    pq = []
    for c in range(97, 123):
        if count.get(c, 0):
            heappush(pq, Key(chr(c), count))
 
    # null character for default previous checking
    prev = Key('#', -1)
    str = ""
 
    while pq:
        key = heappop(pq)
        str += key.character
 
        # Since one character is already added
        key.freq -= 1
 
        # We avoid inserting if the frequency drops to 0
        if prev.freq > 0:
            heappush(pq, prev)
 
        prev = key
 
    if len(str) != n:
        print("Not possible")
    else:
        print(str)
 
 
# Driver's Code
if __name__ == "__main__":
    string = "bbbaa"
 
    # Function call
    rearrangeString(string)
 
    # This code is contributed by kraanzu.
    '''
    Time Complexity: O(N*log(N))
    Space Complexity: O(N)
    '''
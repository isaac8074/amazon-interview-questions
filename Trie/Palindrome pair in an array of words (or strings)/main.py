
def function(wordlist):
  #storing word in reverse format along with their indices.
   
    hashmap_reverse = {word[::-1]: index for index, word in enumerate(wordlist)}
    ans = []
    #enumerating over all words and for each character of them
    for index, word in enumerate(wordlist):
        for i in range(len(word)):
          #extracting left and right of them
            left, right = word[:i+1], word[i+1:]
            #checking if left exists and is palindrome and also right is present in map
            #this is to make sure the best edge case described holds.
             
            if not len(left) == 0 and left == left[::-1] and right in hashmap_reverse and hashmap_reverse[right] != index:
                ans.append([hashmap_reverse[right], index])
               
            #normal case.
            if right == right[::-1] and left in hashmap_reverse and hashmap_reverse[left] != index:
                ans.append([index, hashmap_reverse[left]])
    if len(ans)>0:
        return True
    return False
   
   
words = ["geekf", "geeks", "or","keeg", "abc", "bc"]
print(function(words))
# Time Complexity: O(nl) where n = length og array and l = length of longest string
# Space Complexity: O(n)
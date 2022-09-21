# Python3 program to find maximum
# integer possible by doing at-most
# K swap operations on its digits.
 
# function to find maximum integer
# possible by doing at-most K swap
# operations on its digits
def findMaximumNum(string, k, maxm, ctr):
      
    # return if no swaps left
    if k == 0:
        return
  
    n = len(string)
    # Consider every digit after
    # the cur position
    mx = string[ctr]
 
    for i in range(ctr+1,n):
        # Find maximum digit greater
        # than at ctr among rest
        if int(string[i]) > int(mx):
            mx=string[i]
             
    # If maxm is not equal to str[ctr],
    # decrement k       
    if(mx!=string[ctr]):
        k=k-1
     
    # search this maximum among the rest from behind
    # first swap the last maximum digit if it occurs more than 1 time
    # example str= 1293498 and k=1 then max string is 9293418 instead of 9213498
    for i in range(ctr,n):
        # If digit equals maxm swap
        # the digit with current
        # digit and recurse for the rest
        if(string[i]==mx):
            # swap str[ctr] with str[j]
            string[ctr], string[i] = string[i], string[ctr]
            new_str = "".join(string)
            # If current num is more than
            # maximum so far
            if int(new_str) > int(maxm[0]):
                  maxm[0] = new_str
  
            # recurse of the other k - 1 swaps
            findMaximumNum(string, k , maxm, ctr+1)
 
            # backtrack
            string[ctr], string[i] = string[i], string[ctr]
  
# Driver Code
if __name__ == "__main__":
    string = "129814999"
    k = 4
    maxm = [string]
    string = [char for char in string]
    findMaximumNum(string, k, maxm, 0)
    print(maxm[0])
  
# This code is contributed Aarti_Rathi
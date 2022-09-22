# A Dynamic Programming based Python3 program
# to find maximum number of A's
# that can be printed using four keys
 
# this function returns the optimal
# length string for N keystrokes
def findoptimal(N):
 
    # The optimal string length is
    # N when N is smaller than 7
    if (N <= 6):
        return N
 
    # An array to store result of
    # subproblems
    screen = [0] * N
 
    # Initializing the optimal lengths
    # array for until 6 input
    # strokes.
     
    for n in range(1, 7):
        screen[n - 1] = n
 
    # Solve all subproblems in bottom manner
    for n in range(7, N + 1):
         
        # for any keystroke n, we will need to choose between:-
        # 1. pressing Ctrl-V once after copying the
        # A's obtained by n-3 keystrokes.
 
        # 2. pressing Ctrl-V twice after copying the A's
        # obtained by n-4 keystrokes.
 
        # 3. pressing Ctrl-V thrice after copying the A's
        # obtained by n-5 keystrokes.
        screen[n - 1] = max(2 * screen[n - 4],
                        max(3 * screen[n - 5],
                            4 * screen[n - 6]));
         
    return screen[N - 1]
 
# Driver Code
if __name__ == "__main__":
 
    # for the rest of the array we
    # will reply on the previous
    # entries to compute new ones
    for N in range(1, 21):
        print("Maximum Number of A's with ", N,
              " keystrokes is ", findoptimal(N))
 
# This code is contributed by ashutosh450
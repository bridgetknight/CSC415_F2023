from random import randint
import time
import pyllist

# Problem 1: function to determine the missing number in a sequential list of integers
def missing_number(arr):

    # Start from second value in array and compare to previous number in sequence
    start = 1
    
    for idx, num in enumerate(arr[start:], start=start):

        # If the current number is not the next expected number in the sequence, 
        # then print and return missing value
        if(num != arr[idx-1]+1):
            return(arr[idx-1]+1)
        
# Problem 2: function to find zeroes in matrix and set respective row,col to 0
def set_zero(mat):
    columns = len(mat[0])
    rows = len(mat)
    pos = [] # empty list for storing zero positions
    
    for i in range(0,rows*columns):
        
        # iterate matrix values
        row = i // columns
        col = i % columns
        
        # save positions of zeroes
        if(mat[row][col] == 0):
            pos.append([row,col])

    # iterate through position pairs (row,col)
    for pair in pos:
        
        row = pair[0]
        col = pair[1]
        
        # set those rows and columns to zero
        mat[row] = [0]*columns
        for i in range(0, rows):
            mat[i][col] = 0
        
    return mat

# Problem 3: function to find the middle of a singly LinkedList (using llist library)
def find_middle(llist):
    
    # Set two pointers to the first value in LinkedList
    p1 = p2 = llist.first
    
    # While p2 has two more values ahead of it, move p1 forward 1 and p2 forward 2
    while((p2.next is not None) and (p2.next.next is not None)):
        p1 = p1.next
        p2 = p2.next.next
    
    # p1 will stop halfway, return p1
    return p1.value

if __name__ == "__main__":
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # Problem 1: Missing Number
    # Determine the missing number in a sequential list of numbers.
    
    # Sample sequential array
    arr = []
    length = 10000
    for i in range(length):
        arr.append(i)
    arr[randint(1,length-1)] = 0

    
    # Timing
    start = time.time_ns()
    result = missing_number(arr)
    end = time.time_ns()
    
    print("* * * * * PROBLEM 1 * * * * *")
    print(f"The missing number is {result} and the total time is {(end-start)} ns.\n")
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # Problem 2: Zero Matrix
    # If an element in an M*N matrix is 0, set its entire row and column to 0.
    #
    # NOTE: can either do retroactively (do not take into account new zeroes) or 
    # sequentially (take new zeroes into account)

    arr = [
        [0,1,5,4,3],
        [4,3,6,0,8],
        [3,2,6,3,1]
    ]

    print("* * * * * PROBLEM 2 * * * * *")
    print(f"The given matrix is:\n{arr}\nand the resulting matrix is:")
    
    # Timing
    start = time.time_ns()
    result = set_zero(arr)
    end = time.time_ns()
    
    print(f"{result}\nand the total time is {(end-start)*1000} ns.\n")
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # Problem 3: Middle of LinkedList
    # Get the element in the middle of a LinkedList in a single pass.

    llist = pyllist.sllist([0,1,2,3,4,5,6])

    print("* * * * * PROBLEM 3 * * * * *")
    print(f"The given LinkedList is:\n{llist}")
    
    # Timing
    start = time.time_ns()
    result = find_middle(llist)
    end = time.time_ns()
    
    print(f"and the middle value is {result}\nand the total time is {(end-start)*1000} ns.\n")
    
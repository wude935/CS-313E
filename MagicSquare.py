#  File: MagicSquare.py
#  Description:
#  Student's Name: Derek
#  Student's UT EID: DW
#  Partner's Name:
#  Partner's UT EID:
#  Course Name: CS 313E
#  Unique Number:
#  Date Created:
#  Date Last Modified:

# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]


def make_square(n):
    x = (n-1)//2  # Initial value is the middle coordinate of specified square
    y = n - 1  # Initial value is always n - 1
    count = 1
    # Creates a n x n grid with the value 'blank' in each element.
    # The upper leftmost corner is coordinate (0,0) and the lower rightmost corner is coordinate (n, n)
    grid = [['blank' for i in range(n)] for j in range(n)]
    for k in range(n * n):
        grid[y][x] = count
        new_x = x + 1
        new_y = y + 1
        if new_x > n - 1:  # Catches values that go out right
            new_x = 0
        if new_y > n - 1:  # Catches values that go too far down
            new_y = 0
        if grid[new_y][new_x] != 'blank':  # Prevents overwriting
            new_x = x
            new_y = y - 1
        x = new_x
        y = new_y
        count += 1
    return grid


# Print the magic square in a neat format where the numbers
# are right justified
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6

def print_square(magic_square):

    for row in magic_square:
        # Converts rows intro strings
        print(' '.join(str(number) for number in row))


# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True


def check_square(magic_square):
    is_magic = True
    n = len(magic_square)  # Gets length of input
    known_square = make_square(n)  # creates reference square for comparison

    for i in range(n):
        y = i - 1
        for j in range(n):
            x = j - 1
            # Checks input vs reference square
            if not is_magic or magic_square[y][x] != known_square[y][x]:
                is_magic = False
    return is_magic


def main():
    n = 0
    while(n % 2 == 0):  # Catches any even numbers and reprompts user
        print('Please enter an odd number')
        n = int(input())
    magic_square = make_square(n)
    print_square(magic_square)
    print('Is this a magic square?', check_square(magic_square))


# Prompt the user to enter an odd number 1 or greater
3
# Check the user input

# Create the magic square

# Print the magic square

# Verify that it is a magic square


# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
# if __name__ == "__main__":
main()

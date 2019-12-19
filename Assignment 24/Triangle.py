import time


# returns the greatest path sum using exhaustive search
def exhaustive_search(grid):
    return

# returns the greatest path sum using greedy approach


def greedy(grid):
    return

# returns the greatest path sum using divide and conquer (recursive) approach


def rec_search(grid):
    # stores all the results of rec_search_helper
    res_list = []
    rec_search_helper(grid, 0, res_list)
    return (max(res_list))

# helper function that finds the path with the largest sum using recursion


def rec_search_helper(grid, res, res_list):
    grid_len = len(grid)
    # base case
    if grid_len == 1:
        res_list.append(res + grid[0][0])
    else:
        left_grid = []
        right_grid = []
        # creates two subtriangles, one to the left and one to the right
        for i in range(1, grid_len):
            left_grid.append(grid[i][:-1])
            # print(left_grid)
            right_grid.append(grid[i][1:])
            # adds the top of the subtriangle
        res += grid[0][0]
        return rec_search_helper(left_grid, res, res_list) or rec_search_helper(right_grid, res, res_list)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    # sets up the memo
    memo = []
    grid_len = len(grid)
    for i in range(grid_len):
        memo.append([])
    return dynamic_prog_helper(grid, memo)
    

# helper function that finds the path witht he largest sum using dynamic programming
def dynamic_prog_helper(grid, memo):
    grid_len = len(grid)
    # sets up the memo for the last row
    for i in range(len(grid[-1])):
        memo[-1].append(grid[-1][i])
    # uses dynamic programming to find the largest sum    
    # goes through every row in the grid
    for i in reversed(range(grid_len - 1)):
        # goes through every element in a row
        for j in range(len(grid[i])):
            left_sum = j
            right_sum = j + 1
            # updates the memo by choosing the larger previous sum either to the left and right and adds it to the existing value 
            memo[i].append(grid[i][j] + max(memo[i + 1][left_sum], memo[i + 1][right_sum]))
    return memo[0][0]

# # reads the file and returns a 2-D list that represents the triangle
# def read_file():
#     return


def main():
    grid = []
    # read triangular grid from file
    in_file = open("./triangle.txt", "r")
    num_rows = int(in_file.readline().strip())
    for i in range(num_rows):
        grid.append(list(map(int, in_file.readline().strip().split())))
    print(grid)

    print(rec_search(grid))

    ti = time.time()
    # output greates path from exhaustive search
    tf = time.time()
    del_t = tf - ti
    # print time taken using exhaustive search

    ti = time.time()
    # output greates path from greedy approach
    tf = time.time()
    del_t = tf - ti
    # print time taken using greedy approach

    ti = time.time()
    # output greates path from divide-and-conquer approach
    tf = time.time()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach

    ti = time.time()
    # output greates path from dynamic programming
    tf = time.time()
    del_t = tf - ti
    # print time taken using dynamic programming
    print(dynamic_prog(grid))


if __name__ == "__main__":
    main()

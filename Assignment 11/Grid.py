# counts all the possible paths in a grid recursively
def count_paths(n, row, col):
    # if the square is to the right-most col or the bottom row then make it 1
    if row == n-1 or col == n-1:
        return 1
    # adds numbers to top and right to find the path
    else:
        return count_paths(n, row + 1, col) + count_paths(n, row, col + 1)


# recursively gets the greatest sum of all the paths in the grid
def path_sum(grid, n, row, col):
    # base case if you are on the bottom right most square
    if row == n - 1 and row == n-1:
        return grid[row][col]
    # adds the numbers to the right if you are on the bottom row
    elif row == n-1:
        return grid[row][col] + path_sum(grid, n, row, col + 1)
    # adds the numbers to the top if you are on the right-most row
    elif col == n-1:
        return grid[row][col] + path_sum(grid, n, row + 1, col)
    # adds the number either from the right to the bottom, whichever is larger
    else:
        return grid[row][col] + max(path_sum(grid, n, row + 1, col), path_sum(grid, n, row, col + 1))

# gets the path of the greatest sum path
output = []
def get_path(grid, n, row, col):
    #print('print', grid[row][col])
    # base case if you are on the bottom right most square, appends square to output
    if row == n - 1 and row == n-1:
        output.append(grid[row][col])
    # appends square to output and calls function on next square to the right
    elif row == n-1:
        output.append(grid[row][col])
        get_path(grid, n, row, col + 1)
    # appends square to output and calls the function on the next square to the top
    elif col == n-1:
        output.append(grid[row][col])
        get_path(grid, n, row + 1, col)
    # appends and calls function on whichever square to the right or top is larger
    else:
        if path_sum(grid, n, row + 1, col) > path_sum(grid, n, row, col + 1):
            output.append(grid[row][col])
            get_path(grid, n, row + 1, col)
        else:
            output.append(grid[row][col])
            get_path(grid, n, row, col + 1)
    return output


def main():
    # open file for reading
    in_file = open("grid.txt", "r")

    # read the dimension of the grid
    dim = in_file.readline()
    dim = dim.strip()
    dim = int(dim)

    # create an empty grid
    grid = []

    # populate the grid
    for i in range(dim):
        line = in_file.readline()
        line = line.strip()
        row = line.split()
        for j in range(dim):
            row[j] = int(row[j])
        grid.append(row)

    # close the file
    in_file.close()

    # get the number of paths in the grid and print
    num_paths = count_paths(dim, 0, 0)
    print('Number of paths in a grid of dimension', dim, 'is', num_paths)
    print()

    # get the maximum path sum and print
    max_path_sum = path_sum(grid, dim, 0, 0)
    print('Greatest path sum is', max_path_sum)
    print()

    # get the path
    path = get_path(grid, dim, 0, 0)
    print('Actual Path is', path)


main()

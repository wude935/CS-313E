def search(grid, target):
    lo = 0
    hi = len(grid) - 1
    while (lo <= hi):
        mid = (lo + hi)//2
        rowLength = len(grid[mid])
        loRowValue = grid[mid][0]
        hiRowValue = grid[mid][rowLength - 1]
        if target > hiRowValue:
            lo = mid + 1
        elif target < loRowValue:
            hi = mid - 1
        elif target >= loRowValue and target <= hiRowValue:
            return searchRow(grid[mid], target)
    return False


def searchRow(row, target):
    lo = 0
    hi = len(row) - 1
    while (lo <= hi):
        mid = (lo + hi)//2
        if target > row[mid]:
            lo = mid + 1
        elif target < row[mid]:
            hi = mid - 1
        else:
            return True
    return False


def main():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    print(search(grid, 13))


main()

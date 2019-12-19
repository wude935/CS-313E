#  File: Queens.py

#  Description: Finds all possible solutions for a n queens on a n x n board

#  Student Name: Derek Wu

#  Student UT EID: dw29924

#  Partner Name: Victor Li

#  Partner UT EID: vql83

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/21/19

#  Date Last Modified: 10/21/19

num_solutions = 0

class Queens (object):
    # initialize the board
    def __init__(self, n=8):
        self.board = []
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()

    # check if no queen captures another
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do a recursive backtracking solution
    def recursive_solve(self, col):
        global num_solutions
        result = False
        if (col == self.n):
            num_solutions += 1
            self.print_board()
            print()
            return True
        else:
            for i in range(self.n):
                if (self.is_valid(i, col)):
                    self.board[i][col] = 'Q'

                    if (self.recursive_solve(col + 1)):
                        result = True
                    self.board[i][col] = '*'

            return result


def main():
    board_size = 0
    while not (board_size >= 1 and board_size <= 8):  # Catches any numbers larger then 8 and smaller than 1 and reprompts user
        board_size = int(input('Enter size of the board: '))
    # create a regular chess board
    game = Queens(board_size)
    print()
    if game.recursive_solve(0) == False:
      print('No solutions exist for this board')
    else:
      print('There are', num_solutions, 'solutions for a', board_size, 'x', board_size, 'board')



main()

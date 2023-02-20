""" This class represents a single Sudoku's puzzle board.
You can initialize an object of this class with initial values for the Sudoku's cells, along with the empty cells that
need to be solved.
To solve the Sudoku, call the 'solve()' method. This method returns 'True' if the puzzle has been solved successfully.

Author:     Din Ezra     dinezra11@gmail.com
"""


class Sudoku:
    def __init__(self, board):
        """ Initialize the sudoku's object.
        The object has a matrix for the puzzle board, and another matrix for the possibilities of values for each cell.
        Also, the object also holds the amount of empty cells. When this value is zero - the sudoku is solved!

        :param board:       9x9 sudoku board.
                            Empty cells are indicated by zeros.
        """
        self.board = board
        self.options = list(list(set(range(1, 10)) for _ in range(9)) for _ in range(9))
        self.emptyCells = 9 * 9  # If zero - the puzzle is solved!
        
    def removeOption(self, row, col, value):
        """ Remove the possibility of the 'value' digit to appear in the given row, given cell, and given sub-box.

        :param row:     Row index.
        :param col:     Column index.
        :param value:   Value of digit to remove the possibility for.
        """
        # Remove value from row and column
        for i in range(len(self.board)):
            self.options[row][i].discard(value)
            self.options[i][col].discard(value)

        # Remove value from the corresponding 3x3 sub-box.
        rowBox, colBox = row // 3, col // 3
        for i in range(rowBox * 3, rowBox * 3 + 3):
            for j in range(colBox * 3, colBox * 3 + 3):
                self.options[i][j].discard(value)

    def solve(self):
        """ Solve the sudoku puzzle.

        :return:         True if success, false if failed.
        """
        while self.emptyCells != 0:
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if len(self.options[i][j]) == 0:
                        continue
                    elif len(self.options[i][j]) == 1:
                        value = self.options[i][j].pop()
                        self.board[i][j] = value
                        self.removeOption(i, j, value)

                        self.emptyCells -= 1
                    elif self.board[i][j] != 0:
                        self.removeOption(i, j, self.board[i][j])
                        self.options[i][j].clear()

                        self.emptyCells -= 1
        return True
   
    def printBoardToConsole(self, printOpt=False):
        """ Print the sudoku board to the console. Also print the options matrix if needed.
        This function is for debugging purposes.

        :param printOpt:       Boolean. Indicates if the options matrix should be printed also.
        """

        def printMatrix(matrix):
            """ Print matrix in board form. """
            for i in range(len(matrix)):
                if i % 3 == 0:
                    print("- - - - - - - - - - - - -")

                row = "| "
                for j in range(len(matrix[0])):
                    row += str(matrix[i][j]) + " "

                    if (j + 1) % 3 == 0:
                        row += "| "
                print(row)

            print("- - - - - - - - - - - - -")

        printMatrix(self.board)
        print()
        if printOpt:
            printMatrix(self.options)

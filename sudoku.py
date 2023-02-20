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

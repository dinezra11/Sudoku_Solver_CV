# Sudoku_Solver_CV
Using Computer Vision techniques, extract a Sudoku board from a given photo and automatically show the solution.
I will be using the following python libraries in my project: numpy, opencv, pytesseract, tkinter.

The project consists of 4 phases:
1. Developing the Sudoku Solver class: Implement an algorithm that gets a 9x9 integer matrix that represents a single Sudoku's board as an input, and returns the final solution of the given board.
Of course that an error will occur if the given board is illegal or could not be solved.
2. Board extraction from a given photo: Given any picture, I need to use computer-vision techniques in order to successfully extract the board from it. I will be using opencv library for that purpose.
3. Digit Recognition: After we have the Sudoku's board extracted from the original picture, we need to divide and extract each cell from the board so we can identify which digit it represents (or empty). I will need to use some pre-processing techniques in order to have a good accuracy from the predictions of the model. For the model, I will use the OCR (Optical Character Recognition) library pytesseract.
4. GUI: Using tkinter, create a friendly GUI so the user will be able to easily upload any picture to the application, and get automatically get the solution.

Hope you will enjoy my code! Any suggesstion will be appreciated.
Din - dinezra11@gmail.com

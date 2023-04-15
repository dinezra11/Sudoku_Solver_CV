# Sudoku_Solver_CV
Using Computer Vision techniques, extract a Sudoku board from a given photo and automatically show the solution.
I will be using the following python libraries in my project: numpy, opencv, tensorflow, tkinter.

The project consists of 4 phases:
1. Developing the Sudoku Solver class: Implement an algorithm that gets a 9x9 integer matrix that represents a single Sudoku's board as an input, and returns the final solution of the given board.
Of course that an error will occur if the given board is illegal or could not be solved.
2. Board extraction from a given photo: Given any picture, I need to use computer-vision techniques in order to successfully extract the board from it. I will be using opencv library for that purpose.
3. Digit Recognition: After we have the Sudoku's board extracted from the original picture, we need to divide and extract each cell from the board so we can identify which digit it represents (or empty). I will need to use some pre-processing techniques in order to have a good accuracy from the predictions of the model. I will use a pre-trained deep learning model to classify the digits from the image.
4. GUI: Using tkinter, create a friendly GUI so the user will be able to easily upload any picture to the application, and get automatically get the solution.

## How to run the program
To run the program, please make sure that you have all of the necessary packages installed in your environment.
All of the packages are listed in the file "requirements.txt", so you can simply install them with the command "pip install -r requirements.txt".
After everything is installed - run "main.py" script and the program will start.

## Using the program
The program is friendly and easy to use. You just need to load the image you want to analyze, then click on "Solve!", and the sudoku's solution will appear on the output frame (right side of the screen)!

Hope you will enjoy my code! Any suggesstion will be appreciated.
Din - dinezra11@gmail.com

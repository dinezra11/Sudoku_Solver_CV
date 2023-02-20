""" Image analyze. This file is in charge of extracting the Sudoku board from the imported image, splitting the cells
and make digit recognition for the board's initial state.
After the digit recognition, save and return an array of the given Sudoku puzzle for further processing.
Use the function 'getSudoku()' to get the array representation of the puzzle from the given image.

**  Library used for image processing is OpenCV.

Author:     Din Ezra     dinezra11@gmail.com
"""
import cv2 as cv
import numpy as np

IMAGE_SIZE = 450 # Define a constant for the image resizing in the pre-processing stage


def preProcessing(originalImg):
    """ Pre-processing of the imported image.

    :param originalImg:         The loaded image.
    :return:                    A new image, after pre-processing.
    """
    originalImg = cv.resize(originalImg, (IMAGE_SIZE, IMAGE_SIZE))
    newImg = cv.cvtColor(originalImg, cv.COLOR_BGR2GRAY)
    newImg = cv.GaussianBlur(newImg, (3, 3), 6)
    newImg = cv.adaptiveThreshold(newImg, 255, 1, 1, 11, 2)

    return newImg


def extractPuzzle(img):
    """ Find the biggest contours in the image, and use it as the Sudoku's board.

    :param img:         The pre-processed image.
    :return:            A new image, consisting only the Sudoku part extracted from the original image.
    """

    def sortPoints(pointsArr):
        """ Sort the given points, so they will be in the appropriate format for drawing and processing.

        :param pointsArr:       Array of 4 points.
        :return:                Sorted array. -> [top_left, top_right, bottom_left, bottom_right]
        """
        # Initialize helper variables
        pointsArr = pointsArr.reshape((4, 2))
        add = pointsArr.sum(1)
        sortedPoints = np.zeros((4, 2), dtype=np.int32)

        # Sort the points to the appropriate order
        sortedPoints[0] = pointsArr[np.argmin(add)]
        sortedPoints[3] = pointsArr[np.argmax(add)]
        diff = np.diff(pointsArr, axis=1)
        sortedPoints[1] = pointsArr[np.argmin(diff)]
        sortedPoints[2] = pointsArr[np.argmax(diff)]

        # Return the sorted array of points
        return sortedPoints

    # Find contours and get the biggest one (it will be the Sudoku's board)
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # We only care about the contours
    biggest = max(contours, key=cv.contourArea)

    # Get the approximation of the 4 points that construct the rectangle shape of the board.
    points = []
    epsilon = 0.08
    while len(points) != 4:
        # Loop until the biggest contour is represented by 4 points
        points = cv.approxPolyDP(biggest, epsilon * cv.arcLength(biggest, True), True)
        epsilon /= 2 # Improve the 'guess' for the next iteration, if needed..

    # Sort the 4 points that we got from the above lines of code
    points = sortPoints(points)

    # Crop the Sudoku board part from the original image
    board = np.float32(points)
    original = np.float32([[0, 0], [IMAGE_SIZE, 0], [0, IMAGE_SIZE], [IMAGE_SIZE, IMAGE_SIZE]])
    transformedMatrix = cv.getPerspectiveTransform(board, original)

    # Return the image of the Sudoku puzzle only
    croppedBoard = cv.warpPerspective(img, transformedMatrix, (IMAGE_SIZE, IMAGE_SIZE))
    return croppedBoard


def loadImage(path):
    """ Get a path to the given Sudoku's board, analyze it and represent it as a 2D-array.

    :param path:        The path to the image.
    :return:            2D array representing the Sudoku's board.
    """
    img = cv.imread(path) # Load the image
    img = preProcessing(img) # Pre-process the image
    img = extractPuzzle(img) # Extract the Sudoku's board from the image

    ### TESTING
    cv.imshow("test", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


loadImage("example2.png")

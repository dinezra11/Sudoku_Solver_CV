""" Image analyze. This file is in charge of extracting the Sudoku board from the imported image, splitting the cells
and make digit recognition for the board's initial state.
After the digit recognition, save and return an array of the given Sudoku puzzle for further processing.
Use the function 'getSudoku()' to get the array representation of the puzzle from the given image.

**  Library used for image processing is OpenCV.

Author:     Din Ezra     dinezra11@gmail.com
"""
import cv2 as cv
import numpy as np
import tensorflow as tf

IMAGE_SIZE = 450 # Define a constant for the image resizing in the pre-processing stage
MODELINPUT_SIZE = 48 # The size of an individual image that the model expects to get as an input


def preProcessing(originalImg):
    """ Pre-processing of the imported image.

    :param originalImg:         The loaded image.
    :return:                    A new image, after pre-processing.
    """
    originalImg = cv.resize(originalImg, (IMAGE_SIZE, IMAGE_SIZE))
    newImg = cv.cvtColor(originalImg, cv.COLOR_BGR2GRAY)
    newImg = cv.GaussianBlur(newImg, (3, 3), 6)
    newImg = cv.adaptiveThreshold(newImg, 255, 1, 1, 11, 2)

    return originalImg, newImg


def extractPuzzle(img, processedImg):
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
    contours, hierarchy = cv.findContours(processedImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # We only care about the contours
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


def digitRecognition(img):
    """ Split the cells from the Sudoku's image and use a pre-trained deep learning model
    to make predictions for the digits.

    :param img:         Image of the Sudoku's board.
    :return:            2D array representing the Sudoku's board, after the digit classification.
    """

    # Load pre-trained model and pre-process image
    model = tf.keras.models.load_model("DigitRecognitionModel.h5")
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Extract the cells coordination from the full image
    cells = []
    for row in np.vsplit(img, 9):
        for col in np.hsplit(row, 9):
            col = cv.resize(col, (MODELINPUT_SIZE, MODELINPUT_SIZE)) / 255.0
            cells.append(col)
    cells = np.array(cells).reshape((-1, MODELINPUT_SIZE, MODELINPUT_SIZE, 1))

    # Call the model and get the predictions for the digits
    predictions = model.predict(cells)
    results = []
    for p in predictions:
        index = np.argmax(p)
        results.append(index)

    results = np.array(results).astype("uint8").reshape(9, 9).tolist()

    return results, img


def drawDigitsOnTop(baseImg, board):
    """ Draw the given board's values on top of the image. """
    offset = IMAGE_SIZE // 9
    for i in range(9):
        for j in range(9):
            if board[j][i] != 0:
                cv.putText(baseImg, str(board[j][i]), (offset*i+7, offset*(j+1)-8), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,0))

    return baseImg


def loadImage(path):
    """ Get a path to the given Sudoku's board, analyze it and represent it as a 2D-array.

    :param path:        The path to the image.
    :return:            2D array representing the Sudoku's board, and the image of the board (extracted from the
                        original image).
    """
    img = cv.imread(path) # Load the image
    img, processedImg = preProcessing(img) # Pre-process the image
    img = extractPuzzle(img, processedImg) # Extract the Sudoku's board from the image
    result, img = digitRecognition(img)

    return result, img

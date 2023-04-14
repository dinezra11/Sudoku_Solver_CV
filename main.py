""" Main script for the project!
Using tkinter library, the application will initialize and load the interface.



Author:     Din Ezra     dinezra11@gmail.com
"""
from customtkinter import *
from tkinter import filedialog as fd
from PIL import Image
from time import sleep

import imageAnalyze
from sudoku import Sudoku

IMAGESIZE = (350, 350) # Constant


def initializeWindow():
    def headerFrame():
        """ Initialize the title frame. """
        frame = CTkFrame(root)
        CTkLabel(frame, text="Sudoku Solver", font=(None, 36)).pack()
        CTkLabel(frame, text="using Computer Vision", font=(None, 12)).pack()

        return frame

    def footerFrame():
        """ Initialize the credits and information frame. """
        frame = CTkFrame(root)
        CTkLabel(frame, text="Application developed by Din Ezra for educational purposes only.").pack(pady=0)
        CTkLabel(frame, text="Any comment will be appreciated :)").pack()
        CTkLabel(frame, text="dinezra11@gmail.com").pack()

        return frame

    def inputFrame(parent, solveFunc):
        """ Initialize the user-input frame.

        :param parent:          The parent frame for this frame.
        :param solveFunc        The solving function from the output frame.
        :return                 The frame's object.
        """

        def loadFile():
            types = (
                ('Image File', ('*.png', '*.jpeg', '*.jpg', '*.gif', '*.tiff')),
            )
            loadedImg = fd.askopenfilename(filetypes=types)

            if loadedImg not in (None, "", " "):
                lblImage.configure(text="", image=CTkImage(Image.open(loadedImg), size=IMAGESIZE))
                btnSolve.configure(command=lambda: solveFunc(loadedImg))

        def clear():
            lblImage.configure(text="", image=emptyImage)
            btnSolve.configure(command=None)

        frame = CTkFrame(parent)
        emptyImage = CTkImage(Image.new("RGBA", IMAGESIZE, (255, 0, 0, 0)), size=IMAGESIZE)

        lblTitle = CTkLabel(frame, text="Load an Image as an Input")
        lblImage = CTkLabel(frame, text="", image=emptyImage)

        # Buttons Frame
        buttonsFrame = CTkFrame(frame)
        btnClear = CTkButton(buttonsFrame, text="Clear", command=clear)
        btnLoad = CTkButton(buttonsFrame, text="Load an Image", command=loadFile)
        btnSolve = CTkButton(buttonsFrame, text="Solve!", command=None)
        btnClear.grid(row=0, column=0, padx=10, pady=5)
        btnLoad.grid(row=0, column=1, padx=10, pady=5)
        btnSolve.grid(row=0, column=2, padx=10, pady=5)

        # Pack Frame
        lblTitle.pack()
        lblImage.pack()
        buttonsFrame.pack(pady=10)

        return frame

    def outputFrame(parent):
        """ Initialize the output frame.

        :param parent:          The parent frame for this frame.
        :return                 The frame's object and a pointer to the solving function, so
                                it can be accessed from the input frame.
        """

        def solve(imgPath):
            # Reset progress bar
            progress.stop()
            progress.configure(mode="determinate")
            progress.set(0)
            frame.update()

            # Analyze image (Board extraction)
            lblStatus.configure(text="Analyzing image..")
            frame.update()
            a, b = imageAnalyze.loadImage(imgPath)
            lblImage.configure(image=CTkImage(Image.fromarray(b), size=IMAGESIZE))

            # Attempt to solve the sudoku
            progress.set(0.5)
            lblStatus.configure(text="Solving sudoku..")
            frame.update()
            sleep(1)
            puzzle = Sudoku(a)

            print(puzzle.solve())
            puzzle.printBoardToConsole()

            # Done
            progress.set(1)
            lblStatus.configure(text="Done.")

        frame = CTkFrame(parent)
        lblTitle = CTkLabel(frame, text="Solution Generator (Output)")
        lblImage = CTkLabel(frame, text="", image=CTkImage(Image.new("RGBA", IMAGESIZE, (255, 0, 0, 0)), size=IMAGESIZE))
        lblStatus = CTkLabel(frame, text='Load an image and click on "Solve!" to start..')
        progress = CTkProgressBar(frame, orientation="horizontal", mode="indeterminate")
        progress.start()

        # Pack Frame
        lblTitle.pack()
        lblImage.pack()
        lblStatus.pack(pady=(10, 0))
        progress.pack()

        return frame, solve

    def applicationFrame():
        """ Initialize the application frame.
        This frame is basically a merge between the input frame and the output frame.
        """
        padx, pady = 10, 10
        frame = CTkFrame(root)
        outFrame, solveFunc = outputFrame(frame)
        inFrame = inputFrame(frame, solveFunc)

        outFrame.pack(padx=padx, pady=pady, fill="both", side="right", expand=True)
        inFrame.pack(padx=padx, pady=pady, fill="both", side="left", expand=True)

        return frame

    # Window Settings
    set_appearance_mode("dark")
    set_default_color_theme("green")
    root = CTk()
    root.title("Sudoku Solver CV - by Din Ezra")
    w, h = 1200, 650
    x, y = root.winfo_screenwidth() / 2 - w / 2, root.winfo_screenheight() / 2 - h / 2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.resizable(False, False)

    # Main Frame Settings
    headerFrame().pack(padx=90, pady=(15, 25), fill="both", expand=False)
    applicationFrame().pack(padx=90, fill="both", expand=True)
    footerFrame().pack(padx=30, pady=5, fill="both", side="bottom", expand=False)

    return root


def main():
    root = initializeWindow()
    root.mainloop()


if __name__ == "__main__":
    main()

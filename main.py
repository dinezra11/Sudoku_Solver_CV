""" Main script for the project!
Using tkinter library, the application will initialize and load the interface.



Author:     Din Ezra     dinezra11@gmail.com
"""
from customtkinter import *
from tkinter import filedialog as fd
from PIL import Image


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

    def inputFrame(parent):
        """ Initialize the user-input frame.

        :param parent:          The parent frame for this frame.
        """

        def loadFile():
            types = (
                ('Image File', ('*.png', '*.jpeg', '*.jpg', '*.gif', '*.tiff')),
            )
            loadedImg = fd.askopenfilename(filetypes=types)

            if loadedImg not in (None, "", " "):
                lblImage.configure(text="", image=CTkImage(Image.open(loadedImg), size=imageSize))

        def clear():
            lblImage.configure(text="", image=emptyImage)

        frame = CTkFrame(parent)
        imageSize = (350, 350)
        emptyImage = CTkImage(Image.new("RGBA", imageSize, (255, 0, 0, 0)), size=imageSize)

        lblTitle = CTkLabel(frame, text="Input Example")
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
        """
        frame = CTkFrame(parent)
        CTkLabel(frame, text="Output Example").pack()

        return frame

    def applicationFrame():
        """ Initialize the application frame.
        This frame is basically a merge between the input frame and the output frame.
        """
        padx, pady = 10, 10
        frame = CTkFrame(root)
        inputFrame(frame).pack(padx=padx, pady=pady, fill="both", side="left", expand=True)
        outputFrame(frame).pack(padx=padx, pady=pady, fill="both", side="right", expand=True)

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

from customtkinter import *


def initializeWindow():
    # Window Settings
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    root = CTk()
    root.title("Sudoku Solver CV - by Din Ezra")
    w, h = 1200, 650
    x, y = root.winfo_screenwidth() / 2 - w / 2, root.winfo_screenheight() / 2 - h / 2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.resizable(False, False)

    # Main Frame Settings
    frame = CTkFrame(root)
    frame.pack(pady=15, padx=90, fill="both", expand=True)
    CTkLabel(frame, text="Sudoku Solver", font=(None, 36)).pack()
    CTkLabel(frame, text="using Computer Vision", font=(None, 12)).pack()

    return root, frame


def main():
    root, frameMain = initializeWindow()
    root.mainloop()


if __name__ == "__main__":
    main()

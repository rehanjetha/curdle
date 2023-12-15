import tkinter
from tkinter import ttk
import sys

class Panel(tkinter.Tk):
    """Curdle Configuration Panel made with Tkinter"""

    def __init__(self):
        """Initialize Panel Class"""
        super().__init__()  # inherit tkinter root & its methods

        # Class Variables
        self.__bg = "#343541"  # panel background colour
        self.__fg = "#FFFFFF"  # text foreground colour
        self.__size = "600x300"  # panel dimensions

        # Window Pre-Configuration
        self.title("Cu-rdle Configuration Panel")  # set panel name
        self.geometry(f"{self.__size}")  # set panel size
        self.resizable(False, False)  # prevent window resizing
        self.configure(bg=self.__bg)  # set background colour
        self.protocol("WM_DELETE_WINDOW", self.close)  # close entire pgm when closed

        self.create_widgets()  # create & place all widgets


    def create_widgets(self):
        """Method to create & place all widgets"""

        # Use TTK Style Widgets
        style = ttk.Style(self)  # use TTK styles on root
        style.configure("TButton", background=self.__bg)  # set bg for buttons
        style.configure("TLabel", foreground=self.__fg, background=self.__bg)  # set bg & fg for buttons

        # Tkinter Variables
        diff_var = tkinter.IntVar()  # difficulty variable
        ai_var = tkinter.BooleanVar()  # ai boolean variable

        # Panel Labels
        intro_label = ttk.Label(self, text="Welcome to CU-RDLE", font=("Open Sans", 18))  # title header
        diff_label = ttk.Label(self, text="Difficulty: ")  # difficulty label
        wrd_len_label = ttk.Label(self, text="Word Length: ")  # word length label
        guess_label = ttk.Label(self, text="Guess Amount: ")  # guesses label

        # Panel Buttons
        norm_radio = ttk.Radiobutton(self, text="Normal", variable=diff_var, value=1)  # normal difficulty
        hard_radio = ttk.Radiobutton(self, text="Hard", variable=diff_var, value=2)  # hard difficulty
        insane_radio = ttk.Radiobutton(self, text="Insane", variable=diff_var, value=3)  # insane difficulty
        ai_check = ttk.Checkbutton(self, text="AI Mode", variable=ai_var)  # ai button
        wrd_len_spin = ttk.Spinbox(self, from_=3, to=6)  # word length spinbox
        guess_spin = ttk.Spinbox(self, from_=3, to=10)  # guess amt spinbox
        start_button = ttk.Button(self, text="Start")  # start
        how_button = ttk.Button(self, text="Tutorial Video")  # tutorial

        # Default Word Length
        wrd_len_spin.insert(0, 5)  # set 5 to default word length

        # Default Guess Amount
        guess_spin.insert(0, 6)  # set 6 to default guess amt

        # Grid Layout
        intro_label.grid(row=0, column=2)  # place intro header

        diff_label.grid(row=1, column=0)
        norm_radio.grid(row=1, column=2)
        hard_radio.grid(row=1, column=3)
        insane_radio.grid(row=1, column=4)

        wrd_len_label.grid(row=2, column=0)
        wrd_len_spin.grid(row=2, column=2)

        guess_label.grid(row=3, column=0)
        guess_spin.grid(row=3, column=2)

        start_button.grid(row=4, column=4)
        ai_check.grid(row=5, column=0)
        how_button.grid(row=6, column=0)


    @staticmethod
    def close():
        """Static Method: Close PGM"""
        sys.exit()  # close entire program


    def get_bg(self):
        """Accessor Method: Panel Background"""
        return self.__bg
    

    def get_fg(self):
        """Accessor Method: Buttons' Foreground"""
        return self.__fg


    def get_size(self):
        """Accessor Method: Panel Size"""
        return self.__size
    

    def set_size(self, length, width):
        """Mutator Method: Panel Size"""
        new_size = f"{length}x{width}"
        self.__size = new_size


pan = Panel()
pan.mainloop()  
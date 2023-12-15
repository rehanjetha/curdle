import json
import sys
import tkinter
from tkinter import messagebox, ttk

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
        self.__diff_var = tkinter.IntVar()  # difficulty variable
        self.__ai_var = tkinter.BooleanVar()  # ai boolean variable
        self.__wrd_var = tkinter.IntVar()  # word length variable
        self.__guess_var = tkinter.IntVar()  # guess length variable

        # Default Word Length
        self.__wrd_var.set(5)

        # Default Guess Amount
        self.__guess_var.set(6)

        # Panel Labels
        intro_label = ttk.Label(self, text="Welcome to CU-RDLE", font=("Open Sans", 18))  # title header
        diff_label = ttk.Label(self, text="Difficulty: ")  # difficulty label
        wrd_len_label = ttk.Label(self, text="Word Length: ")  # word length label
        guess_label = ttk.Label(self, text="Guess Amount: ")  # guesses label

        # Panel Buttons
        norm_radio = ttk.Radiobutton(self, text="Normal", variable=self.__diff_var, value=1)  # normal difficulty
        hard_radio = ttk.Radiobutton(self, text="Hard", variable=self.__diff_var, value=2)  # hard difficulty
        insane_radio = ttk.Radiobutton(self, text="Insane", variable=self.__diff_var, value=3)  # insane difficulty
        ai_check = ttk.Checkbutton(self, text="AI Mode", variable=self.__ai_var)  # ai button
        self.__wrd_len_spin = ttk.Spinbox(self, from_=3, to=6, textvariable=self.__wrd_var)  # word length spinbox
        self.__guess_spin = ttk.Spinbox(self, from_=3, to=10, textvariable=self.__guess_var)  # guess amt spinbox
        start_button = ttk.Button(self, text="Start", command=self.start)  # start
        how_button = ttk.Button(self, text="Tutorial Video", command=self.video)  # tutorial

        # Panel Layout
        intro_label.grid(row=0, column=2, pady=(0, 20))  # place intro header

        diff_label.grid(row=2, column=0, sticky="w")
        norm_radio.grid(row=2, column=2, sticky="w")
        hard_radio.grid(row=2, column=3, sticky="w")
        insane_radio.grid(row=2, column=4, sticky="w")

        wrd_len_label.grid(row=3, column=0, sticky="w")
        self.__wrd_len_spin.grid(row=3, column=2)

        guess_label.grid(row=4, column=0, sticky="w")
        self.__guess_spin.grid(row=4, column=2)

        start_button.grid(row=5, column=4)
        ai_check.grid(row=6, column=0)
        how_button.grid(row=7, column=0)

    def start(self):
        """Method to perform value checks & start game"""

        # Determine Difficulty
        if (self.__diff_var.get() == 1):
            diff = "Normal"
        elif (self.__diff_var.get() == 2):
            diff = "Hard"
        elif (self.__diff_var.get() == 3):
            diff = "Insane"
        else:
            messagebox.showerror('Difficulty Error', 'Error: Please choose a difficulty')
            return

        # Ensure Valid Values
        try:
            int(self.__wrd_var.get())
        except:
            messagebox.showerror('Word Length Error', 'Error: Please choose a valid word length')
            return
        try:
            int(self.__guess_var.get())
        except:
            messagebox.showerror('Guess Length Error', 'Error: Please choose a valid guess length')
            return
        
        # Check Values' Domain
        if (3 <= self.__wrd_var.get() <= 6):
            word_len = self.__wrd_var.get()
        else:
            messagebox.showinfo('Invalid Word Length', 'Defaulting to Word Length of 5')
            word_len = 5
        if (3 <= self.__guess_var.get() <= 10):
            guess_len = self.__guess_var.get()
        else:
            messagebox.showinfo('Invalid Guess Length', 'Defaulting to Guess Length of 6')
            guess_len = 6

        # Use/Not Use AI
        if (self.__ai_var.get() == True):
            use_ai = True
        else:
            use_ai = False

        # Write Data to JSON
        game_settings = {
            "difficulty": diff,
            "wordLength": word_len,
            "guessLength": guess_len,
            "AIMode": use_ai
        }
        with open("Database/config.json", "w") as config_file:
            json.dump(game_settings, config_file, indent=4)
        messagebox.showinfo('Launching Curdle', "The game will begin momentarily")
        self.close()

    def video(self):
        """Method to play tutorial video"""
        pass


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


    def set_bg(self, new_bg):
        """Mutator Method: Set Background"""
        self.__bg = new_bg


pan = Panel()
pan.mainloop()  
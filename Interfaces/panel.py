import json
from tkinter import messagebox, ttk
import customtkinter as ctk

class Panel(ctk.CTk):
    """Curdle Configuration Panel made with ctk"""

    def __init__(self):
        """Initialize Panel Class"""
        super().__init__()  # inherit ctk root & its methods

        # Class Variables
        self.__bg = "#343541"  # panel background colour
        self.__fg = "#FFFFFF"  # text foreground colour
        self.__size = "600x300"  # panel dimensions


        # Window Pre-Configuration
        self.title("Cu-rdle Configuration Panel")  # set panel name
        self.geometry(f"{self.__size}")  # set panel size
        self.configure(bg=self.__bg)  # set background colour
        self.create_widgets()  # create & place all widgets


    def create_widgets(self):
        """Method to create & place all widgets"""

        # ctk Variables
        self.__diff_var = ctk.IntVar()  # difficulty variable
        self.__ai_var = ctk.StringVar(value="on")  # ai boolean variable
        self.__wrd_var = ctk.IntVar()  # word length variable
        self.__guess_var = ctk.IntVar()  # guess length variable
        self.__how_var = ctk.StringVar(value="on")  # tutorial variable

        # Default Word Length
        self.__wrd_var.set(5)

        # Default Guess Amount
        self.__guess_var.set(6)

        # Panel Labels
        intro_label = ctk.CTkLabel(self, text="Welcome to CU-RDLE", font=("Open Sans", 18))  # title header
        diff_label = ctk.CTkLabel(self, text="Difficulty: ")  # difficulty label
        wrd_len_label = ctk.CTkLabel(self, text="Word Length: ")  # word length label
        guess_label = ctk.CTkLabel(self, text="Guess Amount: ")  # guesses label

        # Panel Buttons
        norm_radio = ctk.CTkRadioButton(self, text="Normal", variable=self.__diff_var, value=1)  # normal difficulty
        hard_radio = ctk.CTkRadioButton(self, text="Hard", variable=self.__diff_var, value=2)  # hard difficulty
        insane_radio = ctk.CTkRadioButton(self, text="Insane", variable=self.__diff_var, value=3)  # insane difficulty
        ai_check = ctk.CTkSwitch(self, text="AI Mode", variable=self.__ai_var, onvalue="on", offvalue="off")  # ai button
        word_len_spin = ttk.Spinbox(self, from_=3, to=6, textvariable=self.__wrd_var)  # word length spinbox
        guess_spin = ttk.Spinbox(self, from_=3, to=10, textvariable=self.__guess_var)  # guess amt spinbox
        start_button = ctk.CTkButton(self, text="Start", command=self.start)  # start
        how_button = ctk.CTkSwitch(self, text="Tutorial Video", variable=self.__how_var, onvalue="on", offvalue="off")  # tutorial

        # Panel Layout
        intro_label.grid(row=0, column=2, pady=(0, 50))  # place intro header

        diff_label.grid(row=2, column=0, sticky="w")
        norm_radio.grid(row=2, column=1, sticky="w")
        hard_radio.grid(row=2, column=2, sticky="w")
        insane_radio.grid(row=2, column=3, sticky="w")

        wrd_len_label.grid(row=3, column=0, sticky="w")
        word_len_spin.grid(row=3, column=2)

        guess_label.grid(row=4, column=0, sticky="w")
        guess_spin.grid(row=4, column=2)

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
            messagebox.showerror('Difficulty Error', 'Error: Please choose a difficulty')  # error
            return  # do not start

        # Ensure Valid Values
        try:
            int(self.__wrd_var.get())
        except:
            messagebox.showerror('Word Length Error', 'Error: Please choose a valid word length')  # error
            return  # do not start
        try:
            int(self.__guess_var.get())
        except:
            messagebox.showerror('Guess Length Error', 'Error: Please choose a valid guess length')  # error
            return  # do not start

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

        # Show/Don't Show Tutorial
        if (self.__how_var.get() == "on"):
            show_tuto = True
        else:
            show_tuto = False

        # Use/Not Use AI
        if (self.__ai_var.get() == "on"):
            use_ai = True
        else:
            use_ai = False

        # Write Data to JSON
        game_settings = {
            "difficulty": diff,
            "wordLength": word_len,
            "guessLength": guess_len,
            "tutorial": show_tuto,
            "AIMode": use_ai
        }
        with open("Database/config.json", "w") as config_file:
            json.dump(game_settings, config_file, indent=4)
        messagebox.showinfo('Launching Curdle', "The game will begin momentarily")

    def video(self):
        """Method to play tutorial video"""
        pass

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
import customtkinter as ctk
import json
import sys
from tkinter import messagebox


class Panel(ctk.CTk):
    """Curdle Configuration Panel made with CTK"""

    def __init__(self):
        """Initialize Panel Class"""
        super().__init__()  # inherit ctk root & its methods

        # Class Variables
        self.__size = "450x215"  # panel dimensions

        # Window Pre-Configuration
        self.title("Curdle Game Setup")  # set panel name
        self.geometry(self.__size)  # set panel size
        ctk.set_appearance_mode('dark')  # set dark mode
        ctk.set_default_color_theme('blue')  # set blue theme
        self.resizable(width=False, height=False)  # disable resizing
        self.create_widgets()  # create & place all widgetsdef on_closing():
        self.protocol("WM_DELETE_WINDOW", sys.exit)  # close entire pgm if config closed


    def create_widgets(self):
        """Method to create & place all widgets"""

        # ctk Variables
        self.__diff_var = ctk.IntVar()  # difficulty variable
        self.__ai_var = ctk.StringVar(value="off")  # ai boolean variable
        self.__guess_var = ctk.IntVar()  # guess length variable
        self.__wrd_var = ctk.IntVar()  # word length variable
        self.__how_var = ctk.StringVar(value="on")  # tutorial variable

        # Defaut Difficulty
        self.__diff_var.set(1)

        # Default Word Length
        self.__wrd_var.set(5)

        # Default Guess Amount
        self.__guess_var.set(6)

        # Panel Labels
        intro_label = ctk.CTkLabel(self, text="Welcome to Curdle!", font=("Open Sans", 18))  # title header
        guess_label = ctk.CTkLabel(self, text="Guesses: ")  # guesses label
        guess_val_label = ctk.CTkLabel(self, textvariable=self.__guess_var)  # guess len display
        wrd_len_label = ctk.CTkLabel(self, text="Word Length: ")  # word length label
        wrd_val_label = ctk.CTkLabel(self, textvariable=self.__wrd_var) # word len val display

        # Panel Buttons
        norm_radio = ctk.CTkRadioButton(self, text="Normal", variable=self.__diff_var, value=1)  # normal difficulty
        hard_radio = ctk.CTkRadioButton(self, text="Hard Mode", variable=self.__diff_var, value=2)  # hard difficulty
        insane_radio = ctk.CTkRadioButton(self, text="Insane", variable=self.__diff_var, value=3)  # insane difficulty
        guess_slide = ctk.CTkSlider(self, from_=3, to=10, variable=self.__guess_var)  # guess amt spinbox
        wrd_len_slide = ctk.CTkSlider(self, from_=3, to=6, variable=self.__wrd_var)  # word length spinbox
        ai_check = ctk.CTkSwitch(self, text="AI Mode", variable=self.__ai_var, onvalue="on", offvalue="off")  # ai switch   
        start_button = ctk.CTkButton(self, text="Start", command=self.start)  # start
        how_button = ctk.CTkSwitch(self, text="Tutorial Video", variable=self.__how_var, onvalue="on", offvalue="off")  # tutorial switch

        # Panel Layout
        intro_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))
        norm_radio.grid(row=1, column=0, padx=(15, 0), pady=(0, 10))
        hard_radio.grid(row=1, column=1, pady=(0, 10))
        insane_radio.grid(row=1, column=2, pady=(0, 10))
        guess_label.grid(row=3, column=0, pady=(0, 10))
        guess_slide.grid(row=3, column=1, pady=(0, 10))
        guess_val_label.grid(row=3, column=2, pady=(0, 10))
        wrd_len_label.grid(row=4, column=0, pady=(0, 10))
        wrd_len_slide.grid(row=4, column=1, pady=(0, 10))
        wrd_val_label.grid(row=4, column=2, pady=(0, 10))
        start_button.grid(row=5, column=1)
        ai_check.grid(row=5, column=0)
        how_button.grid(row=5, column=2)


    def start(self):
        """Method to perform value checks & start game"""

        # Determine Difficulty
        diff_values = {1: "Normal", 2: "Hard", 3: "Insane"}
        diff = diff_values.get(self.__diff_var.get(), None)

        if (diff == None):  # if default set doesn't work
            messagebox.showerror('Difficulty Error', 'Error: Please choose a difficulty')  # error
            return  # do not start
        
        # Fetch Widget Values
        word_len = self.__wrd_var.get()
        guess_len = self.__guess_var.get()
        show_tuto = (self.__how_var.get() == "on")
        use_ai = (self.__ai_var.get() == "on")

        # Make JSON Format
        game_settings = {
            "difficulty": diff,
            "wordLength": word_len,
            "guessLength": guess_len,
            "tutorial": show_tuto,
            "AIMode": use_ai
        }

        # Write to game_settings to JSON
        try:
            with open("Database/config.json", "w") as config_file:
                json.dump(game_settings, config_file, indent=4)
            messagebox.showinfo('Launching Curdle', "The game will begin momentarily")
            self.destroy()  # close panel
        except:
            messagebox.showerror('Missing CONFIG Folder', 'Error: Missing Database Folder. Closing program.')
            sys.exit()  # fatal error

    def get_size(self):
        """Accessor Method: Panel Size"""
        return self.__size  # return panel size


    def set_size(self, length, width):
        """Mutator Method: Panel Size"""
        new_size = f"{length}x{width}"  # new panel size
        self.__size = new_size  # change panel size
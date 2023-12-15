import tkinter as tk

def get_number():
    number = spinbox.get()
    result_label.config(text=f"Selected Number: {number}")

# Create the main window
root = tk.Tk()
root.title("Number Selection Example")

# Spinbox widget for numerical input
spinbox = tk.Spinbox(root, from_=0, to=100)
spinbox.pack(pady=10)

# Button to get the selected number
get_number_button = tk.Button(root, text="Get Number", command=get_number)
get_number_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

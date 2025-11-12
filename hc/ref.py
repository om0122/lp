# --- HCI (Human-Computer Interface) Practical Reference File ---
#
# This single file is a complete, runnable Python script using Tkinter.
# Tkinter is Python's built-in, standard library for creating GUIs (Graphical User Interfaces).
# You do NOT need the internet for this. It works with a standard Python installation.
#
# HOW TO USE:
# 1. Save this file as 'hci_practical.py'.
# 2. Open your terminal or command prompt (NOT in WSL if you're on Windows).
# 3. Navigate to the folder where you saved it (e.g., 'cd Desktop').
# 4. Run it with: python hci_practical.py
#
# This script will create a window that demonstrates all the core concepts.
# Read the comments to understand how each part works.
# ---

# --- 1. IMPORTING ---
# We import the 'tkinter' library. We also import 'ttk' (themed tkinter),
# which provides more modern-looking widgets (buttons, labels, etc.).
import tkinter as tk
from tkinter import ttk

# --- 2. THE "ACTION" FUNCTIONS ---
# It's good practice to define the functions (the "actions") first.
# These functions are "called" by our widgets (like a button click).

def handle_button_click():
    """
    This function is triggered when 'greet_button' is clicked.
    It performs the core HCI task:
    1. GET data from a widget (the 'name_entry' box).
    2. PROCESS the data.
    3. OUTPUT data to another widget (the 'result_label').
    """
    # 1. GET: Use the .get() method to read the text from the entry box.
    user_name = name_entry.get()

    # 2. PROCESS: Check if the user_name is empty.
    if not user_name:
        user_name = "World"  # Provide a default value

    # 3. OUTPUT: Use the .config() method to change the 'text' property
    #    of the result_label.
    greeting = f"Hello, {user_name}! Welcome to HCI."
    result_label.config(text=greeting)

def clear_text_box():
    """
    This function clears the multi-line text box.
    It shows how to interact with a 'Text' widget.
    """
    # To delete from a Text widget, you specify a start and end point.
    # '1.0' means line 1, character 0.
    # 'tk.END' means the very end of the text.
    info_text_box.delete('1.0', tk.END)
    info_text_box.insert('1.0', "Text cleared!")


# --- 3. THE MAIN APPLICATION SETUP ---

# --- A. Create the Main Window ---
# This is the root or "main window" of your application.
# All other widgets will live inside this 'window'.
window = tk.Tk()
window.title("HCI Practical Reference")
window.geometry("500x450")  # Set a starting size (Width x Height)

# --- B. Create a Frame to Hold Content ---
# A 'Frame' is an invisible container used to group other widgets.
# This is the best way to organize your layout.
main_frame = ttk.Frame(window, padding="10")  # 'padding="10"' adds 10px of space
main_frame.pack(fill='both', expand=True) # .pack() is one way to place things.

# --- C. The Layout System: .grid() ---
# We will use the '.grid()' system inside 'main_frame'.
# This system lets you place widgets in a table (rows and columns).
# We "configure" the columns to make them stretchable.
main_frame.columnconfigure(1, weight=1) # Make column 1 (the entry boxes) stretch

# --- 4. CREATING & PLACING WIDGETS ---
# A "Widget" is any UI element (button, label, text box).
#
# The pattern is always:
# 1. Create the widget (e.g., `my_button = ttk.Button(...)`)
# 2. Place the widget (e.g., `my_button.grid(...)`)
#
# --- Row 0: Name Label and Entry ---
# ttk.Label: A widget that displays static text.
name_label = ttk.Label(main_frame, text="Enter Your Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky='w') # sticky='w' (west) aligns it left

# ttk.Entry: A widget for a single line of user text input.
name_entry = ttk.Entry(main_frame, width=40)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew') # sticky='ew' (east-west) stretches it

# --- Row 1: The Button ---
# ttk.Button: A widget that the user clicks to trigger an action.
# The 'command' property is set to the *name* of the function to run.
greet_button = ttk.Button(main_frame, text="Greet Me", command=handle_button_click)
greet_button.grid(row=1, column=1, padx=5, pady=5, sticky='e') # sticky='e' (east) aligns it right

# --- Row 2: The Result Label ---
# This label starts empty and will be updated by our 'handle_button_click' function.
result_label = ttk.Label(main_frame, text="...waiting for a greeting...", font=("Helvetica", 12))
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10) # 'columnspan=2' makes it span both columns

# --- Row 3: Separator ---
# A visual line to separate sections.
separator = ttk.Separator(main_frame, orient='horizontal')
separator.grid(row=3, column=0, columnspan=2, sticky='ew', pady=10)

# --- Row 4: Multi-line Text Box ---
# tk.Text: A widget for multi-line text input/output. (Note: This one is 'tk', not 'ttk')
text_label = ttk.Label(main_frame, text="Multi-line Text Box:")
text_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')

info_text_box = tk.Text(main_frame, height=8, width=50)
info_text_box.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

# We can pre-fill the text box using .insert()
info_text_box.insert(tk.END, "This is a Text widget. It can hold multiple lines.\n")
info_text_box.insert(tk.END, "The button above will 'get' from the 'Entry' and 'config' the label.\n")

# --- Row 6: Another Button ---
# This button will call our 'clear_text_box' function.
clear_button = ttk.Button(main_frame, text="Clear Text Box", command=clear_text_box)
clear_button.grid(row=6, column=1, padx=5, pady=5, sticky='e')


# --- 5. START THE APPLICATION ---
# 'window.mainloop()' is the *last* line you call.
# It tells Tkinter to draw the window and "listen" for user events
# (like mouse clicks or key presses) until the user closes the window.
window.mainloop()

# --- End of Reference File ---

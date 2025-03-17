import tkinter as tk

# Function to handle button clicks
def on_click(button_text):
    current_text = entry.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Function to toggle themes
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode  # Switch theme state

    if dark_mode:
        root.config(bg="#1e1e1e")
        entry.config(bg="#333", fg="white", insertbackground="white")
        theme_button.config(text="Light Mode", bg="#444", fg="white")

        for btn in buttons_list:
            btn.config(bg="#555", fg="white", activebackground="#777")
    else:
        root.config(bg="white")
        entry.config(bg="white", fg="black", insertbackground="black")
        theme_button.config(text="Dark Mode", bg="lightgray", fg="black")

        for btn in buttons_list:
            btn.config(bg="lightgray", fg="black", activebackground="darkgray")

# Create the main window
root = tk.Tk()
root.title("Themed Calculator")

# Initial theme state
dark_mode = False
root.config(bg="white")

# Entry field for input and results
entry = tk.Entry(root, width=20, font=("Arial", 18), justify="right", bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Theme Toggle Button
theme_button = tk.Button(root, text="Dark Mode", command=toggle_theme, bg="lightgray", fg="black", font=("Arial", 12))
theme_button.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=5)

# Calculator buttons
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

# List to store button references
buttons_list = []

# Add buttons to the window
for r, row in enumerate(buttons, start=2):
    for c, text in enumerate(row):
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), bg="lightgray",
                        fg="black", activebackground="darkgray", command=lambda t=text: on_click(t))
        btn.grid(row=r, column=c)
        buttons_list.append(btn)

# Run the Tkinter event loop
root.mainloop()
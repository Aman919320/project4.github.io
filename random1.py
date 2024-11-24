import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Keep the clipboard content
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Length input
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Password output
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()

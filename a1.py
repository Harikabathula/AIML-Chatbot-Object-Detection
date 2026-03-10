import tkinter as tk

# Create main window
window = tk.Tk()
window.title("My First Tkinter App")
window.geometry("400x300")

# Create a label
label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# Button click function
def on_click():
    label.config(text="Button Clicked!")

# Create a button
button = tk.Button(window, text="Click Me", command=on_click)
button.pack()

# Run the application
window.mainloop()

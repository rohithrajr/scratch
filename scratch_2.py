import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Add a label to the window
label = tk.Label(root, text="Hello, Tkinter!", font=("TkDefaultFont", 20))
label.pack()

# Start the GUI event loop
root.mainloop() 
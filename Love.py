import tkinter as tk

def display_message():
    message_label.config(text="I LOVE YOU")

# Create the main window
root = tk.Tk()
root.title("Love Message")

# Create a label widget to display the message with a larger font size
message_label = tk.Label(root, text="", font=("Helvetica", 36))

# Create a button to trigger the message display
display_button = tk.Button(root, text="I ❤️ U", command=display_message)

# Pack the widgets
message_label.pack(pady=20)
display_button.pack()

# Start the GUI main loop
root.mainloop()

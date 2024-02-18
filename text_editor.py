import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


# Function to open a file and populate the text editor
def open_file(window, text_edit):
    # Ask the user to select a file
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    # If the user cancels the file selection, do nothing
    if not filepath:
        return
    
    # Clear the existing content in the text editor
    text_edit.delete(1.0,tk.END)

    # Read the content from the selected file and insert it into the text editor
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)

    # Set the window title to display the opened file's path
    window.title(f"Open File: {filepath}")
 
# Function to save the content of the text editor to a file
def save_file(window, text_edit):
    # Ask the user to select a file to save the content
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    # If the user cancels the file selection, do nothing
    if not filepath:
        return
    
    # Write the content of the text editor to the selected file
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)

    # Set the window title to display the saved file's path
    window.title(f"Open File: {filepath}")

# Main function to create the GUI and handle user interactions
def main():
    # Create the main window
    window = tk.Tk()
    window.title("Text Editor with Python")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    # Create a text editor widget
    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)

    # Create a frame to hold the save and open buttons
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text= "Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text= "Open", command=lambda: open_file(window, text_edit))

    # Place the buttons in the frame and the frame in the window
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    # Bind keyboard shortcuts for saving and opening files
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    # Start the main event loop
    window.mainloop()

# Call the main function to run the text editor
main()
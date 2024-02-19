import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename


# Function to open a file and populate the text editor
def open_file(window, text_edit):
    """
    Open a file and populate the text editor.

    Parameters:
        window (tk.Tk): The main window.
        text_edit (tk.Text): The text editor widget.

    Raises:
        FileNotFoundError: If the selected file is not found.
        Exception: For any other unexpected errors during file opening.
    """

    # Ask the user to select a file
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    # Check if a file path has been selected
    if filepath:
        try:
            # Attempt to open the selected file in read mode
            with open(filepath, "r") as f:
                # Read the content of the file
                content = f.read()

                 # Clear the existing content in the text editor
                text_edit.delete(1.0, tk.END)

                # Insert the content of the file into the text editor
                text_edit.insert(tk.END, content)

            # Update the window title to indicate the opened file    
            window.title(f"Open File: {filepath}")

        # Handle exceptions that may occur during file opening and display an error message using a message box    
        except Exception as e:
            messagebox.showerror("Error", f"Error opening file: {str(e)}")
 
# Function to save the content of the text editor to a file
def save_file(window, text_edit):
    """
    Save the content of the text editor to a file.

    Parameters:
        window (tk.Tk): The main window.
        text_edit (tk.Text): The text editor widget.

    Raises:
        PermissionError: If permission is denied to write to the selected file.
        Exception: For any other unexpected errors during file saving.
    """

    # Ask the user to select a file to save the content
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    # Check if a file path has been selected
    if filepath:
        try:
            # Attempt to open the selected file in write mode
            with open(filepath, "w") as f:
                # Retrieve the content from the text editor
                content = text_edit.get(1.0, tk.END)

                # Write the content to the selected file
                f.write(content)

            # Update the window title to indicate the saved file    
            window.title(f"Save File: {filepath}")

        # Handle exceptions that may occur during file saving and display an error message using a message box    
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {str(e)}")

# Function to close the program
def close_program(window):
    """
    Close the program with user confirmation.

    Parameters:
        window (tk.Tk): The main window.
    """
    
    if messagebox.askokcancel("Close Program", "Are you sure you want to close the program?"):
        window.destroy()

# Main function to create the GUI and handle user interactions
def main():
    """
    Create the GUI for the text editor and handle user interactions.
    """

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
    close_button = tk.Button(frame, text="Close", command=lambda: close_program(window))

    # Place the buttons in the frame and the frame in the window
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")
    close_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    # Bind keyboard shortcuts for saving and opening files
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    # Start the main event loop
    window.mainloop()

# Call the main function to run the text editor
main()
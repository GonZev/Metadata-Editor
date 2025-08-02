import tkinter as tk
from ui_app import AppUI

if __name__ == "__main__":
    # --- Setup the main window ---
    root = tk.Tk()
    root.title("Audio Metadata Editor")
    root.geometry("600x720")

    # --- Create the UI ---
    # This creates an instance of our AppUI class,
    # which builds the user interface.
    app_ui = AppUI(root)

    # --- Start the application ---
    # This starts the Tkinter event loop, which waits for user actions.
    root.mainloop()

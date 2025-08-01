from tkinter import filedialog
import os


class AppFunctions:
    def __init__(self, root):
        self.root = root

    def select_mp3_file(self):
        file = filedialog.askopenfilename(
            filetypes=[("Archivos MP3", "*.mp3")])
        if file:
            # this value is to use in ENTRY FILE NAME
            self.path_mp3 = file
            return self.path_mp3
            # this value, use in LABEL MP3
            # self.label_mp3 = os.path.basename(file)
        return None

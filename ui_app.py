import tkinter as tk
from function_app import AppFunctions


class AppUI:
    def __init__(self, root):
        self.root = root
        # Create an instance of the functions class
        self.functions = AppFunctions(self.root)

        # --- VARS ---

        # --- Functions ---

        def select_cover_album(self):
            return 0

        def save(self):
            return 0

        # --- UI Elements ---
        label_title = tk.Label(root, text="Edit Audio Metadata",
                               font=('Arial', 34))
        label_title.pack(pady=20)

        button_select_song = tk.Button(
            root, font='12',
            text="Seleccionar canción MP3",
            command=self.on_select_mp3)

        button_select_song.pack(pady=5, padx=22, anchor='w')

        self.file_name = tk.Label(
            root,
            text='Nombre de archivo',
            font='14').pack()

        self.label_mp3 = tk.Label(
            root, text="Archivo no seleccionado", font='12')
        self.label_mp3.pack()

        self.entry_file_name = tk.Entry(root, width=30)
        self.entry_file_name.pack()

        tk.Label(root, text="Título", font='14').pack()

        self.entry_titulo = tk.Entry(root, width=30)
        self.entry_titulo.pack()

        tk.Label(root, text="Artista", font='14').pack()

        self.entry_artista = tk.Entry(root, width=30)
        self.entry_artista.pack()

        tk.Label(root, text="Álbum", font='14').pack()

        self.entry_album = tk.Entry(root, width=30)
        self.entry_album.pack()

        tk.Button(
            root,
            text="Seleccionar portada (JPG)",
            font='14',
            command=select_cover_album).pack(pady=5)

        self.label_portada = tk.Label(
            root,
            text="Imagen no seleccionada",
            font='12')
        self.label_portada.pack()

        tk.Button(root,
                  text='Guardar medatata',
                  command=save).pack()

    def on_select_mp3(self):
        mp3_file = self.functions.select_mp3_file()
        if mp3_file:
            self.label_mp3.config(text=mp3_file)

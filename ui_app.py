import tkinter as tk
import os

from function_app import AppFunctions

from PIL import Image, ImageTk


class AppUI:
    def __init__(self, root):
        self.root = root
        self.root.configure(background='gainsboro')
        # Create an instance of the functions class
        self.functions = AppFunctions(self.root)

        # --- UI Elements ---

        label_title = tk.Label(
            root,
            text="Edit Audio Metadata",
            font=('Arial bold', 34, 'bold'),
            bg='gainsboro'
        )
        label_title.pack(pady=20, padx=50, anchor='w')

        button_select_song = tk.Button(
            root, font='12',
            text="Select file",
            command=self.on_select_mp3
        )
        button_select_song.pack(pady=5, padx=50, anchor='w')

        self.file_name = tk.Label(
            root,
            text='Name of file',
            font='14',
            bg='gainsboro'
        ).pack(padx=50, anchor='w')

        self.entry_file_name = tk.Entry(
            root, width=50)
        self.entry_file_name.pack(padx=50, anchor='w')

        tk.Label(root, text="Title", font='14',
                 bg='gainsboro').pack(padx=50, anchor='w')

        self.entry_titulo = tk.Entry(root, width=50)
        self.entry_titulo.pack(padx=50, anchor='w')

        frame_artist = tk.Frame(root)
        frame_artist.pack(padx=50, anchor='w')

        tk.Label(frame_artist, text="Artist", font='14',
                 bg='gainsboro').pack(anchor='w', side='left')

        self.check_var_artista = tk.BooleanVar()
        check_artist = tk.Checkbutton(frame_artist, text="Don't delete",
                                      variable=self.check_var_artista)
        check_artist.pack(side="left", anchor="w")

        self.entry_artista = tk.Entry(root, width=50)
        self.entry_artista.pack(padx=50, anchor='w')

        frame_album = tk.Frame(root)
        frame_album.pack(padx=50, anchor='w')

        tk.Label(frame_album, text="Album", font='14',
                 bg='gainsboro').pack(anchor='w', side='left')

        self.check_var_album = tk.BooleanVar()
        check_album = tk.Checkbutton(frame_album, text="Don't delete",
                                     variable=self.check_var_album)
        check_album.pack(side="left", anchor="w")

        self.entry_album = tk.Entry(root, width=50)
        self.entry_album.pack(padx=50, anchor='w')

        frame_date = tk.Frame(root)
        frame_date.pack(padx=50, anchor='w')

        tk.Label(frame_date, text="Date (only year)", font='14',
                 bg='gainsboro').pack(anchor='w', side='left')

        self.check_var_date = tk.BooleanVar()
        check_date = tk.Checkbutton(frame_date, text="Don't delete",
                                    variable=self.check_var_date)
        check_date.pack(side="left", anchor="w")

        self.entry_date = tk.Entry(root, width=50)
        self.entry_date.pack(padx=50, anchor='w')

        frame_cover = tk.Frame(root)
        frame_cover.pack(padx=50, anchor='w')
        tk.Button(
            frame_cover,
            text="Select cover",
            font='14',
            command=self.select_cover_album).pack(pady=10, anchor='w', side='left')

        self.check_var_cover = tk.BooleanVar()
        check_cover = tk.Checkbutton(frame_cover, text="Don't delete",
                                     variable=self.check_var_cover)
        check_cover.pack(side="left", anchor="w")

        self.label_portada = tk.Label(
            root,
            text="Image no selected",
            font='12',
            bg='gainsboro'
        )
        self.label_portada.pack(padx=50, anchor='w')

        tk.Button(root,
                  text='Save',
                  font='Arial 14 bold',
                  command=self.save,
                  width=100, height=2,
                  bg='green', fg='white').pack(padx=50, pady=20)

    # --- Functions to buttons ---

    def on_select_mp3(self):
        self.clear_entries()

        mp3_file = self.functions.select_mp3_file()
        if mp3_file:
            self.entry_file_name.insert(0, mp3_file)
            self.entry_titulo.insert(0, os.path.basename(mp3_file))

    def select_cover_album(self):
        path_cover, label_cover = self.functions.select_cover_album()
        # # Cargar imagen desde archivo (puede ser jpg, png, etc.)
        image = Image.open(path_cover)
        image = image.resize((200, 200))  # opcional: redimensionar
        photo = ImageTk.PhotoImage(image)
        self.label_portada.config(image=photo, text='')
        self.label_portada.image = photo

    def save(self):
        self.functions.save_metadata(
            self.entry_file_name.get(),
            self.entry_titulo.get(),
            self.entry_artista.get(),
            self.entry_album.get(),
            self.entry_date.get()
        )
        # CLEAR ENTRIES
        self.clear_entries()

    def clear_entries(self):
        self.entry_file_name.delete(0, tk.END)
        self.entry_titulo.delete(0, tk.END)
        if not self.check_var_artista.get():
            self.entry_artista.delete(0, tk.END)
        if not self.check_var_album.get():
            self.entry_album.delete(0, tk.END)
        if not self.check_var_date.get():
            self.entry_date.delete(0, tk.END)
        if not self.check_var_cover.get():
            self.label_portada.configure(text='Imagen no seleccionada')

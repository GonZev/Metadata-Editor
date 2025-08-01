import tkinter as tk
from tkinter import filedialog, messagebox
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, error
import os


class MetadataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Metadata Editor")

        self.ruta_mp3 = ""
        self.ruta_portada = ""

        # Widgets
        tk.Label(root, text="Edit Audio Metadata",
                 font=('Arial', 34)).pack(pady=30)

        tk.Button(root, font='12', text="Seleccionar canción MP3",
                  command=self.seleccionar_mp3).pack(pady=5,
                                                     padx=22, anchor='w')

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

        tk.Button(root, text="Seleccionar portada (JPG)", font='14',
                  command=self.seleccionar_portada).pack(pady=5)

        self.label_portada = tk.Label(
            root, text="Imagen no seleccionada", font='12')
        self.label_portada.pack()

        tk.Button(root, text='Guardar medatata',
                  command=self.guardar_metadata).pack()

    def seleccionar_mp3(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("Archivos MP3", "*.mp3")])
        if archivo:
            self.ruta_mp3 = archivo
            self.label_mp3.config(text=os.path.basename(archivo))
            self.entry_file_name.insert(0, self.ruta_mp3)
            self.entry_titulo.insert(0, os.path.basename(archivo))

    def seleccionar_portada(self):
        imagen = filedialog.askopenfilename(
            filetypes=[("Imágenes JPG", "*.jpg")])
        if imagen:
            self.ruta_portada = imagen
            self.label_portada.config(text=os.path.basename(imagen))

    def guardar_metadata(self):
        if not self.ruta_mp3:
            messagebox.showerror("Error", "Primero selecciona un archivo MP3.")
            return
        file_name = self.entry_file_name.get()
        titulo = self.entry_titulo.get()
        artista = self.entry_artista.get()
        album = self.entry_album.get()

        try:
            try:
                audio = EasyID3(self.ruta_mp3)
            except error.ID3NoHeaderError:
                audio = EasyID3()
                audio.save(self.ruta_mp3)
                audio = EasyID3(self.ruta_mp3)

            audio["title"] = titulo
            audio["artist"] = artista
            audio["album"] = album
            audio.save()

            # change file name
            os.rename(self.ruta_mp3, file_name)

              audio_id3 = ID3(self.ruta_mp3)
               with open(self.ruta_portada, "rb") as img:
                    audio_id3["APIC"] = APIC(
                        encoding=3,
                        mime="image/jpeg",
                        type=3,
                        desc="Cover",
                        data=img.read()
                    )
                audio_id3.save()

            messagebox.showinfo("Éxito", "Metadata guardada correctamente.")

            # CLEAR ENTRIES
            self.entry_file_name.delete(0, tk.END)
            self.entry_titulo.delete(0, tk.END)
            self.entry_artista.delete(0, tk.END)
            self.entry_album.delete(0, tk.END)
            self.label_mp3.config(text='Archivo no seleccionado', font=14)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x600')
    app = MetadataApp(root)
    root.mainloop()

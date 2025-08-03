from tkinter import filedialog, messagebox
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, error
import os
import mimetypes


class AppFunctions:
    def __init__(self, root):
        self.root = root
        self.path_cover = ''

    def select_mp3_file(self):
        self.path_mp3 = ''
        file = filedialog.askopenfilename(
            filetypes=[("Archivos MP3", "*.mp3")])
        if file:
            # this value is to use in ENTRY FILE NAME
            self.path_mp3 = file
            return self.path_mp3
        return None

    def select_cover_album(self):
        self.path_cover = ''
        self.label_cover = ''
        image = filedialog.askopenfilename(
            filetypes=[('Imágenes JPG', "*.jpg")]
        )
        if image:
            self.path_cover = image
            self.label_cover = os.path.basename(image)
            return self.path_cover, self.label_cover
        return None, None

    def save_metadata(
        self,
        entry_file_name,
        entry_title,
        entry_artist,
        entry_album,
            entry_date):
        if not self.path_mp3:
            messagebox.showerror('Error', 'Primero selecciona un archivo MP3.')
            return
        file_name = entry_file_name
        title = entry_title
        artist = entry_artist
        album = entry_album
        date = entry_date

        try:
            try:
                audio = EasyID3(self.path_mp3)
            except error.ID3NoHeaderError:
                audio = EasyID3()
                audio.save(self.path_mp3)
                audio = EasyID3(self.path_mp3)

            if title:
                audio['title'] = title
            if artist:
                audio['artist'] = artist
            if album:
                audio['album'] = album
            if album:
                audio['date'] = date
            audio.save()

            # change file name
            os.rename(self.path_mp3, file_name)
            if self.path_cover:
                audio_id3 = ID3(self.path_mp3)
                mime_type = mimetypes.guess_type(self.path_cover)
                img_type = 'image/jpeg'
                if mime_type[0]:
                    img_type = mime_type[0]
                for key in list(audio_id3.keys()):
                    if key.startswith('APIC'):
                        del audio_id3[key]
                with open(self.path_cover, 'rb') as img:
                    audio_id3['APIC'] = APIC(
                        encoding=3,
                        mime=img_type,
                        type=3,
                        desc='Cover',
                        data=img.read()
                    )
                audio_id3.save()
            messagebox.showinfo('Éxito', 'Metadata guardada correctamente.')
        except Exception as e:
            messagebox.showerror('Error', f"Ocurrió un error: {str(e)}")

import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame

class MusicPlayer:
    def __init__(self, window):
        self.window = window
        self.window.title("Music Player")
        self.window.geometry("400x300")

        self.current_file = None
        self.paused = False

        self.label = tk.Label(window, text="Music Player")
        self.label.pack()

        self.btn_select = tk.Button(window, text="Select Song", command=self.select_song)
        self.btn_select.pack()

        self.btn_play_pause = tk.Button(window, text="Play", command=self.play_pause)
        self.btn_play_pause.pack()

        self.volume_slider = ttk.Scale(window, from_=0, to=100, orient="horizontal", command=self.set_volume)
        self.volume_slider.pack()
        self.volume_slider.set(50)  # Initial volume set to 50

        self.song_listbox = tk.Listbox(window)
        self.song_listbox.pack()

    def select_song(self):
        self.current_file = filedialog.askopenfilename(initialdir="/", title="Select Song",
                                                       filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
        if self.current_file:
            pygame.mixer.init()
            pygame.mixer.music.load(self.current_file)
            self.song_listbox.insert(tk.END, os.path.basename(self.current_file))

    def play_pause(self):
        if self.current_file:
            if not pygame.mixer.music.get_busy() or self.paused:
                pygame.mixer.music.play()
                self.btn_play_pause.config(text="Pause")
                self.paused = False
            else:
                pygame.mixer.music.pause()
                self.btn_play_pause.config(text="Play")
                self.paused = True

    def set_volume(self, value):
        volume = int(value) / 100
        pygame.mixer.music.set_volume(volume)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

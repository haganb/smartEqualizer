import tkinter as tk
from tkinter import filedialog
from config import config
import firm
import pygame
import os

# SMART EQUALIZER 
# University of Delaware Fall-Spring 2021
# Hagan Beatson, Alex Chacko, Ryan Lenihan, Michael Richards
# ELEG/CPEG 498/499

class menu:
    def __init__(self, config):
        # Menu setup
        pygame.mixer.init() # initialize media player
        self.pause_toggle = True
        self.config = config
        self.window = tk.Tk()

        self.pauseText = tk.StringVar()
        self.pauseText.set("Pause")
        self.playText = tk.StringVar()
        self.playText.set("Play")

        self.songName = tk.StringVar()
        self.songName.set("None")
        self.pathToSong= ""

        self.currentProfile = tk.StringVar()
        self.currentProfile.set("Predictive")

        self.window.title('Smart Equalizer')
        self.build_main_menu()
        self.window.mainloop()
        
    def build_main_menu(self):
        info_frame = tk.Frame(master=self.window)
        button_frame = tk.Frame(master=self.window)
        control_frame = tk.Frame(master=self.window)

        # info frame setup
        greeting = tk.Label(
            text="Smart Equalizer",
            font=("Times", 24, "bold"),
            master=info_frame
        )
        greeting.pack(side=tk.TOP)

        profile_label = tk.Label(
            text="Current profile configuration:",
            font=("Times", 12),
            master=info_frame
        )
        profile_label.pack()

        profile_status = tk.Label(
            #text="Current profile configuration: " + current_profile,
            textvar = self.currentProfile,
            font=("Times", 12),
            width=50,
            height=2,
            master=info_frame
        )
        profile_status.pack()

        song_label = tk.Label(
            text="Song selected:",
            font=("Times", 12),
            master=info_frame
        )
        song_label.pack()

        selected_song = tk.Label(
            #text="Selected song: " + self.songName,
            textvar = self.songName,
            font=("Times", 12),
            width=50,
            height=2,
            master = info_frame
        )
        selected_song.pack()

        # control frame setup
        play = tk.Button(
            text=("Play"),
            command=self.play_audio,
            width=10,
            height=5,
            master=control_frame
        )
        play.pack(side=tk.LEFT)

        pause = tk.Button(
            textvar=self.pauseText,
            command=self.pause,
            width=10,
            height=5,
            master=control_frame
        )
        pause.pack(side=tk.RIGHT)

        # button frame setup
        select_song = tk.Button(
            text="Select song to play",
            font=("Times"),
            width=20,
            height=4,
            master=button_frame,
            command = self.choose_audio_file   
        )
        select_song.pack(side=tk.LEFT)

        profiles=[
            "Predictive",
            "Pop",
            "Hip Hop",
            "Rock",
            "Classical",
            "Blues",
            "Country",
            "Reggae",
            "Metal",
            "Jazz",
            "Disco"
            "Custom 1",
            "Custom 2"
        ]
        profile_select = tk.OptionMenu(
            button_frame,
            self.currentProfile,
            *profiles,
        )
        profile_select.config(width=25, height=5)
        profile_select.pack(side=tk.LEFT)

        #edit_profile = tk.Button(
        #    text="Modify profile EQ values",
        #    font=("Times"),
        #    width=25,
        #    height=5,
        #    master=button_frame
        #)
        #edit_profile.pack(side=tk.RIGHT)

        exit_button = tk.Button(
            text="Exit",
            font=("Times"),
            width=15,
            height = 2,
            command=exit
        )
        exit_button.pack(side=tk.BOTTOM)

        info_frame.pack(side=tk.TOP)
        control_frame.pack(side=tk.TOP)
        button_frame.pack(side=tk.BOTTOM)

    def choose_audio_file(self):
        name = filedialog.askopenfilename(
            initialdir="/",
            title="Select a file",
            filetypes= (("Audio files", "*.wav*"),)
        )
        self.pathToSong = name
        name = name.split("/")[-1:]
        self.songName.set(name)

    def play_audio(self):
        self.pauseText.set("Pause")
        self.playText.set("Playing...")
        self.pause_toggle = True
        firm.play(self.pathToSong, self.currentProfile.get(), self.config)
        self.playText.set("Play")

    def pause(self):
        if self.pause_toggle:
            firm.pause()
            self.pauseText.set("Unpause")
        else:
            firm.unpause()
            self.pauseText.set("Pause")
        self.pause_toggle = not self.pause_toggle # flip boolean
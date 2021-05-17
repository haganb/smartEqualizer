from Arduino import Arduino
from configparser import ConfigParser
import pygame
import os

def establish_connection():
    board = Arduino()


def play(song_name, profile, config):

    # Get predictive tag for song
    if(profile == "Predictive"):
        print("need to predict")

    # Get profile according to prediction
    config.config.read('config.ini')
    

    # Update arduino values



    # Play song
    print(song_name)
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play()

def pause():
    print("Now pausing...")
    pygame.mixer.music.pause()

def unpause():
    print("Now unpausing...")
    pygame.mixer.music.unpause()
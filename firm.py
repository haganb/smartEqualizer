from Arduino import Arduino
from configparser import ConfigParser
import pygame
import os
from predict import predict

def establish_connection():
    board = Arduino()


def play(song_name, profile, config):
    print("Now playing {}".format(song_name))
    # Get predictive tag for song
    
    if(profile == "Predictive"):
        profile = predict(song_name)

    # Get profile according to prediction
    print("Loading configuration for {}...".format(profile))
    config.config.read('config.ini')
    high = config[profile]["high"]
    med = config[profile]["med"]
    low = config[profile]["low"]
    print("value thruple: {}", (high, med, low))

    # Update arduino values
    


    # Play song
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play()

def pause():
    print("Now pausing...")
    pygame.mixer.music.pause()

def unpause():
    print("Now unpausing...")
    pygame.mixer.music.unpause()
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

def pause():
    print("Now pausing...")
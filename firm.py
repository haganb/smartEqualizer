from Arduino import Arduino
from configparser import ConfigParser
import pygame
import os
from predict import predict
import serial

arduino = serial.Serial(port='COM1', baudrate=115200, timeout=.1)


def write_read(x):
    x = str(x)
    arduino.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)
    data = arduino.readline()
    return data

# accounts for people misusing the config file or passing in invalid values
def flatten_payload(payload):
    # method used to apply ceiling to any payload values
    for val in range(len(payload)):
        if payload[val].isnumeric():
            if int(payload[val]) > 10:
                payload[val] = '10'
                print("Value capped at +10 dB")
            elif int(payload[val]) < -10:
                payload[val] = '-10'
                print("Value capped at -10 dB")
        else:
            payload[val] == '0'
            print("Value not accepted, defaulting to 0")
    return payload

def play(song_name, profile, config):
    print("Now playing {}".format(song_name))
    # Get predictive tag for song

    if(profile == "Predictive"):
        profile = predict(song_name)
    profile = profile.lower()
    
    # Get profile according to prediction
    print("Loading configuration for {}...".format(profile))
    config.config.read('config.ini')
    profile_val = config.get_profile(profile)

    # Update arduino values
    profile_val = flatten_payload(profile_val)
    payload = "".join(char + " " for char in profile_val)
    print(payload)
    write_read(payload)

    # Play song
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play()

def pause():
    print("Now pausing...")
    pygame.mixer.music.pause()

def unpause():
    print("Now unpausing...")
    pygame.mixer.music.unpause()
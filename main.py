import argparse
import tkinter as tk
from config import config
from menu import menu

# SMART EQUALIZER 
# University of Delaware Fall-Spring 2021
# Hagan Beatson, Alex Chacko, Ryan Lenihan, Michael Richards
# ELEG/CPEG 498/499


if __name__ == "__main__":
    config = config()
    menu = menu(config)
    #print(key for key in list(config.profiles.keys()))
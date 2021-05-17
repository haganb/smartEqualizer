import configparser

# SMART EQUALIZER 
# University of Delaware Fall-Spring 2021
# Hagan Beatson, Alex Chacko, Ryan Lenihan, Michael Richards
# ELEG/CPEG 498/499

# configuration class: used to read/write genre profile values
# config lets user set their own decible values for each genre profile
class config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.profiles = self.build_config_profile()

    def build_config_profile(self):
        self.config.read('config.ini')
        vals = {}
        for genres in self.config.sections():
            vals.update({genres : [self.config[genres]["high"], self.config[genres]["med"], self.config[genres]["low"]]})
        return vals

    def write_to_genre(self, genre, vals):
        #config_file = open("config.ini", 'w')
        #self.config(write(config_file))
        self.config.read("config.ini")
        self.config[genre]["high"] = vals[0]
        self.config[genre]["med"] = vals[1]
        self.config[genre]["low"] = vals[2]
        with open('config.ini', 'w') as conf:
            self.config.write(conf)
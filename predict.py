# Smart Equalizer Prediction Procedure
# ADAPTED FROM https://data-flair.training/blogs/python-project-music-genre-classification/
# Utilize GTZAN Genre Collection http://marsyas.info/downloads/datasets.html
# University of Delaware Spring 2021

from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np
import os
import pickle 
import numpy as np
from collections import defaultdict
from train_knn import getNeighbors, nearestClass

def loadDataset(filename):
    dataset = []
    with open(filename , 'rb') as f:
        while True:
            try:
                dataset.append(pickle.load(f))
            except EOFError:
                f.close()
                break
    return dataset

def predict(song_name):
    dataset = loadDataset("train.dat")
    results = defaultdict(int)
    i = 1
    for folder in os.listdir("audio/genres/"):
        results[i] = folder
        i += 1
    (rate,sig) = wav.read(song_name)
    mfcc_feat = mfcc(sig,rate, winlen=0.020, appendEnergy=False)
    covariance = np.cov(np.matrix.transpose(mfcc_feat))
    mean_matrix = mfcc_feat.mean(0)
    feature = (mean_matrix, covariance, 0)
    pred = nearestClass(getNeighbors(dataset ,feature , 5))
    return results[pred]
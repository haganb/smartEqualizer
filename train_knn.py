# Smart Equalizer Training Procedure
# ADAPTED FROM https://data-flair.training/blogs/python-project-music-genre-classification/
# Utilize GTZAN Genre Collection http://marsyas.info/downloads/datasets.html
# University of Delaware Spring 2021

from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np
import os
import pickle
import random
import operator

# distance: calculate "distance" between neighbors
def distance(instance1, instance2, k):
    distance =0 
    mm1 = instance1[0] 
    cm1 = instance1[1]
    mm2 = instance2[0]
    cm2 = instance2[1]
    distance = np.trace(np.dot(np.linalg.inv(cm2), cm1)) 
    distance+=(np.dot(np.dot((mm2-mm1).transpose() , np.linalg.inv(cm2)) , mm2-mm1 )) 
    distance+= np.log(np.linalg.det(cm2)) - np.log(np.linalg.det(cm1))
    distance-= k
    return distance

# getNeighbors: given a set and instance within the set, get the k nearest neighbors to the instance
def getNeighbors(trainingSet, instance, k):
    distances = []
    for x in range (len(trainingSet)):
        dist = distance(trainingSet[x], instance, k )+ distance(instance, trainingSet[x], k)
        distances.append((trainingSet[x][2], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

# nearestClass: narrow prediction down to single genre classification
def nearestClass(neighbors):
    classVote = {}
    for x in range(len(neighbors)):
        response = neighbors[x]
        if response in classVote:
            classVote[response]+=1 
        else:
            classVote[response]=1
    sorter = sorted(classVote.items(), key = operator.itemgetter(1), reverse=True)
    return sorter[0][0]

def getAccuracy(testSet, predictions):
    correct = 0 
    for x in range (len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return 1.0*correct/len(testSet)


# TRAIN KNN, OUTPUT TO BINARY
if __name__=="__main__":
    directory = "audio/genres/" # change if audio set directory is modified
    f = open("train.dat" ,'wb') # write to binary file
    i = 0
    for folder in os.listdir(directory):
        i += 1
        if i == 11:
            break   
        for file in os.listdir(directory+folder):  
            (rate,sig) = wav.read(directory + folder + "/" + file)
            mfcc_feat = mfcc(sig,rate, winlen=0.020, appendEnergy = False)
            covariance = np.cov(np.matrix.transpose(mfcc_feat))
            mean_matrix = mfcc_feat.mean(0)
            feature = (mean_matrix, covariance, i)
            pickle.dump(feature, f)
    f.close()
    dataset = []
    def loadDataset(filename , split , trSet , teSet):
        with open("my.dat" , 'rb') as f:
            while True:
                try:
                    dataset.append(pickle.load(f))
                except EOFError:
                    f.close()
                    break  
        for x in range(len(dataset)):
            if random.random() <split :      
                trSet.append(dataset[x])
            else:
                teSet.append(dataset[x])  
    trainingSet = []
    testSet = []
    loadDataset("train.dat" , 0.66, trainingSet, testSet) # 2/3rds train, 1/3rd validate
    leng = len(testSet)
    predictions = []
    for x in range (leng):
        predictions.append(nearestClass(getNeighbors(trainingSet ,testSet[x] , 5))) 
    accuracy1 = getAccuracy(testSet , predictions)
    print("KNN accuracy on dataset:", accuracy1)
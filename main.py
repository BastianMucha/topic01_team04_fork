# Pakete etc. 
# Pandas, Numpy und Matplotlib davor über Miniforge Prompt herunterladen sonst geht hier gar nix
# Panda is pandas dataframe
# numpy is number array (general python tool)

import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt
import sklearn as skl

from functions.PCA import *
from functions.KNN import *

from sklearn.decomposition import PCA
print('\n')
# Import der Dateien 
# ANMERKUNG: Funktioniert auch nur, wenn die Dateien in der SELBEN Directory wie das Skript sind -> Im Git-Ordner
# Problem mit Git da CSV-Dateien zu groß sind um sie zu committen, sonst kann man gar nix mehr pushen 
# Dateien in GitHub Desktop ab in .gitignore, dann verpisst sich das Problem

testdata = pnd.read_csv('fashion-mnist_test.csv')
traindata = pnd.read_csv('fashion-mnist_train.csv')
testdata_pixel = testdata.drop('label', axis=1).to_numpy()
traindata_pixel = traindata.drop('label', axis=1).to_numpy()
label_train = traindata['label'].to_numpy()
label_test = testdata['label'].to_numpy()


img = traindata_pixel.reshape((-1,28,28)) #only relevant for visualisation
num_img = traindata_pixel.shape[0]

# subtracting mean of each pixel while keeping the dimensions of the images to center the images in preparation for PCA
traindata_centered = centered(traindata_pixel)
testfunction()



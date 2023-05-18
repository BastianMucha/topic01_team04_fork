import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt
import sklearn as skl

from functions.PCA import pca, custum_imshow, centered
from collections import Counter

testdata = pnd.read_csv('fashion-mnist_test.csv')
traindata = pnd.read_csv('fashion-mnist_train.csv')
testdata_pixel = testdata.drop('label', axis=1).to_numpy()
traindata_pixel = traindata.drop('label', axis=1).to_numpy()
label_train = traindata['label'].to_numpy()
label_test = testdata['label'].to_numpy()

PCs_train, PCs_test = pca(traindata_pixel,testdata_pixel,0.90)

def knn_quality(PCs_train, PCs_test, k, label_train, label_test, testsize):
    """returns the accuray of the KNN for the first testsize images

    Args:
        PCs_train (numpy array): transformed training data
        PCs_test (numpy array): transformed testing data
        k (int): number of neighbours 
        label_train (numpy array 1D): labels of training data
        label_test (numpy array 1D): labels of testing data
        testsize (int): number of testing images you want to classify

    Returns:
        float: accuracy
    """
    distances = np.linalg.norm(PCs_test[:testsize, None] - PCs_train, axis=2)
    neighbour_index = np.argpartition(distances, kth=k-1, axis=1)[:,:k]
    neighbour_label = label_train[neighbour_index]
    result = []
    for subarray in neighbour_label:
        data = Counter(subarray)
        most_common_item = data.most_common(1)[0][0]
        result.append(most_common_item)
    result = np.array(result)
    accuracy = np.sum(result==label_test[:testsize])/testsize
    return accuracy

print(knn_quality(PCs_train, PCs_test, 10, label_train, label_test, 100))


def dist(PCs_test, PCs_train, k):
    """
    Calculates the k-nearest neighbors of the test data based on the training data.
    
    Parameters:
    PCs_test (numpy array): The test data matrix with shape (n_test_samples, n_features).
    PCs_train (numpy array): The training data matrix with shape (n_train_samples, n_features).
    k (int): The number of nearest neighbors to consider.
    
    Returns:
    numpy array: An array of shape (n_test_samples, k) containing the indices of the k-nearest neighbors for each test sample.
    """
    k = int(k)
    distances = np.linalg.norm(PCs_test[:10, None] - PCs_train, axis=2)
    item_numbers_of_most_similar_pics = np.argpartition(distances, kth=k-1, axis=1)[:, :k]

    return item_numbers_of_most_similar_pics


def labl(item_numbers_of_most_similar_pics,label):
    """
    Calculates the labels of the item numbers that were previously described as the closest ones.
    """
    labls = label[item_numbers_of_most_similar_pics]

    return labls

def most_common_items(arr):
    result = []
    for subarr in arr:
        data = Counter(subarr)
        most_common_item = data.most_common(1)[0][0]
        result.append(most_common_item)
    result = np.array(result)
    return result

def quality(orginal, result):
    fal = 0
    for i in range(0,len(result)):
        if orginal[i] == result[i]:
            fal += 1
    false_quote = fal/len(result)
    return false_quote

def knn_complete(PCs_test, PCs_train,k,label_train, label_test):
    label_neighbours = labl(dist(PCs_test, PCs_train, k),label_train)
    prediction = most_common_items(label_neighbours)
    error_rate = quality(label_test,prediction)
    return error_rate

#print(knn_complete(PCs_test, PCs_train, 10, label_train, label_test))
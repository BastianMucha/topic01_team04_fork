import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt
#import main #No module named 'main'

def centering(): # 'centering ist ein python eigenname, das Python Modul wird hiermit überschrieben. Das kann zu Problemen führen.'
    centered_img = img - img.mean(axis=(1,2), keepdims=True) #mean is calculated along 2nd and 3rd axis, meaning the heigth and the width of an image (remember: the first dimension is which picture we are looking at)
    return centered_img

def pca(centered_img,prop_variance): #added input variable centered_img
    covariance_matrix = np.cov(centered_img.reshape(num_img, -1), rowvar=False) #defining variable and creating covariance matrix while reshaping/flattening the images to obtain a 2D array, rowvar = False to compute cov matrix over rows, -1 means that the function calculates the required dimensions, so if the number of pictures is given it calculates the size 28x28 for each picture
    eigen_val , eigen_vec = np.linalg.eigh(covariance_matrix) #eigh function has two outputs, so two values have to be defined
    sorted_index = np.argsort(eigen_val)[::-1] #gives indexes to sort array from lowes to highest and inverts this vector
    sorted_eigenvalue = eigen_val[sorted_index] #apply sorting to eigenvalues
    sorted_eigenvectors = eigen_vec[:,sorted_index] #apply sorting to eigenvectors, first coordinate (vertical axis) has to be : to select all rows
<<<<<<< HEAD
    def propvar(prop_var):
        sum = 0
        sum_eigenvalues = sum(eigen_val)
        principal_component_number = -1
        while sum <= prop_var:
            for i in sorted_eigenvalue:
                sum += i/sum_eigenvalues
                principal_component_number += 1
        return principal_component_number
    eigenvectors_pca = sorted_eigenvectors[:,0:propvar(prop_variance)] #slicing of first principil_component_number eigenvectors from sorted eigenvector matrix
    # transform data
=======
    principal_component_number = 4 #yeah science
    eigenvectors_pca = sorted_eigenvectors[:,0:principal_component_number] #slicing of first principil_component_number eigenvectors from sorted eigenvector matrix
    # transform data

    # TODO there is no return of this function. 
>>>>>>> 9f1606df33356121895e5ac133bf8efdd9933c7c

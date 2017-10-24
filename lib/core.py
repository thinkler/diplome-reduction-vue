import os
import json
import urllib2
from sklearn.cluster import KMeans
from minisom import MiniSom
import numpy as np
from numpy import genfromtxt
import pandas as pd
import pdb
import csv
import io
import math
from sklearn.preprocessing import StandardScaler
from numpy import *
from numpy.linalg import *
from numpy.random import *
from sklearn.decomposition import PCA

def reduct(data, factors):
    performed = []
    for row in table.split('\n'):
        n_row = []
        for el in row.split(','):
            if (len(el) > 0):
                n_row.append(float(el))
        performed.append(n_row)
    performed.pop()

def cluster_to_int(array):
    new_arr = []
    for row in array:
        n_row = []
        for ind, el in enumerate(row):
            if (ind == 0):
                n_row.append(int(el))
            else:
                n_row.append(el)
        new_arr.append(n_row)
    return new_arr

def kmeans(array, fcount):
    performed_data = array

    kmeans = KMeans(n_clusters = fcount)
    kmeans.fit(performed_data)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    output_data = np.c_[labels, performed_data]
    output_data = output_data[np.argsort(output_data[:,0])]

    return output_data.tolist()

def pca(array, fcount):
    X = np.array(array)
    X_std = StandardScaler().fit_transform(X)
    mean_vec = np.mean(X_std, axis=0)
    cov_mat = np.cov(X_std.T)
    eig_vals, eig_vecs = np.linalg.eig(cov_mat)
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    eig_pairs.sort(key=lambda x: x[0], reverse=True)
    tot = sum(eig_vals)
    var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
    cum_var_exp = np.cumsum(var_exp)

    arr = []
    
    for i in range(fcount):
        arr.append(eig_pairs[i][1].reshape(len(eig_vals),1))

    matrix_w = np.hstack(arr)
    result = X_std.dot(matrix_w)


    cluster_nums = []
    for val in result:
        maxVal = np.amax(val)
        cluster_nums.append(np.nonzero(val == maxVal)[0][0])

    output = []
    for idx, val in enumerate(cluster_nums):
        output.append([val] + array[idx])

    return output

def soma(array, fcount):
    array = np.array(array)
    size = len(array[0])
    som = MiniSom(len(array), fcount, size, sigma=0.8, learning_rate=0.7) 
    som.random_weights_init(array)
    som.train_batch(array, 10)  
    
    results = []

    for val in array.tolist():
        results.append([som.winner(val)[1]] + val)

    return results

def norm(vec):
    return sqrt(sum(vec**2))

def mds(data, dimensions):
    """
    Multidimensional Scaling - Given a matrix of interpoint distances,
    find a set of low dimensional points that have similar interpoint
    distances.
    """

    data = np.array(data)

    arrSize = len(data)
    distance = zeros((arrSize,arrSize))



    for (i, pointi) in enumerate(data):
        for (j, pointj) in enumerate(data):
            distance[i,j] = norm(pointi - pointj)

    d = distance

    (n,n) = d.shape
    E = (-0.5 * d**2)

    # Use mat to get column and row means to act as column and row means.
    Er = mat(mean(E,1))
    Es = mat(mean(E,0))

        # From Principles of Multivariate Analysis: A User's Perspective (page 107).
    F = array(E - transpose(Er) - Es + mean(E))

    [U, S, V] = svd(F)

    Y = U * sqrt(S)

    cluster_nums = []
    for val in Y[:,0:dimensions]:
        maxVal = np.amax(val)
        cluster_nums.append(np.nonzero(val == maxVal)[0][0])

    output = []
    for idx, val in enumerate(cluster_nums):
        output.append([val] + data[idx].tolist())

    return output

    

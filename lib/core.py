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
from guppy import hpy
import time

def reduct(data, factors):
    performed = []
    for row in data.split('\n'):
        n_row = []
        for el in row.split(','):
            if (len(el) > 0):
                n_row.append(float(el))
        performed.append(n_row)
    performed.pop()
    data = performed

    true_cluster_nums = []        
    for row in data:
        true_cluster_nums.append(int(row[0]))
        del row[0]

    kmeansData = kmeans(data, factors)
    pcaData = pca(data, factors)
    somaData = soma(data, factors)
    mdsData = mds(data, factors)
    
    kmeansData['data'] = cluster_to_int(kmeansData['data'])
    pcaData['data'] = cluster_to_int(pcaData['data'])
    somaData['data'] = cluster_to_int(somaData['data'])
    mdsData['data'] = cluster_to_int(mdsData['data'])

    match_error = calc_errors(true_cluster_nums, kmeansData['data'], pcaData['data'], somaData['data'], mdsData['data'])
    clust_matches = clust_size(true_cluster_nums, kmeansData['data'], pcaData['data'], somaData['data'], mdsData['data'])

    pureOutput = []
    for index, row in enumerate(data):
        pureOutput.append([int(true_cluster_nums[index])] + row)


    return {
        'mds': {
            'title': 'Multidimensional Scaling',
            'data': mdsData['data'],
            'speed': mdsData['time'],
            'memory': mdsData['memory'],
            'match_error': match_error['mds'],
            'clusters_sizes': clust_matches['sizes']['mds'],
            'clusters_sizes_error': clust_matches['sizes_error']['mds']
        },
        'pca': {
            'title': 'Principal Component Analysis',
            'data': pcaData['data'],
            'speed': pcaData['time'],
            'memory': pcaData['memory'],
            'match_error': match_error['pca'],
            'clusters_sizes': clust_matches['sizes']['pca'],
            'clusters_sizes_error': clust_matches['sizes_error']['pca']
        },
        'kmeans': {
            'title': 'K-means',
            'data': kmeansData['data'],
            'speed': kmeansData['time'],
            'memory': kmeansData['memory'],
            'match_error': match_error['kmeans'],
            'clusters_sizes': clust_matches['sizes']['kmeans'],
            'clusters_sizes_error': clust_matches['sizes_error']['kmeans']
        },
        'soma': {
            'title': 'Self Organazing Map',
            'data': somaData['data'],
            'speed': somaData['time'],
            'memory': somaData['memory'],
            'match_error': match_error['soma'],
            'clusters_sizes': clust_matches['sizes']['soma'],
            'clusters_sizes_error': clust_matches['sizes_error']['soma']
        },
        'pure': {
            'data': pureOutput,
            'clusters_sizes': clust_matches['sizes']['pure'],
        }
    }

def calc_errors(ideal, kmeans, pca, soma, mds):
    mds_error = 0
    pca_error = 0
    soma_error = 0
    kmeans_error = 0
    for i, el in enumerate(ideal):
        if mds[i][0] != el:
            mds_error = mds_error + 1
        if pca[i][0] != el:
            pca_error = pca_error + 1
        if soma[i][0] != el:
            soma_error = soma_error + 1
        if kmeans[i][0] != el:
            kmeans_error = kmeans_error + 1

    return {
        'mds': mds_error,
        'pca': pca_error,
        'soma': soma_error,
        'kmeans': kmeans_error,
    }

def clust_size(ideal, kmeans, pca, soma, mds):
    mds_count = {}
    pca_count = {}
    soma_count = {}
    kmeans_count = {}
    ideal_count = {}
    # pdb.set_trace()
    for i, el in enumerate(ideal):
        if el in ideal_count:
            ideal_count[el] += 1
        else:
            ideal_count[el] = 1

        if mds[i][0] in mds_count:
            mds_count[mds[i][0]] += 1
        else:
            mds_count[mds[i][0]] = 1
        
        if pca[i][0] in pca_count:
            pca_count[pca[i][0]] += 1
        else:
            pca_count[pca[i][0]] = 1
        
        if soma[i][0] in soma_count:
            soma_count[soma[i][0]] += 1
        else:
            soma_count[soma[i][0]] = 1
        
        if kmeans[i][0] in kmeans_count:
            kmeans_count[kmeans[i][0]] += 1
        else:
            kmeans_count[kmeans[i][0]] = 1

    mds_error = {}
    pca_error = {}
    soma_error = {}
    kmeans_error = {}

    for key in ideal_count:
        mds_error[key] = mds_count[key] - ideal_count[key]    
        pca_error[key] = pca_count[key] - ideal_count[key]    
        soma_error[key] = soma_count[key] - ideal_count[key]    
        kmeans_error[key] = kmeans_count[key] - ideal_count[key]    

    return {
        'sizes': {
            'mds': mds_count,
            'pca': pca_count,
            'soma': soma_count,
            'kmeans': kmeans_count,
            'pure': ideal_count
        },
        'sizes_error': {
            'mds': mds_error,
            'pca': pca_error,
            'soma': soma_error,
            'kmeans': kmeans_error
        }
    }

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

    t0 = time.time()
    m0 =  hpy().heap().size
    kmeans = KMeans(n_clusters = fcount)
    kmeans.fit(performed_data)
    m1 =  hpy().heap().size
    t1 = time.time()
    
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    output_data = np.c_[labels, array]

    return { 'data': output_data.tolist(), 'time': t1 - t0, 'memory': m1 - m0 }

def pca(array, fcount):
    X = np.array(array)
    t0 = time.time()
    m0 =  hpy().heap().size
    X_std = StandardScaler().fit_transform(X)
    mean_vec = np.mean(X_std, axis=0)
    cov_mat = np.cov(X_std.T)
    eig_vals, eig_vecs = np.linalg.eig(cov_mat)
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
    eig_pairs.sort(key=lambda x: x[0], reverse=True)
    tot = sum(eig_vals)
    var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
    cum_var_exp = np.cumsum(var_exp)
    t1 = time.time()
    m1 =  hpy().heap().size
    
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

    return { 'data': output, 'time': t1 - t0, 'memory': m1 - m0 }

def soma(array, fcount):
    array = np.array(array)
    size = len(array[0])
    t0 = time.time()
    m0 =  hpy().heap().size
    som = MiniSom(len(array), fcount, size, sigma=0.8, learning_rate=0.7) 
    som.random_weights_init(array)
    som.train_batch(array, 10)  
    t1 = time.time()
    m1 =  hpy().heap().size
    results = []

    for val in array.tolist():
        results.append([som.winner(val)[1]] + val)

    return { 'data': results, 'time': t1 - t0, 'memory': m1 - m0 }

def norm(vec):
    return sqrt(sum(vec**2))

def mds(data, dimensions):
    data = np.array(data)

    arrSize = len(data)
    distance = zeros((arrSize,arrSize))

    for (i, pointi) in enumerate(data):
        for (j, pointj) in enumerate(data):
            distance[i,j] = norm(pointi - pointj)

    d = distance
    t0 = time.time()
    m0 =  hpy().heap().size
    (n,n) = d.shape
    E = (-0.5 * d**2)

    # Use mat to get column and row means to act as column and row means.
    Er = mat(mean(E,1))
    Es = mat(mean(E,0))

        # From Principles of Multivariate Analysis: A User's Perspective (page 107).
    F = array(E - transpose(Er) - Es + mean(E))

    [U, S, V] = svd(F)

    Y = U * sqrt(S)
    t1 = time.time()
    m1 =  hpy().heap().size
    cluster_nums = []
    for val in Y[:,0:dimensions]:
        maxVal = np.amax(val)
        cluster_nums.append(np.nonzero(val == maxVal)[0][0])

    output = []
    for idx, val in enumerate(cluster_nums):
        output.append([val] + data[idx].tolist())

    return { 'data': output, 'time': t1 - t0, 'memory': m1 - m0 }

    

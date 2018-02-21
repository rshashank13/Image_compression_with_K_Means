# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
from K_means_model import K_Means

def convert_matrix(matrix,clusters,idx):
    converted = matrix.copy()
    for i in range(matrix.shape[0]):
        converted[i] = clusters[idx[i]]
    return converted

img = Image.open('bird_small.png')
matrix = np.asarray(img)
pixels = matrix.shape
matrix = matrix.reshape(((matrix.shape[0]*matrix.shape[1]),matrix.shape[2]))
matrix = np.matrix(matrix)
my_model = K_Means()
clusters = my_model.run_K_means(matrix,16,iterations=10,best_of=1)
converted = convert_matrix(matrix,clusters, my_model.assigned_clusters)
converted = np.array(converted)
converted = converted.reshape(pixels)
im = Image.fromarray(np.uint8(converted))
im.save('converted.png')
im.show()


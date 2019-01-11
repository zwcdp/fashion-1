"""Read+Convert data

The data is embedded in a csv file with each row containing a label 
(first column) and the one pixel per column.

Convert each row to a (28x28) image

Global parameters:
    * LW (int): Width and height of the final images.
"""

__author__ = "Tim de Klijn"

import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


LW = 28 # length/width
N = 10000 # datasize

def convert_line(line: str, plot=False):
    """
    A line from the data file is converted to an image
    """

    # Create final image
    im = np.zeros((LW,LW))
    c = 1 # counter

    # Remove new line and split on ","
    line = line.replace("\n","").split(",") 
    label = int(line[0])

    # TODO speed up
    # Loop over pixels of empty image and place values from line list
    for y in range(np.shape(im)[0]):
        for x in range(np.shape(im)[1]):
            im[y][x] = int(line[c])
            c+=1
    if plot: plot_image(im)
    return label, im


def plot_image(im):
    """imshow array"""
    plt.imshow(im)
    plt.show()


def convert_data():
    """Convert data to usable format"""

    X = []
    y = []

    with open(os.path.join("data", "fashion-mnist_train.csv")) as f:
        lines = f.readlines()
        for l in lines[1:N]:
            label, im = convert_line(l)
            X.append(im.flatten())
            y.append(label)

    return X, y


def do_pca(X,y, components: int=2, plot: bool=True):
    """Run and plot PCA"""

    # PCA Stuff?
    pca = PCA(n_components=components)
    pca.fit(X)

    # Transform input data based onb eigenvectors
    X = pca.transform(X)
    x = [i[0] for i in X]
    y = [i[1] for i in X]

    # plot
    if plot:
        plt.scatter(x,y, c=y)
        plt.show()

if __name__ == "__main__":
    X, y = convert_data()
    do_pca(X, y)
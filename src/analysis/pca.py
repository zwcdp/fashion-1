import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

sys.path.append("..")

from data.data_reader import read_images

def do_pca(X, y, components: int = 2, plot: bool = True):
    """Run and plot PCA"""

    # PCA Stuff?
    pca = PCA(n_components=components)
    pca.fit(X)

    # Transform input data based on eigenvectors
    X = pca.transform(X)

    # Get scatters
    x = [i[0] for i in X]
    w = [i[1] for i in X]

    # plot
    if plot:
        plt.scatter(x, w, c=y)
        plt.show()

if __name__ == "__main__":
    X = read_images()
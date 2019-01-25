import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

def do_pca(X, y, components: int = 2, plot: bool = True):
    """Run and plot PCA"""

    new_X = []
    for i in X:
        new_X.append(i.flatten())

    X = new_X

    # PCA Stuff?
    pca = PCA(n_components=components)
    pca.fit(X)

    # Transform input data based on eigenvectors
    X = pca.transform(X)

    # Get scatters
    x = [i[0] for i in X]
    w = [i[1] for i in X]

    # plot

    plt.scatter(x, w, c=y)
    plt.show()
"""data_reader,

Global variables:
    * RAW_DATA_FOLDER (os.path): relative path to raw data
    * IMG_SIZE (int): length of side of image in pixels,
        assumes square image
    * FILENAMES (dict): dictionairy linking shorthand file
        identifiers to actual filenames
"""


__author__ = "Tim de Klijn"


import os
import gzip
import numpy as np
import matplotlib.pyplot as plt


RAW_DATA_FOLDER = os.path.join("data", "raw")
IMG_SIZE = 28
FILENAMES = {"train_data": "train-images-idx3-ubyte.gz",
             "train_label": "train-images-idx3-ubyte.gz",
             "test_data": "train-images-idx3-ubyte.gz",
             "test_label": "t10k-labels-idx1-ubyte.gz"}


def read_images(file_label="test_data", num_img=10):
    """
    Read images from idx3-ubyte.gz files and return the images in
    numpy array format.

    Parameters:
        * file_label (str): label pointing to FILENAMES dictionary value
        * num_img (int): amount of images to read

    Returns:
        * data (np.array): array containing the images as array
    """
    f = gzip.open(os.path.join(RAW_DATA_FOLDER, FILENAMES[file_label]))
    f.read(16)
    buf = f.read(IMG_SIZE * IMG_SIZE * num_img)
    data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    data = data.reshape(num_img, IMG_SIZE, IMG_SIZE, 1)
    f.close()

    return data

def read_labels(file_label="test_label", num_lab=10):
    """
    Read the 'num_lab' first labels form the label file with filename 
    FILESNAME[file_label] and return these a numpy array.

    Parameters:
        * file_label (str): label pointing to FILENAMES dictionary value
        * num_lab (int): amount of labels to read

    Returns:
        * labels (np.array): array containing the labels
    """
    f = gzip.open(os.path.join(RAW_DATA_FOLDER, FILENAMES[file_label]))
    labels = np.array([])
    for _ in range(0,num_lab):
        f.read(8)
        buf = f.read(1)
        # Add new label to list
        labels = np.concatenate([
            labels, 
            np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
            ])

    return labels


def quickplot_image(data, img_index=None) -> None:
    """
    Quickly plot an image from the dataset.

    Parameters:
        * data (np.array): array containing images as array
        * img_index (int): which images from the array to plot if
            img_index is None a radom image from the first 10 will
            be plotted
    """
    if img_index == None:
        img_index = np.random.choice(range(0,10))
    img = np.asarray(data[img_index]).squeeze()
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    data = read_images()
    quickplot_image(data)

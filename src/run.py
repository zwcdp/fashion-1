"""Calling python scripts based on commandline arguments

"""

import argparse


if __name__ == "__main__":


    parser = argparse.ArgumentParser(
        description="{}".format("Call python scripts")
    )

    parser.add_argument(
        "--pca", 
        action = "store_true",
        help = "Do PCA")

    args = parser.parse_args()

    if args.pca:
        print("do_pca")
        from analysis.pca import do_pca
        from data.data_reader import read_images, read_labels

        X = read_images(num_img=1000)
        y = read_labels(num_lab=1000)
        do_pca(X, y)
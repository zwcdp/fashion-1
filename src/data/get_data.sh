# Tim de Klijn, 2019

# Download data and place in ../../data/raw folder

# Check if folder exists, if not create
mkdir --parents ../../data/raw/

# Loactions + filenames of data and labels
TRAINDATA="../../data/raw/train-images-idx3-ubyte.gz"
TRAINLABEL="../../data/raw/train-labels-idx1-ubyte.gz"
TESTDATA="../../data/raw/t10k-images-idx3-ubyte.gz"
TESTLABEL="../../data/raw/t10k-labels-idx1-ubyte.gz"

# Download data

curl http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz \
    --output $TRAINDATA --silent

curl http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz \
    --output $TRAINLABEL --silent

curl http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz \
    --output $TESTDATA --silent

curl http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz \
    --output $TESTLABEL --silent

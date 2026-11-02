import numpy as np


def standardize(X):
    # assume that X is a 2D numpy ndarray
    # compute the vector of averages
    means= np.mean(a=X, axis=0)     # axis a counted from the right hand side
    # we want the means on columns
    stds = np.std(a=X, axis=0)
    # compute the standard deviation on columns (for variables)
    Xstd = (X - means) / stds
    return Xstd

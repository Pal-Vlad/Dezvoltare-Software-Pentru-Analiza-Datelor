import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
from mpmath import arange


# Python Graph Gallery
# https://python-graph-gallery.com/


# create the correlogram graphic
# assume that we receive a numpy.ndarray or
# pandas.DataFrame
def correlogram(R2=None, dec=2, title='Correlogram',
                valMin=-1, valMax=1):
    plt.figure(num=title, figsize=(12, 8), facecolor='w', edgecolor='k')

    plt.title(label=title, fontsize=12, fontweight='bold', horizontalalignment='center', verticalalignment='top')
    # heatmap works with both numpy.ndarray and pandas.data frame
    sb.heatmap(data=np.round(R2, decimals=dec), vmin=valMin, vmax=valMax, annot=True, cmap='RdYlGn')# cmap='bwr'
    return None

def correlation_circle(R2=None, V1=0, V2=1,
                    dec=2, title='Correlation circle'):
    # draw first a circle
    theta = [t for t in arange(0, 2*np.pi, 1)]
    print(theta, type(theta))
    X = [np.cos(t) for t in theta]
    Y = [np.sin(t) for t in theta]
    plt.plot(X, Y)
    return None

def eigenvalues(val, title='Explained variance by the principal components'):
    # TODO
    return None

def show():
    plt.show()

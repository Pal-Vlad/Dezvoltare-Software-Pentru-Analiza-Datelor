'''
A class for implementing PCA (Principal Components Analysis)
'''

import numpy as np
import Functions as f


class PCA:
    def __init__(self, X):
        # we assume that we receive X as a numpy.ndarray
        self.X = X
        # compute the correlation matrix of X
        self.Xcorr = np.corrcoef(x = self.X, rowvar = False)
        # we have the variables on the columns

        # standardize X
        self.Xstd = f.standardize(self.X)
        # compute the variance-covariance matrix
        self.Xcov = np.cov(m = self.Xstd, rowvar = False)
        #we have the variables on the columns
        np.linalg.eigh(self.Xcov)
        eigenvalues,eigenvectors = np.linalg.eigh(self.Xcov)
        print(eigenvalues,eigenvalues.shape)
        # sort the vectors of eighenvalues in descending order
        indices = [k for k in np.argsort(a=eigenvalues)[::-1]]
        indices = [k for k in np.argsort(a=eigenvalues, descending=True)]
        indices = [k for k in reversed(np.argsort(a=eigenvalues))]
        print(indices)
        self.alpha = eigenvalues[indices]
        self.a = eigenvectors[:, indices]


        # obtain the principal components
        # self.C = np.matmul(self.Xstd, self.a)
        self.C = self.Xstd @ self.a  # the operator @ is overloaded for matrix multiplication
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         #comment
    def getXcorr(self):
        return self.Xcorr

    def getXstd(self):
        return self.Xstd

    def getXcov(self):
        return self.Xcov

    def getEigenValues(self):
        return self.alpha
    def getEigenVectors(self):
        return self.a

    def getPrincipalComponents(self):
        return self.C
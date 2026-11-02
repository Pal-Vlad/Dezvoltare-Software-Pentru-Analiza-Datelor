import pandas as pd
import Functions as f
import Graphics as g
import numpy as np
import pca.PCA as pca


# table = pd.read_csv('./dataIN/Teritorial.csv',
#                     index_col=0)
table = pd.read_csv('./dataIN/Teritorial.csv',
                    index_col='Judet')
print(table, type(table))

# list of observations
obs = table.index.values[:]
print(obs, type(obs))

# list variables that can be used in the computation
vars = table.columns.values[1:]
print(vars, type(vars))

# extract from the dataFrame the useful numerical matrix
# in a numpy.ndarray
X = table[vars].values
print(X, type(X))

# standardize the initial variables
Xstd = f.standardize(X)
print(Xstd.shape, type(Xstd))
# save the standardized matrix into a CSV file
Xstd_df = pd.DataFrame(data=Xstd, index=obs, columns=vars)
Xstd_df.to_csv('./dataOUT/Xstd.csv')

# we need to compute the variance covariance matrix
# of standardized X
Xcov = np.cov(m=Xstd, rowvar=False)
print(Xcov.shape, type(Xcov))
# we have the variables on the columns
# save the covariance matrix into a CSV file
Xcov_df = pd.DataFrame(data=Xcov, index=vars, columns=vars)
Xcov_df.to_csv('./dataOUT/Xcov.csv')

# instantiate the PCA class
modelPCA = pca.PCA(X)
# extract the correlation matrix
Xcorr = modelPCA.getXcorr()
# create the correlogram based on the correlation matrix of X
g.correlogram(R2=Xcorr)
# create the correlogram based on the correlation matrix as pandas.DataFrames
Rcorr_df = pd.DataFrame(data=Xcorr, index=vars, columns=vars)
g.correlogram(R2=Rcorr_df, dec = 1, title='Correlogram from pandas.DataFrame')
# g.show()

# print the eighenvalues
alpha = modelPCA.getEigenValues()
print(alpha, type(alpha), alpha.shape)

# call the correlation circle function
g.correlation_circle()
g.show()


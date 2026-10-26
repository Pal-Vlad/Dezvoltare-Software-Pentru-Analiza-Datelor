import pandas as pd
import Functions as f
import Graphics as g
import matplotlib.pyplot as plt
import numpy as np

# table = pd.read_csv('./dataIN/Teritorial.csv', index_col=0)
# print(table)
table = pd.read_csv('./dataIn/Teritorial.csv', index_col ='Judet')

print(table, type(table))

#list observations
obs = table.index.values[:]
print(obs, type(obs))

#list variables that can be used in the computation
vars = table.columns.values[1:]
print(vars, type(vars))

# extract from the dataFrame the useful numerical matrix
# in a numpy.ndarray
X = table[vars].values
print(X, type(X))

# standardized the initial variables
Xstd = f.standardize(X)
print(Xstd.shape, type(Xstd))
# save the standardize matrix in to a CSV file
Xstd_df = pd.DataFrame(data=Xstd, index=obs, columns=vars)
Xstd_df.to_csv('./dataOUT/Xstd.csv')
plt.plot(X[:,0])
plt.show()

#we need to compute the variance covariance matrix
# of standardized X
Xcov = np.cov(m=Xstd, rowvar=False)
print(Xcov.shape, type(Xcov))
# we have the variables on the columns
# save the covarinace matrix into a csv matrix
# Xcov
Xcov_df = pd.DataFrame(data=Xcov, index=vars, columns=vars)
Xcov_df.to_csv('./dataOUT/Xcov.csv')
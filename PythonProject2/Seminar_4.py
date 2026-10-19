import numpy as np
import pandas as pd

# library problems solved with:
# venv/Scripts/activate
# pip3 install "packagename"

# create pandas. Series and pandas. Data Frame from various sources
# create a generator to generate the first 10 natural numbers
# we want to create a pandas series populated with those values
#
# def generator():
#     t=0
#     while True:
#         t+=1
#         yield t
# print(generator(), type(generator()))
# s1 = pd.Series(data = generator())
# print(s1)

#create a generator using a tuple pseudo-comprehension

tuple_generator = ((i+1) for i in range(10))
print(tuple_generator, type(tuple_generator))

s2 = pd.Series(data=tuple_generator, index =[f"L_{i+1}:" for i in range(10)])
print(s2)

#create labels for the s3 series with the following form "L_X"

s3 = pd.Series(data=((i+1) for i in range(10)), index= ("L_"+str(i+1) for i in range(10)))
print("value of s3\n", s3)

#how do we filter the elements of a series?
#select all values from series 3 which are greater than 5

print(s3[s3>5])

# create series numpy nd array
# shape = (3, 6,4) populate with random numbers generated in the interval(1,10)

array1 = np.random.randint (low = 1, high = 10, size = (3, 6, 4)).reshape(9,8)
print(array1, type(array1))

#create pandasDataFrame

pdf1 = pd.DataFrame(data = array1, index =[f"L_{i+1}:" for i in range(9)], columns =["L_"+str(i+1) for i in range(8)])
print (pdf1)


#create a dataFrame from dictionaries
#dictionary with 3 keys, alina, arina si alena
#for each key we have alina: tuple of strings

dict_1 = {
    "Alina": ("January", "February", "March", "April"),
    "Arina": np.random.randint (low = -5, high = 5, size = 4),
    "Alena": [1, 2, 3, 4]
}
print (dict_1, type(dict_1))

pdfDict = pd.DataFrame(data = dict_1)
print(pdfDict)


#Create a pandas DataFrame from a dictionary of dictionaries
#The keys of the exteranal dictionary are the following "Year 1, Year 2, Year 3" and the keys for the innner dictionaries are "S1, S2, ....S7
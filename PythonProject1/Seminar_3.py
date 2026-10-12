import numpy as np


# Lambda expressions in Python
avg = lambda a, b: (a+b) / 2
print('average of 7, 11 :', avg(8, 11))

#Compute via a Lambda expression the average of vector of values
vector_avg = lambda vector : sum(vector) / len(vector)
print('average of a list of values: ', vector_avg([7, 11, 13, 18]))


#The concept of generator in Python
#It is a special function which yield the next value in sequence
#Generate the first 10 natural numbers
def generator():
    t = 0
    while True:
        t+= 1
        yield t
#Using pseudo tuple comprehension
tuple_generator = (i+1 for i in range(10))
print(tuple_generator, type(tuple_generator))

print(generator(), type(generator()))
call = generator()
for i in range(10):
    #print('Number' + str(i) + ' = ', next(call))
    print('Number ' + str(i) + ' = ', next(tuple_generator))

#Populate a matrix of (6, 4) with random values in [-1, 5)
random_array = np.random.rand(24)
print(random_array, type(random_array))


#Function to convert values from [0, 1) to [a, b)
def random_AB(a, b, n):
    return (a+np.random.rand(n)*(b-a))

random_array= random_AB(-5, 5, 24)
print(random_array, type(random_array))

matrix = (np.ndarray(shape=(6,4), buffer = random_array, order = 'F'))
          # 'C' from contiguos ' f' from Fortran, for creating the matrix on columns
print(matrix, type(matrix))

#Create a ndarray of (3, 6, 4) populated with values randomly generate in [ 1, 10)

random_array = np.random.rand(72)
print(random_array, type(random_array))


def random_AB(a, b, n):
    return np.round((a+np.random.rand(n)*(b-a)))

random_array= random_AB(1, 10, 72)
print(random_array, type(random_array))

matrix = (np.ndarray(shape=(3, 6, 4), buffer = random_array, order = 'F'))
          # 'C' from contiguos ' f' from Fortran, for creating the matrix on columns
print(matrix, type(matrix))


print (np.random.randint(1, 10, size=(3,6,4)))
def int_random_AB(a, b, n):
    return np.random.randint(a,b,n);
vector_1 = int_random_AB(1,10,72)
array_3D = np.ndarray(shape=(3,6,4), buffer = vector_1, order='C', dtype = 'int16')
#The default size of an element for ndarray construct is 4 bytes
print(array_3D, type(array_3D))


#Create a dictionary which has as  keys 'S_1', 'S_2', ... and as values lists of 7 randomly generated integer values in [1, 10)
dict_1 = {'S_' + str(i+1): np.random.randint(1, 10, 7) for i in range(10)}
for(k, v) in dict_1.items():
    print(k, ':', v)
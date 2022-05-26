import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    sums = np.sum(np.exp(L))
    return [np.exp(x)/sums for x in L]
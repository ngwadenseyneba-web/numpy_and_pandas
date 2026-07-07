import numpy as np

#aggregate functions summerize data and returns a single value

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

'''
print(np.sum(array)) #sum of all elements
print(np.mean(array)) #mean of all elements
print(np.std(array)) #standard deviation of all elements
print(np.var(array)) #variance of all elements
print(np.min(array)) #minimum of all elements
print(np.max(array)) #maximum of all elements
print(np.argmin(array)) #index of minimum element
print(np.argmax(array)) #index of maximum element
'''

print(np.sum(array, axis=0)) #sum of each column
print(np.sum(array, axis=1)) #sum of each row
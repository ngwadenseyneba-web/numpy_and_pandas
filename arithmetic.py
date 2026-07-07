import numpy as np

#scalar arithmetic

#radii = np.array([1, 2, 3])

'''print(array + 1)
print(array - 1)
print(array * 2)
print(array / 2)
print(array ** 5)
'''

#vectorized math functions

'''print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
print(np.pi)'''

#exercise
#print(np.pi * radii ** 2 )

#Element wise arithmetic

'''array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)
'''

#comparison operators

scores =np.array([91, 55, 100, 73, 82, 64])

#print(scores < 60)

scores[scores < 60] = 0
print(scores)

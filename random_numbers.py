import numpy as np


'''
#integers
rng = np.random.default_rng(seed = 1)

print(rng.integers(low= 1, high= 101, size= (3, 2)))
'''
'''
#floats
np.random.seed(seed = 1) # seeds are used to generate the same radom numbers every time the code is run

print(np.random.uniform(low = -1, high = 1, size = (3, 2)))
'''

#shuffling

rng = np.random.default_rng()

'''
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)
'''

fruits = np.array([["🍎", "🍌", "🍒", "🌴", "🍇"],
                  ["🍑", "🥝", "🍓", "🍊", "🍋"]])
fruits = rng.choice(fruits, size = 3)
print(fruits)

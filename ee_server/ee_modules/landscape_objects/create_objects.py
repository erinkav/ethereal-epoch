import numpy
import random

results = list()
matrix = [[0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5]]

def choose_locations(num): 
  global matrix, results
  locations = random.sample(matrix, 2)
  for location in locations: 
      results.append(dict(location))
  print(results)

# def random_color
# for m x n sized matrix
# create mask for high altitude parts
# create mask for mid altitude parts

# create mask for low altitude parts

# choose random points on each level of altitude
# push random point to array 

# return [type, rotation, size, location, color]

# type = cube, sphere
# rotation = 0 --> 360
# size = 0.1 --> 1
# location = 0 - n, 0 - m, y at matrix[m, n]
# color = 0 --> 1


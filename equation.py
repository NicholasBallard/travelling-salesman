# equation for the travelling salesman problem

# Can do as array operation in numpy
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.sqrt.html
# >>> np.sqrt([1,4,9])
# array([ 1.,  2.,  3.])

# distance formula

def equation_distance_formula(pointX, pointY):
    return ((pointY[0] - pointX[0]) ** 2 + (pointY[1] - pointX[1]) ** 2) ** 0.5

# origin = # first point, point[0], can recalculate other points relative to origin (0, 0)
pointX = (2, 4)
pointY = (234, 100)

# use f-sting syntax to improve life considerably
# print(f"{equation_distance_formula(pointX, pointY):.2f}", f"units distance between point X {str(pointX)} \
# and point Y {str(pointY)}.")

# Works. Now need to operate on arrays.

import numpy as np

# make array of 1,000 2D coordinates
points = np.random.randint(-1e4, 1e4, (1000, 2))

# TODO: rules for travelling salesman
'''
calculate all the distances
go to all points
return to original
'''

# one distance, position 0 to position 1
print(f"{equation_distance_formula(points[0], points[1]):.2f} is the distance between point {str(points[0])} and point {str(points[1])}.")

# TODO: travelling calculate distances
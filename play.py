import numpy as np
from numpy import linalg

matrix = np.array(([0, 0, -3], [9, 3, 5], [3, 1, 1]))
print(linalg.matrix_rank(matrix))

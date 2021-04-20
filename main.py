import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

def plot_vectors(vectors, colors):
    """
    Plots vectors on the xy-plane. The `vectors` parameter is a Python list.
    Each vector is specified in the format [start_x, start_y, end_x, end_y]
    """
    vectors_array = np.array(vectors)
    start_x = vectors_array[:, 0]
    start_y = vectors_array[:, 1]
    length_x = vectors_array[:, 2] - vectors_array[:, 0]
    length_y = vectors_array[:, 3] - vectors_array[:, 1]

    plt.quiver(start_x, start_y, length_x, length_y, scale_units="xy", angles="xy", scale=1, color=colors)
    plt.gca().set_aspect("equal")
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()

def find_linear_combination_coefficients(e1, e2, v):
    matrix = np.array([e1, e2]).T
    coefficients = np.linalg.solve(matrix, v)
    return coefficients


e1, e2 = [[1, 0], [0, 1]]
v = [3.5, 8.6]
# Find the unknown coefficients. Extract the logic in a function.
# It should accept the two basis vectors and the one we need to represent
# and should return the two coefficients
coefficients = find_linear_combination_coefficients(e1, e2, v)
print("Coefficients: ", str(coefficients))
# Plot the three vectors
plot_vectors([[0, 0, i[0], i[1]] for i in [e1, e2, v]], ["red", "blue", "green"])

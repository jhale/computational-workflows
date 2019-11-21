import numpy as np

def compute_angles(side_lengths):
    a = np.arctan(side_lengths[0]/side_lengths[1])
    b = np.arctan(side_lengths[1]/side_lengths[0])
    hypotenuse = side_lengths[1]/np.sin(a) # Find the bug on this line!
    c = np.arcsin(hypotenuse*np.sin(a)/side_lengths[0])
    return np.rad2deg((a, b, c))

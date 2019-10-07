import numpy as np
import matplotlib.pyplot as plt

#This method is a formula taken from the laboratory booklet
def linear_regression(x,y):
    N = len(x)
    S_x = np.sum(x)
    S_y = np.sum(y)
    S_xx = np.sum(x ** 2)
    S_xy = np.sum(x * y)
    d = N * S_xx - S_x ** 2
    a_0 = (S_y * S_xx - S_x * S_xy) / d
    a_1 = (N * S_xy - S_x * S_y) / d
    y_reg = a_0 + a_1 * x
    D_y = y - y_reg
    S = np.sum((D_y) ** 2)
    Da0 = np.sqrt((1 / (N - 2)) * ((S * S_xx) / d))
    Da1 = np.sqrt((N / (N - 2)) * (S / d))
    return a_0, a_1

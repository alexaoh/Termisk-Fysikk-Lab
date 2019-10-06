#Prepared script for analysis while in the lab
from math import exp
import numpy as np
import matplotlib.pyplot as plt

def c_vm_T(T, R=8.314, theta_avg=270):
    return 3*R*(theta_avg/T)**2*(exp(theta_avg/T)/((exp(theta_avg/T)-1))**2)

#Using aluminium-data from Buyco og Davis
from math import exp
import numpy as np
import matplotlib.pyplot as plt


def c_vm_T(T, R=8.314, theta_avg=270): #Guessed 300 from eyeballing the plot.
    return 3*R*(theta_avg/T)**2*(exp(theta_avg/T)/((exp(theta_avg/T)-1))**2)

T = np.arange(10,1300)

c_vm_exp = np.array([0.0003269,0.001992,0.007608,0.01848,0.03371,0.05097,0.06851,0.08536,0.1010,0.1152,0.1655,0.1922,0.2070,0.2116,0.2156,0.2159,0.2222,0.2273,0.2321,0.2370,0.2421,0.2478,0.2539,0.2606,0.2679,0.2758,0.2844,0.2935])

T_exp = list(np.arange(10,101,10)) + [150,200,250,273.15,298.15] + list(np.arange(300,901,50))

plt.figure()

plt.plot(T, [c_vm_T(t) for t in T], Color="red",label="Theoretical")
plt.plot(T_exp,c_vm_exp*4.184*26.9815, Marker=".",Color="black",label="Experimental",Linestyle="") #Multiply by 4.184*26.9815 to get SI-units
plt.legend(loc=1)
plt.xlabel("T / K")
plt.ylabel("c / J $K^{-1}$ $mol^{-1}$")
plt.show()

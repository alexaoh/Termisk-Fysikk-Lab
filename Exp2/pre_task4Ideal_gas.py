#Plotting the ideal gas-data, to compare with the aluminium

#c_Vm = c_pm - R
from math import exp
import numpy as np
import matplotlib.pyplot as plt

R = 8.314

def c_vm_T(T, R=8.314, theta_avg=270): #Guessed 300 from eyeballing the plot.
    return 3*R*(theta_avg/T)**2*(exp(theta_avg/T)/((exp(theta_avg/T)-1))**2)

T = np.arange(10,1300)

c_pm_exp = np.array([29.114,29.685,30.447,31.302,31.336,32.207,32.992,33.674,34.255,35.166,35.832,36.336,36.732,37.057,37.334,37.579,37.802,38.008])

T_exp = [100,200,250,298] + list(np.arange(300,451,50)) + list(np.arange(500,1401,100))

print(T_exp)

plt.figure()

plt.plot(T, [c_vm_T(t) for t in T], Color="red",label="Theoretical")
plt.plot(T_exp,c_pm_exp-R, Marker=".",Color="black",label="Experimental",Linestyle="") #Multiply by 4.184*26.9815 to get SI-units
plt.legend(loc=1)
plt.xlabel("T / K")
plt.ylabel("c / J $K^{-1}$ $mol^{-1}$")
plt.show()

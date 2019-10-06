#Used this to calculate c_vm from theoretical formula
#the data was used to compare experimental data and theoretical data
from math import exp
import numpy as np
import matplotlib.pyplot as plt


def c_vm_T(T, R=8.314, theta_avg=1325):
    return 3*R*(theta_avg/T)**2*(exp(theta_avg/T)/((exp(theta_avg/T)-1))**2)

T = np.arange(10,1300)

c_vm_exp = [0.762,1.146,1.354,1.582,1.838,2.118,2.661,3.280,3.631,5.290,5.387,5.507]

T_exp = [222.4,262.4,283.7,306.4,331.3,358.3,413.0,479.2,520,879.7,1079.7,1258]

plt.figure()

plt.plot(T, [c_vm_T(t) for t in T], Color="red",label="Theoretical") #Got a bit weird results. Wrong theta_avg perhaps?
plt.plot(T_exp,c_vm_exp, Marker=".",Color="black",label="Experimental",Linestyle="")
plt.legend(loc=1)
plt.xlabel("T / K")
plt.ylabel("c / cal $mol^{-1}$ $K^{-1}$")
plt.show()

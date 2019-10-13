#Using aluminium-data from Giauque  og  Meads
from math import exp
import numpy as np
import matplotlib.pyplot as plt


def c_vm_T(T, R=8.314, theta_avg=285): #Guessed 300 from eyeballing the plot.
    return 3*R*(theta_avg/T)**2*(exp(theta_avg/T)/((exp(theta_avg/T)-1))**2)

T = np.arange(10,1300)

c_vm_exp = np.array([0.022,0.054,0.112,0.203,0.332,0.5,0.698,0.912,1.375,1.846,2.298,2.714,3.094,3.422,3.704,3.943,4.165,4.361,4.536,4.69,4.823,4.938,5.039,5.122,5.198,5.268,5.329,5.383,5.436,5.483,5.523,5.562,5.592,5.599])

T_exp = list(np.arange(15,50,5)) + list(np.arange(50,291,10)) + [298,300]

f = plt.figure()

plt.plot(T, [c_vm_T(t) for t in T], Color="red",label="Theoretical")
plt.plot(T_exp,c_vm_exp*4.184, Marker=".",Color="black",label="Experimental",Linestyle="") #Multiply by 4.184 to get SI-units
plt.legend(loc=2)
plt.title("Giauque and Meads (0K-300K)")
plt.xlim(0,300)
plt.xlabel("T / K")
plt.ylabel("c / J $K^{-1}$ $mol^{-1}$")
plt.show()

f.savefig("pre_task2.pdf", bbox_inches='tight')

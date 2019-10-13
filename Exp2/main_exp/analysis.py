#Prepared script for analysis while in the lab
from math import exp, sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def epsilon(y):
    return y/(exp(y)-1)

def delta_Q_minus_mdeltaL(theta, T_0=295.15, T_f=77, R=8.314, n=0.223375, L=2*10**5,delta_m=4.678/1000):
    return 3*n*R*((T_0*epsilon(theta/T_0)-(T_f*epsilon(theta/T_f))))-L*delta_m

root = float(fsolve(delta_Q_minus_mdeltaL, 10))
print(root)

x = list(np.arange(0,501))
plt.figure()
plt.plot(x,[delta_Q_minus_mdeltaL(t) for t in x], label="Test", linestyle="", marker="x")
plt.title("Test-plot")
plt.legend()
plt.show()

#The other data's delta_m = 4.678

#The steps in Gaussian uncertainty propagation, as highlighted in my journal, follows:

delta_m_1 = 4.912089327571124
delta_m_2 = 4.44409008358123

d_delta_m = (delta_m_1 - delta_m_2)/2
print("d_deltam is:",d_delta_m,"in grams.")

d_T = 1
print("d_T is:", d_T)

#The below is used to calculate delTheta/delT_0:
def new_function_for_Theta_del_T(theta, T_0=295.15+d_T, T_f=77, R=8.314, n=0.223375, L=2*10**5,delta_m=4.678):
    return 3*n*R*((T_0*epsilon(theta/T_0)-(T_f*epsilon(theta/T_f))))-L*delta_m*10**(-3)

def new_function_for_Theta_del_T_2(theta, T_0=295.15-d_T, T_f=77, R=8.314, n=0.223375, L=2*10**5,delta_m=4.678):
    return 3*n*R*((T_0*epsilon(theta/T_0)-(T_f*epsilon(theta/T_f))))-L*delta_m*10**(-3)

root_Theta_del_T = float(fsolve(new_function_for_Theta_del_T,10))
root_Theta_del_T_2 = float(fsolve(new_function_for_Theta_del_T_2,10))

del_theta_del_T_0 = (root_Theta_del_T - root_Theta_del_T_2)/(2*d_T) #This is 2.1 in my journal
print("The sensitivity of r$theta_{E}$ in regards to r$T_{0}$ is", del_theta_del_T_0)

#The below is used to calculate delTheta/del(deltam):
def new_function_for_Theta_del_deltam(theta):
    T_0=295.15
    T_f=77
    R=8.314
    n=0.223375
    L=2*10**5
    delta_m=4.678+d_delta_m
    return 3*n*R*((T_0*epsilon(theta/T_0)-(T_f*epsilon(theta/T_f))))-L*delta_m*10**(-3)

#I thought the fsolve function perhaps was not a fan of having a lot of variables in the function.
#I therefore tried to define it differently, but it gave the exact same result.
#Looks like it was right all along, despite the value of the Gaussian being higher than expected.
def new_function_for_Theta_del_deltam_2(theta):
    T_0=295.15
    T_f=77
    R=8.314
    n=0.223375
    L=2*10**5
    delta_m=4.678-d_delta_m
    return 3*n*R*((T_0*epsilon(theta/T_0)-(T_f*epsilon(theta/T_f))))-L*delta_m*10**(-3)

root_Theta_del_deltam = float(fsolve(new_function_for_Theta_del_deltam,10))
root_Theta_del_deltam_2 = float(fsolve(new_function_for_Theta_del_deltam_2,10))

del_theta_del_deltam = (-root_Theta_del_deltam + root_Theta_del_deltam_2)/(2*d_delta_m) #This is 2.2 in my journal

print("The sensitivity of r$theta_{E}$ in regards to r$deltam$ is", del_theta_del_deltam)

#The below is used to calculate the Gaussian uncertainty propagation:
error_theta = sqrt((del_theta_del_T_0*d_T)**2 + (del_theta_del_deltam*d_delta_m)**2)
print("The gaussian error is:", error_theta)

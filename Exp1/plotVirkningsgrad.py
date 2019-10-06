import numpy as np
import matplotlib.pyplot as plt

T_c = [14.3,14.2,12.4,10.6,8.8,7.5,6.2,5.0,3.9,2.8,2.1,1.2]
x = np.arange(0,23,2)
T_h = [14.5,16.5,18.9,21.1,23.2,25.2,27.1,28.7,30.0,31.6,32.9,34.4]

c = 4.2 #Spesifikk varmekapasitet
rho = 1 #Massetetthet til vannet
m = rho * 4.7 #4.7 er antall liter i hver bøtte
delta_t = 120 #Måler hvert andre minutt (120 sek)
P_snitt = 99.58 #Gjennomsnittseffekten fra kompressoren

delta_T = []
delta_T_hc = [] #For å plotte teoretisk øvre grense
for i in range(1,len(x)):
    delta_T.append(((T_h[i] - T_h[i-1])*m*c)/(P_snitt*delta_t))
    delta_T_hc.append(((T_h[i])+273.15)/(T_h[i]-T_c[i]))


plt.figure()

plt.plot(x[1:-1],delta_T[1:], Marker="+", Color="black",label=" "+r'$\eta$'+ " eksperiment",Linestyle="")
plt.plot(x[1:-1],delta_T_hc[1:], Marker=".",Color="peru",label=" "+r'$\eta$'+ " teoretisk øvre",Linestyle="")
plt.legend(loc=1)
plt.xlabel("t/min")
plt.ylabel("Virkningsgrad/"+r'$\eta$')
plt.show()

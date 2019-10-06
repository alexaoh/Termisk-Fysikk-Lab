import numpy as np
import matplotlib.pyplot as plt

T_c = [14.3,14.2,12.4,10.6,8.8,7.5,6.2,5.0,3.9,2.8,2.1,1.2]
x = np.arange(0,23,2)
T_h = [14.5,16.5,18.9,21.1,23.2,25.2,27.1,28.7,30.0,31.6,32.9,34.4]

plt.figure()

plt.plot(x[1:],T_c[1:], Marker="x", Color="blue",label="Cold Temperature",Linestyle="")

plt.plot(x[1:],T_h[1:], Marker="+",Color="red",label="Hot Temperature",Linestyle="")

plt.legend()

plt.xlabel("t/min")
plt.ylabel("T/Celsius")


plt.show()

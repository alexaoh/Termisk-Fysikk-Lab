from math import exp
import numpy as np
import matplotlib.pyplot as plt
from regression import linear_regression
from scipy.stats import linregress
#Tested with linregress from scipy also, to check the code.

#before alu-pece is inside the liquid nitrogen
#series_1 = [89.09,88.16,86.73,86.03,85.22,84.36,83.45,82.69,81.80]
#t_1 = [0,30,60] + list(np.arange(80,181,20))

#We are using another group's data instead:
t_1 = [0.33333333, 1.33333333, 2.33333333, 3.33333333, 4.33333333]
series_1 = [83.8, 81.27, 78.76, 76.34, 73.93]

#after alu-piece is inside the liquid nitrogen
#series_2 = [80.02,79.03,78.56,77.79,77.01,76.23,75.48,74.71,73.99,73.26,72.51,71.79,71.05,68.82]
#t_2 = list(np.arange(255,496,20)) + [555]

#We are using another group's data instead:
t_2 = [5.58333333, 6.65, 7.58333333, 8.58333333, 9.58333333, 10.58333333, 11.58333333]
series_2 = [66.469, 64.069, 62.149, 60.029, 57.909, 55.919, 53.879]

a_0_1, a_1_1 = linear_regression(np.array(t_1),np.array(series_1))
a_0_2, a_1_2 = linear_regression(np.array(t_2),np.array(series_2))

#a_1_1, a_0_1, tull, tull1, tull2 = linregress(t_1,series_1)
#a_1_2, a_0_2, tull, tull1, tull2 = linregress(t_2,series_2)

y_1 = a_0_1 + a_1_1*np.array(t_1)
y_2 = a_0_2 + a_1_2*np.array(t_2) - (6.089) #Takes the alu weight + string into regard


plt.figure()
plt.plot(t_1,y_1, label="Regression series 1", linestyle="", marker="x")
plt.title("Linear regression")
plt.plot(t_2,y_2, label="Regression series 2", linestyle="", marker="x")
plt.xlabel("t/seconds")
plt.ylabel("mass/grams")
plt.legend()
plt.show()

#Need to find delta_m
#Our OG delta_m = 5.067
#delta_m_1 = a_0_1 + a_1_1*t_1[-1] - (a_0_2 + a_1_2*t_1[-1] - 6.089)
#delta_m_2 = a_0_1 + a_1_1*t_2[0] - (a_0_2 + a_1_2*t_2[0] - 6.089)

#The other data's delta_m = 4.678 (already subtracted the weight of the alu-piece + string)
delta_m_1 = a_0_1 + a_1_1*t_1[-1] - (a_0_2 + a_1_2*t_1[-1])
print(delta_m_1)
delta_m_2 = a_0_1 + a_1_1*t_2[0] - (a_0_2 + a_1_2*t_2[0])
print(delta_m_2)

delta_m = (delta_m_1 + delta_m_2)/2 
print(delta_m)

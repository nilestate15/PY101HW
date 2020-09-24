#Problem 1
#Niles Tate

import numpy as np
import matplotlib.pyplot as plt

#Array
t = np.arange(0.,5.,0.2)

#plot full array
plt.plot(t, linestyle='--', color='red')
#plot markers every 2nd point
plt.plot(t, ' bs', markevery = 2)
#plot marker every 5th point
plt.plot(t, ' g^', markevery = 5)
plt.show()

#Problem 1
#Niles Tate

import numpy as np
import matplotlib.pyplot as plt
#data and point colors
data = {'x': np.arange(50),
        'mycolors': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
#data
data['y'] = data['x'] + 10 * np.random.randn(50)
data['scaled'] = np.abs(data['d']) * 100

#plot as scatter
plt.scatter('x', 'y', c='mycolors', s='scaled', data=data)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

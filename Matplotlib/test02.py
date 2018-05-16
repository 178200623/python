import numpy as np
import matplotlib.pyplot as plt

'''
叠加图
'''
t = np.arange(0. , 5 , 0.2)

plt.plot(t,t**4,'r--',t,t**5,'bs',t,t**6,'g^')
plt.plot(t,t,'r--')
plt.plot(t,t**2,'bs')
plt.plot(t,t**3,'g^')
plt.show()
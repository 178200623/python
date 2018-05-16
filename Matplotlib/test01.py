import numpy as np
import matplotlib.pyplot as plt
from pylab import *
'''
确定坐标范围
'''
x = np.arange(-5.0,5.0,0.02)
y1 = np.sin(x)

#窗体编号为1
plt.figure(1)
#分割figure，创建子坐标系
plt.subplot(211)
plt.plot(x,y1)

plt.subplot(212)
#设置x轴范围
xlim(-2.5,2.5)
#设置y轴范围
ylim(-1.1)
plt.plot(x,y1)

plt.show()
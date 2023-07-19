import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5]
y=[7,4,8,10,20]
#===================================

y_2=[1,2,3,4,5]

#===================================
plt.title('graph')
plt.plot(x,y,'b--',label='first')
plt.plot(x,y_2,'r-',label='second')
plt.ylabel('velocity (m/s)')
plt.xlabel('time (s)')
plt.legend()
plt.show()

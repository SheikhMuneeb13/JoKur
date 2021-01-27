import numpy as np
import matplotlib.pyplot as plt
import math


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


#Co-ordinates of the points C and D are gven below:
p = 3.5 - 3*math.cos(math.radians(75))
q = 3*math.sin(math.radians(75))
r = 3.5 - 3*(math.cos(math.radians(75))) - 4* math.cos(math.radians(15))
z = 3* math.sin(math.radians(75)) + 4* math.sin(math.radians(15))

#vertices
T = np.array([0,0])
R = np.array([3.5,0])
U = np.array([p,q])
E = np.array([r,z])

#Generating all lines
x_TR = line_gen(T,R)
x_RU = line_gen(R,U)
x_UE = line_gen(U,E)
x_ET = line_gen(E,T)

#Plotting all lines
plt.plot(x_TR[0,:],x_TR[1,:],label='$TR$')
plt.plot(x_RU[0,:],x_RU[1,:],label='$RU$')
plt.plot(x_UE[0,:],x_UE[1,:],label='$UE$')
plt.plot(x_ET[0,:],x_ET[1,:],label='$ET$')

plt.plot(T[0], T[1], 'o')
plt.text(T[0] * (1 - 0.1), T[1] * (1) , 'T')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.1), R[1] * (1+0.1) , 'R')
plt.plot(U[0], U[1], 'o')
plt.text(U[0] * (1 + 0.03), U[1] * (1 - 0.1) , 'U')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.05), E[1] * (1 + 0.01) , 'E')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.plot()
plt.show()
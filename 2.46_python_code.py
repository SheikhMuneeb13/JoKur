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

#vertices
R = np.array([0,0])
E = np.array([5.1,0])
A = np.array([5.1,5.1])
D = np.array([0,5.1])

#Generating all lines
x_RE = line_gen(R,E)
x_EA = line_gen(E,A)
x_AD = line_gen(A,D)
x_DR = line_gen(D,R)

#Plotting all lines
plt.plot(x_RE[0,:],x_RE[1,:],label='$RE$')
plt.plot(x_EA[0,:],x_EA[1,:],label='$EA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_DR[0,:],x_DR[1,:],label='$DR$')

plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 - 0.1), R[1] * (1) , 'R')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.1), E[1] * (1+0.1) , 'E')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.1) , 'A')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.05), D[1] * (1 + 0.01) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.plot()
plt.show()
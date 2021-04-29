# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:18:57 2021

@author: DEBDOOT
"""
'''
Monoatomic case

M=[E b 0 0.....b]
  [b E b 0.....0]
  [0 b E b.....0]
  [.............]
  [0.......b E b]
  [b.......0 b E]
'''
import matplotlib.pyplot as plt
import scipy.linalg as la
import math

def Eig(A):

    evals, evecs = la.eig(A)
    evals = evals.real
    return evals
    

n=int(input("Enter matrix dimension:"))
M=[[0 for i in range(n)] for j in range(n)]
E=int(input("Enter diagonal element:"))

b=int(input("Enter non-diagonal element:"))
M[0][n-1]=b
M[n-1][0]=b
for i in range(n):
    for j in range(n):
        if i==j:
            M[i][j]=E
        elif i==j-1 or i==j+1:
              M[i][j]=b


print("The Histogram plot is given below:")
'''
for i in range(n):
    for j in range(n):
        print(M[i][j],end="  ")
    print()
'''
Eigen=Eig(M)
print("The eigen values of the input matrix are:")
for i in range(len(Eigen)):
    print(Eigen[i])
print("--------------------")
maxE=max(Eigen)
minE=min(Eigen)
print("maxium eigen value is:",maxE)
print("minimum eigen value is:",minE)
intervalNum=math.sqrt(n)
Bi=int(intervalNum)
plt.style.use('ggplot')
plt.hist(Eigen, bins=Bi)
plt.xlabel('For mono-atomic case EigenValue')
plt.ylabel('Density of states')
plt.title(f'For dimension n={n},dia E={E}, nondia b={b}')
plt.show()

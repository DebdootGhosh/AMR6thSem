# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:46:08 2021

@author: hp
"""
'''
Diatomic

m=[E1 b 0 0.....b]
  [b E2 b 0.....0]
  [0 b E1 b.....0]
  [.............]
  [0.......b E1 b]
  [b.......0 b E2]
  or
 m=[E1 b 0 0.....b]
  [b E2 b 0.....0]
  [0 b E1 b.....0]
  [.............]
  [0.......b E2 b]
  [b.......0 b E1] 

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
E1=int(input("Enter the value of odd diagonal element:"))
E2=int(input("Enter the value of even diagonal element:"))

b=int(input("Enter the value of non-diagonal element:"))
M[0][n-1]=b
M[n-1][0]=b 
for i in range(n):
    for j in range(n): 
        if i==j:
            if j%2==0:
                M[i][j]=E1
            else:
                M[i][j]=E2
        elif i==j+1:
                M[i][j]=b
        elif i==j-1:
                M[i][j]=b


print("The Histogram plot is given below:")

'''for i in range(n):
   for j in range(n):
        print(M[i][j],end="  ")
   print()
    '''

Eigen=Eig(M)
print("The eigen values are:")
for i in range(len(Eigen)):
    print(Eigen[i])
print("----------------")
maxE=max(Eigen)
minE=min(Eigen)

print("maxium eigen value is:",maxE)
print("minimum eigen value is:",minE)
intervalNum=math.sqrt(n)
Bi=int(intervalNum)
plt.style.use('ggplot')
plt.hist(Eigen, bins=Bi)
plt.xlabel('For di-atomic case EigenValue')
plt.ylabel('Density of states')
plt.title(f'For dimension={n}, dia={E1,E2},nondia={b}')
plt.show()

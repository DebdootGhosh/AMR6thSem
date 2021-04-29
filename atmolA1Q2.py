# -*- coding: utf-8 -*-
'''
Diatomic

m=[E1 b 0 0.....0]
  [b E2 b 0.....0]
  [0 b E1 b.....0]
  [.............]
  [0.......b E1 b]
  [0.......0 b E2]
  or
 m=[E1 b 0 0.....0]
  [b E2 b 0.....0]
  [0 b E1 b.....0]
  [.............]
  [0.......b E2 b]
  [0.......0 b E1] 

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
'''
print("The eigen values are:")
for i in range(len(Eigen)):
    print(Eigen[i])
print("----------------")
'''
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

'''
input:
1.Enter matrix dimension:2000
  Enter the value of odd diagonal element:-11
  Enter the value of even diagonal element:-9
  Enter the value of non-diagonal element:-6
  
2.Enter matrix dimension:2501
  Enter the value of odd diagonal element:-11
  Enter the value of even diagonal element:-9
  Enter the value of non-diagonal element:-6
  
3.Enter matrix dimension:3000
  Enter the value of odd diagonal element:-11
  Enter the value of even diagonal element:-9
  Enter the value of non-diagonal element:-6  
  
4.Enter matrix dimension:4001
  Enter the value of odd diagonal element:-11
  Enter the value of even diagonal element:-9
  Enter the value of non-diagonal element:-6  
  
5.Enter matrix dimension:5000
  Enter the value of odd diagonal element:-11
  Enter the value of even diagonal element:-9
  Enter the value of non-diagonal element:-6 
  
6.Enter matrix dimension:5500
  Enter the value of odd diagonal element:-11
  Enter the value of even diagonal element:-9
  Enter the value of non-diagonal element:-6  
  
7.Enter matrix dimension:6001
  Enter the value of odd diagonal element:-11
  Enter the value of even diagonal element:-9
  Enter the value of non-diagonal element:-6  
  
8.Enter matrix dimension:4000
  Enter the value of odd diagonal element:-12
  Enter the value of even diagonal element:-10
  Enter the value of non-diagonal element:-3  

9.Enter matrix dimension:4000
  Enter the value of odd diagonal element:-10
  Enter the value of even diagonal element:-8
  Enter the value of non-diagonal element:-4
  
10.Enter matrix dimension:4000
  Enter the value of odd diagonal element:-11
  Enter the value of even diagonal element:-9
  Enter the value of non-diagonal element: -5  
  
11.Enter matrix dimension:4000
  Enter the value of odd diagonal element:-10
  Enter the value of even diagonal element:-8
  Enter the value of non-diagonal element:-7

12.Enter matrix dimension:4000
  Enter the value of odd diagonal element:-10
  Enter the value of even diagonal element:-8
  Enter the value of non-diagonal element:-3

'''
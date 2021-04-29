# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:16:15 2021

@author: debdoot
"""

'''
 
Monoatomic case

M=[E b 0 0.....0]
  [b E b 0.....0]
  [0 b E b.....0]
  [.............]
  [0.......b E b]
  [0.......0 b E]
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
'''
print("The eigen values of the input matrix are:")
for i in range(len(Eigen)):
    print(Eigen[i])
print("--------------------")
'''
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

'''
input:
1.Enter matrix dimension:2000
  Enter diagonal element:-12
  Enter non-diagonal element:-4
  
2.Enter matrix dimension:2000
  Enter diagonal element:-12
  Enter non-diagonal element:-5
  
3.Enter matrix dimension:2000
  Enter diagonal element:-12
  Enter non-diagonal element:-6  
  
4.Enter matrix dimension:2000
  Enter diagonal element:-12
  Enter non-diagonal element:-7  
  
5.Enter matrix dimension:2000
  Enter diagonal element:-12
  Enter non-diagonal element:-8  
  
6.Enter matrix dimension:2000
  Enter diagonal element:-12
  Enter non-diagonal element:-9
  
7.Enter matrix dimension:500
  Enter diagonal element:-12
  Enter non-diagonal element:-6 
  
8.Enter matrix dimension:1000
  Enter diagonal element:-12
  Enter non-diagonal element:-6  
  
9.Enter matrix dimension:1500
  Enter diagonal element:-12
  Enter non-diagonal element:-6  
  
10.Enter matrix dimension:2000
   Enter diagonal element:-12
   Enter non-diagonal element:-6  
   
11.Enter matrix dimension:3500
   Enter diagonal element:-12
   Enter non-diagonal element:-6 

'''
'''
output:
1.maxium eigen value is: -4.000009859740166
  minimum eigen value is: -19.99999014025986
  
2.maxium eigen value is: -2.0000123246752186
  minimum eigen value is: -21.999987675324697  
  
3.maxium eigen value is: -1.4789610254124411e-05
  minimum eigen value is: -23.999985210389845  

4.maxium eigen value is: 1.999982745454693
  minimum eigen value is: -25.999982745454673  
  
5.maxium eigen value is: 3.9999802805196523
  minimum eigen value is: -27.99998028051964 
  
6.maxium eigen value is: 5.999977815584621
  minimum eigen value is: -29.99997781558465
  
7.maxium eigen value is: -0.00023592508542761404
  minimum eigen value is: -23.999764074914637 
  
8.maxium eigen value is: -5.909932006411628e-05
  minimum eigen value is: -23.999940900679906  
  
9.maxium eigen value is: -2.628387861180445e-05
  minimum eigen value is: -23.99997371612142  
  
10.maxium eigen value is: -1.4789610254124411e-05
   minimum eigen value is: -23.999985210389845  
   
11.maxium eigen value is: -0.0731330473885765e-06
   minimum eigen value is: -23.99999516866955   
    '''
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:02:36 2021

@author: debdoot
"""

from numpy import*
from matplotlib.pyplot import*
M=[[-10,-5,0,0,0],[-5,-10,-5,0,0],[0,-5,-10,-5,0],[0,0,-5,-10,-5],[0,0,0,-10,-5]]
evalue,evect=linalg.eig(M)
x=evalue



t=[10**-16,10**-15,10**-14,10**-13,10**-12]
E=sort(x)
print(E)
omega_ba1=[]
T1=[]
for i in range(len(E)-1):
    omega_ba1.append((E[i+1]-E[0]))
    T1.append(t[i+1])


omega_ba2=[]
T2=[]
for i in range(len(E)-2):
    omega_ba2.append(E[i+2]-E[1])
    T2.append(t[i+2])
    
X=[i for i in range(-10,50,1)]
print(X)
hbar=6.58*10**-16
C1=[]
C2=[]
for j in range(len(omega_ba1)):
    x1=[]
    for i in range(len(X)):
        
        c1=((10**35)/( (1/(4*T1[j]**2))+((omega_ba1[j]-X[i])/hbar)**2 ))
        x1.append(c1)
    C1.append(x1)
        
for j in range(len(omega_ba2)):
    x2=[]
    for i in range(len(X)):
        c2=((10**35)/( (1/(4*T2[j]**2))+((omega_ba2[j]-X[i])/hbar)**2 ))
        x2.append(c2)
    C2.append(x2)


print(len(X),len(C2[0]))
for i in range(len(C1)):
    print(i)
    k=i+2
    plot(X,C1[i],label='$E_{%.d} to E_1$'%k)
    ylim(0,10000)
    title('Transition from Ei to E1')
    xlabel('Energy(ev)')
    ylabel('Transistion probability *10^35')
    legend()
show()

for i in range(len(C2)):
    print(i)
    k=i+3
    plot(X,C2[i],label='$ E_{%.d} to E_2 $'%k)
    ylim(0,10000)
    title('Transition from Ei to E2')
    xlabel('Energy(ev)')
    ylabel('Transistion probability *10^35')
    legend()
show()



    
    
    
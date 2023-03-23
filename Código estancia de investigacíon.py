

#aquí importamos todo lo necesario
import numpy as np
import sympy
from sympy import *
import sympy as sp
sp.init_printing(use_latex='mathjax')
from gravipy import *


#aquí definimos los símbolos de las variables que usaremos
t,r, theta, phi, Gamma , Lambda, Phi, k, x, y, z = symbols('t,r, theta, phi, Gamma, Lambda, Phi, k, x, y, z')
M=symbols('M')
Q=symbols('Q')
R=symbols('R')
a = sympy.Function('a')(t) #factor de escala de la métrica FRW


#aquí definimos los tipos de coordenadas con las que queremos expresar el resultado
xi = Coordinates('chi', (t,r,theta,phi))
#xi = Coordinates('chi', ( t,x, y, z))
#xi = Coordinates('chi', (x,y)) #cart
#xi = Coordinates('chi', (r,phi)) #pol, cono
#xi = Coordinates('chi', (z, phi)) #cil
#xi = Coordinates('chi', (theta,phi)) #esf

#El número de dimensiones cambia según la teoría en la que estemos.
nd=4 #Este es el número de dimensiones
ndp1=nd+1

#Integral(t,t)
xi(-1)
for i in range(1,ndp1):
    sp.pprint(latex(xi(-i)))
    

#Aquí introducimos las métricas en 2D
#Metric = diag(1, 1) #cartesianas
#Metric = diag(1/y**2, 1/y**2) #lobachevsky
#Metric = diag(1, r**2) #polares 
#Metric = diag(R**2, R**2*(sin(theta))**2) #esfera (ds**2=R**2dtheta**2+R**2sintheta**2dphi**2) R es parametro
#Metric = diag(1, r**2*(sin(theta))**2) #cono (ds**2=dr**2+r**2sintheta**2dphi**2), theta es parametro


#Aquí vienen las métricas en 4D
#Para estos hay que descomentar la 'r', ya que se añade una dimensión más.
#Metric = diag(-(1-2*M/r), 1/(1-2*M/r), r**2, r**2*sin(theta)**2) #schwar
#Metric = diag(-(1-2*M/r+Q**2/r**2), 1/(1-2*M/r+Q**2/r**2), r**2, r**2*sin(theta)**2) #reissner-Nordstrom
Metric = diag(-1,a**2/(1-k*r**2),a**2*r**2, a**2*r**2*sin(theta)**2) #FRW


#código para el tensor métrico
g = MetricTensor('g', xi, Metric)
for i in range(1,ndp1):
    for j in range(1,ndp1):
        print ('g('+ str(i-1)+',' + str(j-1)+')=') 
        print ("\n")
        sp.pprint(latex(g(i,j)))
        print ("\n")


#símbolos de christoffel
Ga = Christoffel('Gamma', g)
for i in range (1,ndp1):
    for j in range (1,ndp1):
        for k in range (1,ndp1):
            if Ga(-i,j,k) != 0:
                sp.pprint(Gamma,)
                print('('+ str(i-1)+',' +str(j-1)+','+ str(k-1)+')=') 
                sp.pprint(latex(Ga(-i,j,k)))
                pass
            
            
#tensor de ricci
Ri = Ricci('Ri', g)
for i in range (1,ndp1):
    for j in range (1,ndp1):
        if Ri(i,j) != 0:
            print('R('+ str(i-1)+',' + str(j-1)+')=') 
            print("\n")    
            sp.pprint(latex(Ri(i,j)))

#escalar de Ricci
R=0
for i in range(1,ndp1):
    R=R+Ri(-i,i)
print('R=')
print(R)    
        

#tensor de Einstein    
G = Einstein('G',Ri)
for i in range (1,ndp1):
    for j in range (1,ndp1):
        if G(i,j) != 0:
            print('G('+ str(i-1)+',' + str(j-1)+')=') 
            print("\n")    
            sp.pprint(latex(G(i,j)))
        
                
 
#tensor de Riemann          
Rm = Riemann('Rm', g)
tau = symbols('tau')

#geodésicas
w = Geodesic('w', g, tau)

for i in range (1,ndp1):
    print('geod('+ str(i-1)+'):') 
    sp.pprint(latex(w(i)))
    
for i in range(1,ndp1):
    for j in range(1,ndp1):
        for k in range(1,ndp1):
            for m in range(1,ndp1):
                if Rm(i,j,k,m) != 0:
                    print('Rm(' + str(i-1)+','+str(j-1)+','+str(k-1)+','+str(m-1)+')=')
                    print("\n")
                    sp.pprint(latex(Rm(i,j,k,m)))

              

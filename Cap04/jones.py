import numpy as np
import matplotlib.pyplot as plt
import random as rd
import pandas as pd

dt = 0.001
t = 1000

n_particulas = 2

eps = 10.0
sigma = 1.0



x = np.zeros(n_particulas)
y = np.zeros(n_particulas)
z = np.zeros(n_particulas)

vx = np.zeros(n_particulas)
vy = np.zeros(n_particulas)
vz = np.zeros(n_particulas)


def init_conditions():
    x[0] = sigma*rd.random()
    y[0] = sigma*rd.random()
    z[0] = sigma*rd.random()

    vx[0] = sigma*rd.random()
    vy[0] = sigma*rd.random()
    vz[0] = sigma*rd.random()

    x[1] = x[0] + 2*sigma*rd.random()
    y[1] = y[0] + 2*sigma*rd.random()
    z[1] = z[0] + 2*sigma*rd.random()

    vx[1] = sigma*rd.random()
    vy[1] = sigma*rd.random()
    vz[1] = sigma*rd.random()


init_conditions()


file = open('dinamica_jones.dat', "w")
file.write('x,y,z\n')
for i in range(0,n_particulas):
    file.write(str(x) + ',' + str(y) + ',' + str(z) + '\n' )



def forces(x,y,z):
    F = np.zeros((n_particulas,3))
    for i in range(0,n_particulas):
        for j in range(0,n_particulas):
            if i!=j:
                r=np.sqrt((x[i]-x[j])**2 +(y[i]-y[j])**2 +(z[i]-z[j])**2)
                V=24*eps*sigma**6*(r**6-2*sigma**6)/r**13
                F[i][0] += (x[i]-x[j])*V
                F[i][1] += (y[i]-y[j])*V
                F[i][2] += (z[i]-z[j])*V
    return F

def move(x,y,z,vx,vy,vz):
    for i in range(0,n_particulas):
        F = forces(x,y,z)
        vx[i] = vx[i]+dt*F[i][0]
        vy[i] = vy[i]+dt*F[i][1]
        vz[i] = vz[i]+dt*F[i][2]

        x[i]=x[i] + vx[i]*dt
        y[i]=y[i] + vy[i]*dt
        z[i]=z[i] + vz[i]*dt
    file.write(str(x) + ',' + str(y) + ',' + str(z) + '\n' )

def run():
    for i in range(0,t):
        move(x,y,z,vx,vy,vz)
run()

file.close()



data = pd.read_csv('dinamica_jones.dat', header = 0)

a = data['x'][0:]

xparticula1 = []
xparticula2 = []
for element in a:
    element = element.replace('[','')
    element = element.replace(']','')
    elementos = element.split()
    xparticula1.append(float(elementos[0]))
    xparticula2.append(float(elementos[1]))

b = data['y'][0:]

yparticula1 = []
yparticula2 = []
for element in b:
    element = element.replace('[','')
    element = element.replace(']','')
    elementos = element.split()
    yparticula1.append(float(elementos[0]))
    yparticula2.append(float(elementos[1]))


c = data['y'][0:]

zparticula1 = []
zparticula2 = []
for element in b:
    element = element.replace('[','')
    element = element.replace(']','')
    elementos = element.split()
    zparticula1.append(float(elementos[0]))
    zparticula2.append(float(elementos[1]))


fig=plt.figure()
ax=fig.gca(projection ='3d')
ax.scatter(xparticula1[0],yparticula1[0],zparticula1[0], color = 'black')
ax.scatter(xparticula2[0],yparticula2[0],zparticula2[0], color = 'black')
ax.plot(xparticula1,yparticula1,zparticula1, color = 'red')
ax.plot(xparticula2,yparticula2,zparticula2, color = 'blue')
plt.show()

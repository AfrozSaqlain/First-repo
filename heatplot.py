import numpy as np
import matplotlib.pyplot as plt


N = 20
A = {n:1/((n**2)*np.sinh(3*n*np.pi)) for n in range(1, N) if n%2 == 1}

x_res = 150
y_res = 150

def func(x,y):
    z = sum(A[n] * np.sinh(n*np.pi*(30-y)/10) * np.cos(n*np.pi*x/10) for n in range(1,N) if n%2 == 1)
    return 1/6 * (30 - y) - 40/np.pi**2 * z

x, y = np.meshgrid(np.linspace(0,10,x_res), np.linspace(0,30,y_res))
z = func(x, y)

def plot(clabel='', cmap='', xlabel='', ylabel=''):
    plt.pcolormesh(x, y, z, cmap = cmap)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar().set_label(clabel)
    plt.show()

plot(clabel='Temperature', cmap='afmhot', xlabel='X-axis', ylabel='Y-axis')

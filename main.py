import scipy.signal as ss
import scipy.fft as fft
import matplotlib.pyplot as plt
import numpy as np

"""
Guia 1
"""

def Ej9():
    y_arr1=[0.0, 0.0]
    y_arr2 = [0.0, 0.0]
    y_arr3 = [0.0, 0.0]
    a1=1
    b1=-1/2
    a2=1/2
    b2=-1/8
    a3=5/4
    b3=-25/32

    y_eq= lambda h, x, y, a, b: (x[h]/2) + a * y[h+1] + b*y[h]

    x_unit=ss.unit_impulse(33, 2)

    x_step=[0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    # x_arr=x_step
    x_arr=x_unit

    for i in range(31):
        y_arr1.append(y_eq(i, x_arr, y_arr1, a1, b1))
        y_arr2.append(y_eq(i, x_arr, y_arr2, a2, b2))
        y_arr3.append(y_eq(i, x_arr, y_arr3, a3, b3))

    fig, ax=plt.subplots()
    ax.plot(range(0, 31), x_arr[2:], linestyle="--", marker="o", markersize=3, label=r'Impulso $x(n)$')
    ax.plot(range(0, 31), y_arr1[2:], linestyle="--", marker="o", markersize=3, label=r'$\alpha=1 ; \beta=-1/2$')
    ax.plot(range(0, 31), y_arr2[2:], linestyle="--", marker="o", markersize=3, label=r'$\alpha=1/2 ; \beta=-1/8$')
    ax.plot(range(0, 31), y_arr3[2:], linestyle="--", marker="o", markersize=3, label=r'$\alpha=5/4 ; \beta=-25/32$')

    # plt.title("Respuesta al escalón")
    plt.xlabel("n")
    plt.ylabel(r'$y(n)$')
    plt.legend()
    plt.grid()
    plt.show()

def Ej15():
    # n=np.linspace(0, 100, 100)
    n=np.arange(1000)
    x_n= 2*np.sin(100*n)
    X=fft.fft(x_n)
    freq=fft.fftfreq(x_n.shape[0])

    x_n_M=[]
    M=3
    for i in range(len(x_n)):
        if(i%M==True):
            x_n_M.append(x_n[i])
    x_n_M=np.array(x_n_M)
    X_M=fft.fft(x_n_M)
    freq_M=fft.fftfreq(x_n_M.shape[0])

    """x_recu=[]
    for i in range(len(x_n_M)-1):
        x_recu.append(x_n_M[i])
        x_recu.append((x_n_M[i]+x_n_M[i+1])/2)
    x_recu.append(x_n_M[-1])
    x_recu = np.array(x_recu)
    X_recu=fft.fft(x_recu)
    freq_recu=fft.fftfreq(x_recu.shape[0])"""

    fig, ax = plt.subplots()
    ax.plot(freq, X.real, linestyle="--", linewidth=1, marker="o", markersize=2, label="X(n)")
    ax.plot(freq_M, X_M.real, linestyle="--", linewidth=1, marker="o", markersize=2, label=r'$X_{M=3}(n)$')
    # ax.plot(freq_recu, X_recu.real, linestyle="--", linewidth=1,  marker="o", markersize=2, label="X(n) recuperada")
    plt.grid()
    plt.legend()
    plt.xlabel("Frecuencia")
    plt.ylabel(r'X(n)')
    plt.show()

Ej15()
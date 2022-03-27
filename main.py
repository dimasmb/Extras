import scipy.signal as ss
import matplotlib.pyplot as plt

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


Ej9()
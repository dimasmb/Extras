import matplotlib.pyplot as plt
import numpy as np

T= lambda Rvar, RL: (400e6/(295*Rvar + 1999200)) * (1/(1 + 0.03*(1/Rvar + 1/RL)))

Zia= lambda Rvar: 2e6/(295+1999200/Rvar)
Zoa = lambda Rvar, RL: 75/(1+ (75*(1/Rvar+1/RL))/2500)

Zo = lambda Rvar, RL: Zoa(Rvar, RL)/(1 + T(Rvar, RL))

Zi = lambda Rvar, RL: Zia(Rvar)/(1 + T(Rvar, RL))


pot = np.linspace(0.001, 25000, 10001)
RL = 7

Zores=Zo(pot, RL)

FILE_NAME1="F:\\ITBA\Años\\2022 1C\\E2\\Vvacio.txt"
FILE_NAME2="F:\\ITBA\Años\\2022 1C\\E2\\Vcarga.txt"
vacio = np.genfromtxt(FILE_NAME1, delimiter='\t', skip_header=True)
carga = np.genfromtxt(FILE_NAME2, delimiter='\t', skip_header=True)
x = vacio[:, 0]
y_vacio = vacio[:, 1]
y_carga = carga[:, 1]

Zo_sim=(y_vacio-y_carga)*7/y_carga

fig, ax = plt.subplots()
ax.plot(pot/1000, Zores, label="Teórico")
ax.plot(x/1000, Zo_sim, linestyle=" ", marker=".", label="Simulado")

plt.xlim(0, 25)
plt.ylim(0, 5)
plt.xlabel(r'$R_{var} [k\Omega]$')
plt.ylabel(r'$Z_{output} [\Omega]$')
plt.title(r'$Z_{output}$' + " con " + r'$R_L=$' + str(RL) + r'$\Omega$')
plt.ylim(bottom=0)
plt.legend()
plt.grid()
plt.show()
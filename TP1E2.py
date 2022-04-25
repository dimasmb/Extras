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

fig, ax = plt.subplots()
ax.plot(pot/1000, Zores)
ax.plot([0, 25], [3.12e-3, 1.26])

plt.xlim(0, 25)
plt.xlabel(r'$R_{var} [k\Omega]$')
plt.ylabel(r'$Z_{output} [\Omega]$')
plt.title(r'$Z_{output}$' + " con " + r'$R_L=$' + str(RL) + r'$\Omega$')
plt.ylim(bottom=0)
plt.grid()
plt.show()
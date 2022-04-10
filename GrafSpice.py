
import math
import numpy as np
import matplotlib.pyplot as plt


FILE_NAME="G:\\Mi unidad\\Notas entre compus\\Spice\\SyH_sim.txt"
my_data = np.genfromtxt(FILE_NAME, delimiter='\t', skip_header=True)
# my_data=np.array(my_data)
print(my_data)
x = my_data[:, 0]
y1 = my_data[:, 1]
y2 = my_data[:, 2]


plt.plot(x,y1, label="Señal")
plt.plot(x,y2, label="C=100pF")

plt.grid(which="both")
plt.xlabel("Tiempo[s]")
plt.ylabel("V")
plt.legend()
plt.tight_layout()
plt.show()
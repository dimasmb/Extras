import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME="G:\\Mi unidad\\Notas entre compus\\CSV\\1_SyH+LLA.csv"

headers = ['Tiempo(s)', 'In', 'Out']

df = pd.read_csv(FILE_NAME, names=headers)

df.set_index(headers[0]).plot()

plt.ylabel('V')
plt.xlim(0, 0.0025)
plt.grid(which="both")
plt.show()
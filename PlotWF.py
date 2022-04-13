import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME="G:\\Mi unidad\\Notas entre compus\\CSV\\3_FAA+LLA+FR.csv"

headers = ['Tiempo(s)', 'In', 'Out']

df = pd.read_csv(FILE_NAME, names=headers)

df.set_index(headers[0]).plot()

plt.ylabel('V')
plt.xlim(0, 0.01)
plt.grid(which="both")
plt.show()
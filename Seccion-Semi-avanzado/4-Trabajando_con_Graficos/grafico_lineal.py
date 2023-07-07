import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Seccion-Semi-avanzado\\4-Trabajando_con_Graficos\\pedos.csv")
print(df)

#creando el grafico
sns.lineplot(x="fecha",y="pedos",data=df)

#creando el púnto en el momento mas pedos
plt.plot("01-09",17,"o")

#creando el grafico
plt.show()


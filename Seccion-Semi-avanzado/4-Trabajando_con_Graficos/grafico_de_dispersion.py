import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Seccion-Semi-avanzado\\4-Trabajando_con_Graficos\\dispersion.csv")
print(df)

#creando el grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)

#creando el grafico
plt.show()
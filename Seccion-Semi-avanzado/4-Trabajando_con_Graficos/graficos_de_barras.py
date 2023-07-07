import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Seccion-Semi-avanzado\\4-Trabajando_con_Graficos\\cofra_ingresos.csv")
print(df)

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)          #nos muestra la estadistica en barras

#suma el total de todos sus ingresos
total_de_ingresos = df["ingresos"].sum()

#mostrando el total
print(f"El total de ingreso es de: {total_de_ingresos} USD")

#creando el grafico
plt.show()


import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('./estadistica/housing.csv')

#primeros 5
print (df.head())

#ultimos 5
print (df.tail())

#fila en especifico
print (df.iloc[7])

#columna por su nombre
print (df["ocean_proximity"])

#obtener la media de la columna de total de cuartos
mediacuartos = df ["total_rooms"].mean()
print('Media del total de cuartos', mediacuartos)

#obtener la medaina de la columna population
medianapopularidad = df["population"].median()
print('mediana de popularidad: ', medianapopularidad)

std_age = df["housing_median_age"].std()
print('Desviacion estandar de años: ', std_age)

#para pder fltrar 
filtrodeloceno = df[df["ocean_proximity"]=="ISLAND"]
print('Filtro de aproximidad del oceano: ', filtrodeloceno)

#vamos a crear un grafico de dispersion entre los registros de la prooximidad del oceano vs los precios

plt.scatter(df["ocean_proximity"][:10], df["median_house_value"][:10])

#hay que definir a x y y 
plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Grafico de dispersion de proximidad al oceano vs precio')
plt.show()
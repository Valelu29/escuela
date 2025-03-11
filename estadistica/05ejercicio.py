import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('./estadistica/housing.csv')

media = df['median_house_value'].mean()
print("Media: ", media)

mediana = df['median_house_value'].median()
print("Mediana: ", mediana)

moda = df['median_house_value'].mode()
print("Moda: ", moda)

rango = df['median_house_value'].max()
print("Rango: ", rango)

varianza = df['median_house_value'].var()
print("Varianza: ", varianza)

desviacion_estandar= df['median_house_value'].std()
print("Desviacion estandar: ", desviacion_estandar)

frecuencias = df['median_house_value'].value_counts().sort_index()
print(f"\nMedia: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Rango: {rango}")
print(f"Varianza: {varianza}")
print(f"Desviación Estándar: {desviacion_estandar}")
print("\nTabla de Frecuencias:")
print(frecuencias)


plt.figure(figsize=(10, 6))
plt.bar(df['population'], df['median_house_value'], width=500, color='skyblue')
plt.title("Comparación de Median House Value con Population")
plt.xlabel("Population")
plt.ylabel("Median House Value")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
avg_house_value = df['median_house_value'].mean()
plt.bar([0], [avg_house_value], color='orange')
plt.title("Costo Promedio de Median House Value")
plt.xlabel("Median House Value")
plt.ylabel("Promedio de Median House Value")
plt.tight_layout()
plt.show()
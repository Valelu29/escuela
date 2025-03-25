import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Ventas totales del comercio
ventas_totales = df["ventas_tot"].sum()

# 2. Contar socios con y sin adeudo
socios_con_adeudo = df[df["B_adeudo"] == "Con adeudo"]["no_clientes"].sum()
socios_sin_adeudo = df[df["B_adeudo"] == "Sin adeudo"]["no_clientes"].sum()
total_socios = socios_con_adeudo + socios_sin_adeudo

# Porcentajes
porcentaje_con_adeudo = (socios_con_adeudo / total_socios) * 100
porcentaje_sin_adeudo = (socios_sin_adeudo / total_socios) * 100
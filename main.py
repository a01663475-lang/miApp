import pandas as pd
from figuras import rectangulo, circulo, triangulo
df = pd.read_csv("figuras.csv") 

for index, row in df.iterrows():
	print(f"Fila {index}: FIGURA={row["FIGURA"]}, medida1 = {row["MEDIDA1"]}, medida2 = {row["MEDIDA2"]}")
	if row["FIGURA"] == "c":
		resultado= circulo(float(row["MEDIDA1"]))
	if row["FIGURA"] == "r":
		resultado = rectangulo(float(row["MEDIDA1"]), float(row["MEDIDA2"]))
	if  row["FIGURA"] == "t":
		resultado = triangulo(float(row["MEDIDA1"]), float(row["MEDIDA2"]))
	print(f"Fila {index}: FIGURA={row["FIGURA"]}, medida1 = {row["MEDIDA1"]}, medida2 = {row["MEDIDA2"]}, area = {resultado[0]}, perimetro = {resultado[1]}")

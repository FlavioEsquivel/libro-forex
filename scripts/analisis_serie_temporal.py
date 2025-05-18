import os
import pandas as pd
import matplotlib.pyplot as plt

# Crear carpetas de salida si no existen
os.makedirs("output/graficas", exist_ok=True)
os.makedirs("output/resultados", exist_ok=True)

# Cargar datos
data = pd.read_csv("data/EURUSD.csv", parse_dates=["Date"], index_col="Date")

# Estadísticas básicas
mean_close = data["Close"].mean()
std_close = data["Close"].std()

# Guardar estadísticas en un archivo de texto
with open("output/resultados/estadisticas.txt", "w") as f:
    f.write(f"Media precio cierre: {mean_close:.5f}\n")
    f.write(f"Desviación estándar: {std_close:.5f}\n")

# Calcular media móvil
data["SMA20"] = data["Close"].rolling(window=20).mean()

# Crear gráfico
plt.figure(figsize=(12, 6))
plt.plot(data["Close"], label="Precio Cierre")
plt.plot(data["SMA20"], label="SMA 20 días")
plt.title("EUR/USD: Precio Cierre y Media Móvil (SMA 20)")
plt.xlabel("Fecha")
plt.ylabel("Precio")
plt.legend()

# Guardar la gráfica con nombre descriptivo
plt.savefig("output/graficas/eurusd_sma20.png")
print("Gráfica guardada en: output/graficas/eurusd_sma20.png")

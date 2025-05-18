# Capítulo 1: Introducción al Forex

## 1.1 ¿Qué es el mercado Forex?

El mercado Forex (Foreign Exchange Market) es el mercado global descentralizado donde se negocian divisas de diferentes países. Es el mercado financiero más grande del mundo con un volumen diario que supera los 6 trillones de dólares (datos 2023).

- **Características principales:**
  - Operación 24 horas, 5 días a la semana.
  - Liquidez extrema.
  - Participantes: bancos centrales, fondos de inversión, brokers, traders individuales.

El Forex permite convertir una divisa en otra, y los precios son determinados por la oferta y demanda global.

---

## 1.2 Pares de divisas y cotizaciones

Las divisas se negocian en pares, por ejemplo: EUR/USD, USD/JPY, GBP/USD. La primera divisa es la base, la segunda es la cotizada.

- **Cotización:** es el precio al que se puede comprar o vender el par.
- **Bid:** precio para vender la base.
- **Ask:** precio para comprar la base.
- **Spread:** diferencia entre ask y bid.

**Ejemplo:** Si EUR/USD tiene bid=1.1010 y ask=1.1012, el spread es 0.0002 (2 pips).

---

## 1.3 Conceptos básicos de trading

- **Lote:** cantidad estándar para operar, generalmente 100,000 unidades de la divisa base.
- **Apalancamiento:** permite controlar una posición mayor con menos capital (ej. 1:100).
- **Margen:** capital necesario para abrir una posición apalancada.

**Órdenes:**

- Orden de mercado: se ejecuta inmediatamente al precio actual.
- Orden límite: se ejecuta cuando el precio alcanza un nivel específico.
- Orden stop: se usa para limitar pérdidas o asegurar ganancias.

---

## 1.4 Matemáticas básicas para Forex

### Media y Varianza

La media es el promedio de un conjunto de precios \( x_1, x_2, ..., x_n \):

\[
\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i
\]

La varianza mide la dispersión:

\[
\sigma^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2
\]

La desviación estándar es la raíz cuadrada de la varianza:

\[
\sigma = \sqrt{\sigma^2}
\]

### Correlación

Para dos series \(X = \{x_i\}\) y \(Y = \{y_i\}\), la correlación de Pearson es:

\[
\rho_{X,Y} = \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2} \sqrt{\sum (y_i - \bar{y})^2}}
\]

Va entre -1 y 1, indicando fuerza y dirección de relación lineal.

---

## 1.5 Series temporales

Los precios Forex se pueden ver como una serie temporal \( \{p_t\} \), donde \(t\) es el tiempo.

Modelos simples para analizar series temporales incluyen:

- **Media móvil (MA):**

\[
MA_t = \frac{1}{m} \sum_{i=0}^{m-1} p_{t-i}
\]

- **Modelos autorregresivos (AR):**

\[
p_t = c + \sum_{i=1}^k \phi_i p_{t-i} + \epsilon_t
\]

donde \(\epsilon_t\) es ruido blanco (valores aleatorios con media cero y varianza constante).

---

## Código de ejemplo: Estadísticas básicas y visualización

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos históricos de EUR/USD
data = pd.read_csv("data/EURUSD.csv", parse_dates=['Date'], index_col='Date')

# Calcular media y desviación estándar del precio de cierre
mean_close = data['Close'].mean()
std_close = data['Close'].std()

print(f"Media precio cierre: {mean_close:.5f}")
print(f"Desviación estándar: {std_close:.5f}")

# Graficar precio de cierre y media móvil simple (SMA 20)
data['SMA20'] = data['Close'].rolling(window=20).mean()

plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Precio Cierre')
plt.plot(data['SMA20'], label='SMA 20 días')
plt.title('EUR/USD Precio Cierre y SMA 20')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.legend()
plt.show()

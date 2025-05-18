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

### 1.2.1 Definición y estructura de un par de divisas

En el mercado Forex, las divisas se negocian siempre en pares, donde la primera divisa es la **moneda base** y la segunda es la **moneda cotizada**. Por ejemplo:

$$
\text{EUR/USD} = \frac{\text{USD}}{1 \text{ EUR}}
$$

Esto significa que el precio del par indica cuántos dólares estadounidenses (USD) se necesitan para comprar 1 euro (EUR).

En este capítulo usaremos siempre la notación estándar de moneda base seguida por moneda cotizada, como en EUR/USD.

---

### 1.2.2 Precios Bid, Ask y Spread

- **Bid:** precio para vender la moneda base (EUR).
- **Ask:** precio para comprar la moneda base (EUR).
- **Spread:** diferencia entre Ask y Bid.

Por ejemplo, si el par EUR/USD tiene:

- \(P_{bid} = 1.1010\)
- \(P_{ask} = 1.1012\)

El spread es \(0.0002\) USD o 2 pips.

---

### 1.2.3 ¿Qué significa comprar o vender EUR/USD?

- **Comprar EUR/USD:** significa comprar euros pagando dólares al precio Ask.
- **Vender EUR/USD:** significa vender euros recibiendo dólares al precio Bid.

Ejemplo: para comprar 1,000 euros al Ask 1.1012 pagarás:

$$
1000 \times 1.1012 = 1101.2 \text{ USD}
$$

Para vender 1,000 euros al Bid 1.1010 recibirás:

$$
1000 \times 1.1010 = 1101.0 \text{ USD}
$$

---

### 1.2.4 Impacto del spread en las operaciones

La diferencia entre el precio de compra y venta implica un costo para el trader, que se calcula como:

$$
\text{Costo por spread} = Q \times (P_{ask} - P_{bid})
$$

donde \(Q\) es la cantidad en euros.

---

### 1.2.5 Ejercicios prácticos

1. Si compras 5,000 euros a \(P_{ask} = 1.1012\) y los vendes inmediatamente a \(P_{bid} = 1.1010\), ¿cuál es la pérdida por spread?

2. Para el par EUR/USD con un spread de 3 pips, calcula el costo para una operación de 10,000 euros.

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

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i
$$

La varianza mide la dispersión:

$$
\sigma^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2
$$

La desviación estándar es la raíz cuadrada de la varianza:

$$
\sigma = \sqrt{\sigma^2}
$$

### Correlación

Para dos series \(X = \{x_i\}\) y \(Y = \{y_i\}\), la correlación de Pearson es:

$$
\rho_{X,Y} = \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2} \sqrt{\sum (y_i - \bar{y})^2}}
$$

Va entre -1 y 1, indicando fuerza y dirección de relación lineal.

---

## 1.5 Series temporales

Los precios Forex se pueden ver como una serie temporal \( \{p_t\} \), donde \(t\) es el tiempo.

Modelos simples para analizar series temporales incluyen:

- **Media móvil (MA):**

$$
MA_t = \frac{1}{m} \sum_{i=0}^{m-1} p_{t-i}
$$

- **Modelos autorregresivos (AR):**

$$
p_t = c + \sum_{i=1}^k \phi_i p_{t-i} + \epsilon_t
$$

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

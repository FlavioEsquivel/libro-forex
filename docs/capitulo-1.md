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
\operatorname{EUR/USD} = \frac{\operatorname{USD}}{1\, \operatorname{EUR}}
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
1000 \times 1.1012 = 1101.2 \mathrm{ USD}
 $$

Para vender 1,000 euros al Bid 1.1010 recibirás:

$$ 
1000 \times 1.1010 = 1101.0 \mathrm{ USD}
 $$

---

### 1.2.4 Impacto del spread en las operaciones

La diferencia entre el precio de compra y venta implica un costo para el trader, que se calcula como:

$$ 
\mathrm{Costo por spread} = Q \times (P_{ask} - P_{bid})
 $$

donde \(Q\) es la cantidad en euros.

---

### 1.2.5 Ejercicios prácticos

1. Si compras 5,000 euros a \(P_{ask} = 1.1012\) y los vendes inmediatamente a \(P_{bid} = 1.1010\), ¿cuál es la pérdida por spread?

2. Para el par EUR/USD con un spread de 3 pips, calcula el costo para una operación de 10,000 euros.

---

## 1.3 Conceptos básicos de trading

El trading en Forex implica una combinación de conocimientos técnicos, estratégicos y una comprensión clara de los términos fundamentales. En esta sección se exploran en profundidad los elementos básicos del trading para cimentar una base sólida.

---

### 1.3.1 Lote

Un **lote** es la unidad estándar para medir la cantidad de divisa que se negocia en una operación. Existen tres tamaños de lote comúnmente utilizados:

- **Lote estándar:** 100,000 unidades de la divisa base.
- **Mini lote:** 10,000 unidades.
- **Micro lote:** 1,000 unidades.

> Por ejemplo, al operar un lote estándar en el par EUR/USD, estás comprando o vendiendo 100,000 euros.

**Importancia del lote:**  
El tamaño del lote influye directamente en el nivel de riesgo y en la magnitud del beneficio o pérdida. Una variación de un pip en un lote estándar equivale a aproximadamente **10 USD**. Por tanto, un movimiento de 50 pips a tu favor supondría 500 USD de ganancia (o pérdida, si es en contra).

---

### 1.3.2 Apalancamiento

El **apalancamiento financiero** permite controlar una posición más grande con un capital menor. Se expresa como una proporción:

- Ejemplo: apalancamiento 1:100 significa que por cada 1 USD de capital propio puedes controlar 100 USD del mercado.

> Esto implica que con 1,000 USD puedes abrir una posición de hasta 100,000 USD.

**Ventajas y riesgos:**

- ✅ Aumenta el potencial de ganancias.
- ❌ También aumenta el riesgo de pérdidas, ya que amplifica los movimientos del mercado.

El uso adecuado del apalancamiento requiere una gestión estricta del riesgo. Un apalancamiento alto mal gestionado puede llevar rápidamente a una **liquidación automática** de la cuenta.

---

### 1.3.3 Margen

El **margen** es el capital requerido como garantía para abrir una posición apalancada. No se trata de un costo, sino de una retención temporal de capital.

$$ 
\mathrm{Margen requerido} = \frac{\mathrm{Tamaño de la operación}}{\mathrm{Apalancamiento}}
 $$

> Por ejemplo, para abrir una posición de 100,000 USD con apalancamiento 1:100 necesitas un margen de:

$$ 
\frac{100,000}{100} = 1,000 \mathrm{ USD}
 $$

**Margen de mantenimiento:** Es el mínimo que debes tener en la cuenta para mantener una posición abierta. Si tu capital cae por debajo de ese nivel, se produce una **margin call**, y tus operaciones pueden cerrarse automáticamente.

---

### 1.3.4 Tipos de órdenes

Las **órdenes** son instrucciones que se dan a la plataforma de trading para abrir o cerrar operaciones en condiciones específicas. Son herramientas clave en la estrategia y gestión de riesgo.

#### a. Orden de mercado

- Se ejecuta **inmediatamente** al mejor precio disponible.
- Garantiza ejecución, pero no un precio exacto.
- Ideal en mercados muy líquidos o cuando la prioridad es entrar/salir rápidamente.

#### b. Orden límite (Limit Order)

- Se coloca a un precio **mejor que el actual** del mercado.
- Útil para entrar al mercado cuando se alcanza un nivel técnico deseado.
- Ejemplo: si EUR/USD está en 1.1010 y deseas comprar en 1.1000, puedes colocar una orden límite de compra.

#### c. Orden stop (Stop Order)

- Se activa cuando el precio **supera un cierto umbral**.
- Útil para:
  - **Detener pérdidas** (stop-loss).
  - **Asegurar ganancias** (trailing stop).
  - Entrar en operaciones si se rompe una resistencia o soporte (buy/sell stop).

---

### 1.3.5 Ejemplo de operación combinando conceptos

Supongamos que deseas comprar 1 lote de EUR/USD (100,000 euros) con un apalancamiento 1:100. El precio actual es 1.1010.

- Margen requerido:  
  $$ 
  \frac{100,000}{100} = 1,000 \mathrm{ USD}
   $$

- Colocas una orden límite de compra en 1.1000 con un stop-loss en 1.0950 y un take-profit en 1.1100.

- Si se ejecuta y alcanza el TP:
  $$ 
  (1.1100 - 1.1000) \times 100,000 = 1,000 \mathrm{ USD de ganancia}
   $$

- Si cae al SL:
  $$ 
  (1.1000 - 1.0950) \times 100,000 = 500 \mathrm{ USD de pérdida}
   $$

Este ejemplo demuestra cómo el lote, el apalancamiento, el margen y las órdenes se combinan en una operación real.

---

### 1.3.6 Gestión del riesgo y del capital

- Nunca uses todo tu capital como margen.
- Limita el riesgo por operación (por ejemplo, 1-2% del capital total).
- Usa órdenes stop-loss siempre.
- Diversifica: no expongas toda tu cuenta a una sola operación o par.

---

### 1.3.7 Psicología del trading

Aunque no es un concepto técnico, la **disciplina emocional** es clave. Los errores más comunes suelen ser:

- Operar impulsivamente sin análisis.
- Mover el stop-loss por miedo.
- Sobreapalancarse por codicia.

La combinación de **educación técnica**, **gestión del riesgo**, y **control emocional** es lo que define a un trader exitoso.


---

## 1.4 Matemáticas básicas para Forex

El trading en Forex no es solo cuestión de intuición o suerte, sino que se basa en el análisis riguroso de datos históricos y actuales. Para ello, es fundamental comprender algunos conceptos matemáticos básicos que permiten interpretar y predecir el comportamiento de los precios.

---

### Media y Varianza

#### 1. Media aritmética

La **media aritmética** es la medida estadística más común que resume un conjunto de datos mediante un único valor representativo. En Forex, se utiliza para analizar precios históricos, como precios de cierre, máximos o mínimos.

Para un conjunto de precios \( x_1, x_2, \dots, x_n \), la media se calcula como:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i
$$

**Interpretación:**  
- La media nos indica el valor "central" o esperado de la serie de precios.
- En análisis técnico, la media móvil (simple o ponderada) es una herramienta que suaviza las fluctuaciones del mercado para detectar tendencias.

#### 2. Varianza

La **varianza** es una medida que cuantifica la dispersión o variabilidad de los datos respecto a la media:

$$
\sigma^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2
$$

**Interpretación:**  
- Una varianza alta indica que los precios tienen grandes fluctuaciones, es decir, el activo es volátil.
- Una varianza baja indica precios más estables.
- En Forex, la varianza es clave para gestionar el riesgo: activos con alta varianza pueden ofrecer mayores oportunidades, pero también mayores pérdidas.

#### 3. Desviación estándar

La **desviación estándar** es la raíz cuadrada de la varianza:

$$
\sigma = \sqrt{\sigma^2} = \sqrt{\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2}
$$

Esta métrica mantiene las unidades originales de los datos (por ejemplo, dólares).

**Importancia en Forex:**  
- Permite definir rangos de volatilidad, por ejemplo, para construir indicadores como las Bandas de Bollinger, que muestran zonas de sobrecompra o sobreventa.
- Ayuda a calcular el riesgo y determinar niveles apropiados para órdenes de stop-loss.

---

### Correlación

La **correlación de Pearson** mide la fuerza y dirección de una relación lineal entre dos variables aleatorias, que en Forex suelen ser series temporales de precios de distintos pares de divisas.

Para dos series \( X = \{x_1, \dots, x_n\} \) y \( Y = \{y_1, \dots, y_n\} \), la correlación es:

$$
\rho_{X,Y} = \frac{\mathrm{cov}(X,Y)}{\sigma_X \sigma_Y}
= \frac{
\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})
}{
\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \cdot \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}
}
$$

Donde:  
- \( \mathrm{cov}(X,Y) \) es la covarianza entre \( X \) y \( Y \), que indica cómo varían conjuntamente.
- \( \sigma_X \) y \( \sigma_Y \) son las desviaciones estándar de cada serie.

**Interpretación:**  
- \( \rho = 1 \): correlación positiva perfecta (ambos activos se mueven en la misma dirección y proporción).
- \( \rho = -1 \): correlación negativa perfecta (se mueven en direcciones opuestas).
- \( \rho = 0 \): no existe correlación lineal.

**Aplicación práctica:**  
- Identificar pares de divisas que se mueven juntos para diversificar o para estrategias de cobertura.
- Predecir movimientos de un par a partir de otro correlacionado.

---

### Aplicaciones avanzadas en Forex

#### Media móvil y su importancia

La media móvil suaviza las series de precios, eliminando ruido para detectar tendencias a corto, mediano y largo plazo.

- **Media móvil simple (SMA):** promedio aritmético móvil.
- **Media móvil exponencial (EMA):** pondera más los precios recientes, respondiendo mejor a cambios recientes.

Se usa en sistemas de trading para generar señales de compra y venta (cruces de medias móviles).

#### Volatilidad y gestión del riesgo

La desviación estándar es la base para medir volatilidad, que es clave para:

- Ajustar tamaños de posición.
- Definir niveles de stop-loss con un margen adecuado para evitar salidas prematuras por fluctuaciones normales.
- Establecer expectativas sobre posibles movimientos de precio.

#### Correlación para portafolios Forex

La correlación es crucial para crear portafolios balanceados:

- Combinar activos con baja o negativa correlación puede reducir el riesgo total.
- Un trader puede evitar posiciones redundantes en pares que se mueven casi idénticamente.

---

### Ejemplos numéricos

Supongamos los precios diarios de cierre de EUR/USD durante 5 días:

| Día | Precio (USD) |
|------|------------|
| 1    | 1.1000     |
| 2    | 1.1020     |
| 3    | 1.0980     |
| 4    | 1.1050     |
| 5    | 1.1070     |

- **Media:**

$$
\bar{x} = \frac{1.1000 + 1.1020 + 1.0980 + 1.1050 + 1.1070}{5} = 1.1024
$$

- **Varianza:**

$$
\sigma^2 = \frac{(1.1000 - 1.1024)^2 + (1.1020 - 1.1024)^2 + \dots + (1.1070 - 1.1024)^2}{5} = 7.04 \times 10^{-6}
$$

- **Desviación estándar:**

$$
\sigma = \sqrt{7.04 \times 10^{-6}} = 0.00265
$$

Esto indica que la volatilidad diaria promedio es aproximadamente 0.00265 USD.

---

### Resumen

Estos conceptos matemáticos son fundamentales para cualquier trader serio de Forex. Permiten cuantificar el riesgo, identificar oportunidades y construir estrategias basadas en datos objetivos y no en conjeturas.

---

**Ejercicio práctico:**  
Calcula la media, varianza y correlación de los precios históricos de dos pares de divisas y analiza cómo esta información podría influir en tus decisiones de trading.

---

## Fórmulas clave

| Concepto           | Fórmula                                                                                 |
|--------------------|-----------------------------------------------------------------------------------------|
| Media aritmética    | \( \displaystyle \bar{x} = \frac{1}{n} \sum_{i=1}^n x_i \)                            |
| Varianza           | \( \displaystyle \sigma^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2 \)              |
| Desviación estándar | \( \displaystyle \sigma = \sqrt{\sigma^2} \)                                           |
| Correlación        | \( \displaystyle \rho_{X,Y} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i-\bar{x})^2}\sqrt{\sum (y_i-\bar{y})^2}} \) |


---

# 1.5 Series temporales

Los precios Forex se pueden modelar y analizar como una **serie temporal** \( \{p_t\} \), donde \(t\) representa el tiempo (por ejemplo, días, minutos o segundos). El análisis de series temporales permite detectar patrones, tendencias, ciclos y volatilidad en los precios que son esenciales para la toma de decisiones en trading.

---

## Conceptos básicos

- **Serie temporal:** secuencia de datos ordenada en el tiempo.
- **Estacionariedad:** propiedad de una serie donde sus estadísticas (media, varianza) son constantes a lo largo del tiempo.
- **Ruido blanco:** una serie de valores aleatorios con media cero y varianza constante, sin autocorrelación.
- **Autocorrelación:** medida de correlación entre valores de la serie en diferentes tiempos.

---

## Modelos simples para analizar series temporales

### Media móvil (MA)

La media móvil suaviza las fluctuaciones cortas y resalta tendencias a largo plazo:

$$
MA_t = \frac{1}{m} \sum_{i=0}^{m-1} p_{t-i}
$$

donde \(m\) es la ventana de tiempo (por ejemplo, 20 días).

### Modelos autorregresivos (AR)

Un modelo AR de orden \(k\) expresa el valor actual como función lineal de los \(k\) valores anteriores más un término de error:

$$
p_t = c + \sum_{i=1}^k \phi_i p_{t-i} + \epsilon_t
$$

- \(c\): constante
- \(\phi_i\): coeficientes de autoregresión
- \(\epsilon_t\): ruido blanco

---

## Modelos para volatilidad: GARCH

Los precios financieros no solo muestran tendencia, sino que su volatilidad cambia con el tiempo. Los modelos GARCH (Generalized Autoregressive Conditional Heteroskedasticity) capturan estas variaciones de volatilidad condicional.

El modelo GARCH(1,1) más común se define como:

$$
\sigma_t^2 = \alpha_0 + \alpha_1 \epsilon_{t-1}^2 + \beta_1 \sigma_{t-1}^2
$$

- \(\sigma_t^2\): varianza condicional en el tiempo \(t\)
- \(\epsilon_t\): innovación (residual) en el tiempo \(t\)
- \(\alpha_0, \alpha_1, \beta_1\): parámetros del modelo (todos positivos y \(\alpha_1 + \beta_1 < 1\))

Este modelo captura la "heteroscedasticidad condicional", es decir, que la varianza cambia con el tiempo dependiendo de eventos pasados.

---

## Ejemplo en Python: Análisis y modelado con GARCH

```python
# Archivo analisis_serie_temporal.py
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
```

---

## Explicación del código

1. **Cálculo de log-retornos:** Es usual trabajar con retornos logarítmicos para modelar series financieras, ya que estabilizan la varianza y convierten multiplicaciones en sumas.
2. **Visualización:** Graficamos el precio y sus retornos para observar patrones y volatilidad.
3. **Modelo GARCH:** Ajustamos un modelo GARCH(1,1) para capturar la volatilidad variable.
4. **Resultados:** Se muestra un resumen del ajuste y una gráfica de la volatilidad estimada en el tiempo.

---

## Conclusión

El análisis de series temporales en Forex es fundamental para entender la dinámica de los precios y la volatilidad. Desde métodos simples como medias móviles hasta modelos avanzados como GARCH, las herramientas estadísticas permiten tomar mejores decisiones en trading y gestión de riesgos.

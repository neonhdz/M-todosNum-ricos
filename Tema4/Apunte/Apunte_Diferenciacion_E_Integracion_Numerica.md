# Unidad 4: Diferenciación e Integración Numérica

En la ingeniería y las ciencias aplicadas, a menudo nos encontramos con funciones que son extremadamente complejas o imposibles de integrar/derivar mediante métodos analíticos tradicionales (por ejemplo, $\int e^{-x^2} dx$). En otros casos, ni siquiera poseemos una función explícita, sino un conjunto de datos tabulados provenientes de mediciones experimentales. Para estos escenarios, los métodos numéricos son la herramienta indispensable.

---

## 4.1 Diferenciación Numérica

La diferenciación numérica aproxima la derivada de una función utilizando los valores de la función en puntos cercanos, basándose en la expansión de la Serie de Taylor.

### Fórmulas de Diferencias Finitas
Si tenemos un tamaño de paso $h$ pequeño:

1. **Diferencia hacia adelante:** $$f'(x) \approx \frac{f(x+h) - f(x)}{h}$$
2. **Diferencia hacia atrás:** $$f'(x) \approx \frac{f(x) - f(x-h)}{h}$$
3. **Diferencia central (La más exacta):** $$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$$

---

## 4.2 Integración Numérica

La integración numérica (o cuadratura) aproxima el valor de la integral definida $\int_{a}^{b} f(x) dx$ calculando el área bajo la curva mediante figuras geométricas conocidas (trazos polinomiales).

### 1. Método del Trapecio
Este método aproxima la función $f(x)$ mediante una línea recta entre intervalos. Si dividimos el intervalo $[a, b]$ en $n$ subintervalos de ancho $h = \frac{b-a}{n}$, la fórmula de aplicación múltiple es:

$$I \approx \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$

- **Ventaja:** Funciona con cualquier cantidad de intervalos.
- **Desventaja:** Su error de truncamiento es relativamente alto frente a curvas pronunciadas.

### 2. Regla de Simpson 1/3
En lugar de rectas, la Regla de Simpson aproxima la función usando parábolas (polinomios de segundo grado). Para aplicarla, el número de subintervalos $n$ **debe ser par**.

$$I \approx \frac{h}{3} \left[ f(x_0) + 4 \sum_{i=1, 3, 5...}^{n-1} f(x_i) + 2 \sum_{j=2, 4, 6...}^{n-2} f(x_j) + f(x_n) \right]$$

- **Ventaja:** Extremadamente exacta para polinomios de hasta tercer grado.

### 3. Cuadratura Gaussiana (Método de Gauss-Legendre)
A diferencia de los métodos de Newton-Cotes (Trapecio y Simpson) que usan puntos equiespaciados, la Cuadratura Gaussiana elige estratégicamente los puntos de evaluación y sus "pesos" para minimizar el error, logrando integraciones exactas con menos evaluaciones de la función.

Primero, se debe realizar un cambio de variable para trasladar los límites de integración originales $[a, b]$ al dominio normalizado $[-1, 1]$ usando la transformación de $x$ a $t$:

$$x = \frac{b-a}{2}t + \frac{b+a}{2}$$
$$dx = \frac{b-a}{2} dt$$

La integral se aproxima mediante la suma ponderada:
$$I \approx \frac{b-a}{2} \sum_{i=1}^{n} w_i f(t_i)$$

**Para una fórmula de 2 puntos ($n=2$):**
- Puntos: $t_1 = -\frac{1}{\sqrt{3}} \approx -0.57735$, $t_2 = \frac{1}{\sqrt{3}} \approx 0.57735$
- Pesos: $w_1 = 1$, $w_2 = 1$

---

## 4.3 Problemario a Entregar (Ejercicios Desarrollados)

Este problemario documenta el análisis y resolución de problemas prácticos empleando las herramientas vistas.

### Problema 1: Aplicación de Diferenciación Numérica (Cinemática)
**Enunciado:** Un sensor óptico mide la posición $x(t)$ de un pistón en milímetros en distintos instantes de tiempo $t$ (segundos). Se obtienen los siguientes datos tabulados:
- $t = [0.0, 0.1, 0.2, 0.3, 0.4]$
- $x = [0.0, 1.2, 3.5, 6.1, 8.8]$

Estime la velocidad (derivada de la posición $v = \frac{dx}{dt}$) en $t = 0.2$ s usando diferencias finitas centrales.

**Desarrollo:**
El paso es $h = 0.1$.
La fórmula de diferencia central es:
$$v(0.2) \approx \frac{x(0.2 + 0.1) - x(0.2 - 0.1)}{2(0.1)}$$
$$v(0.2) \approx \frac{x(0.3) - x(0.1)}{0.2} = \frac{6.1 - 1.2}{0.2} = \frac{4.9}{0.2}$$
**Resultado:** $v(0.2) = 24.5$ mm/s.

---

### Problema 2: Comparativa de Integración (Trabajo Mecánico)
**Enunciado:** Se requiere calcular el trabajo $W$ realizado por un gas que se expande de un volumen de 2 m³ a 6 m³. La relación presión-volumen se modela mediante la función no lineal:
$$P(V) = 50 \ln(V) + \frac{20}{V}$$
(Presión en kPa). El trabajo se define como $W = \int_{2}^{6} P(V) dV$. Calcule el trabajo utilizando el Método del Trapecio y la Regla de Simpson 1/3, ambos con $n=4$ intervalos.

**Desarrollo:**
Paso $h = \frac{6-2}{4} = 1$.
Evaluación de puntos $x_i$:
- $V_0 = 2 \rightarrow P(2) = 50 \ln(2) + 10 = 44.657$
- $V_1 = 3 \rightarrow P(3) = 50 \ln(3) + 6.666 = 61.597$
- $V_2 = 4 \rightarrow P(4) = 50 \ln(4) + 5 = 74.314$
- $V_3 = 5 \rightarrow P(5) = 50 \ln(5) + 4 = 84.471$
- $V_4 = 6 \rightarrow P(6) = 50 \ln(6) + 3.333 = 92.921$

**Cálculo por Trapecio:**
$$W_{trap} = \frac{1}{2} [44.657 + 2(61.597 + 74.314 + 84.471) + 92.921]$$
$$W_{trap} = 0.5 [44.657 + 440.764 + 92.921] = 289.171 \text{ kJ}$$

**Cálculo por Simpson 1/3:**
$$W_{simp} = \frac{1}{3} [44.657 + 4(61.597 + 84.471) + 2(74.314) + 92.921]$$
$$W_{simp} = \frac{1}{3} [44.657 + 584.272 + 148.628 + 92.921] = 290.159 \text{ kJ}$$

**Análisis:** La Regla de Simpson ofrece un resultado más refinado al absorber la curvatura logarítmica de la función de presión de manera más precisa que las rectas del método del trapecio.

---

### Problema 3: Integración Avanzada mediante Cuadratura Gaussiana
**Enunciado:** Estime la integral $\int_{1}^{3} e^{-x^2} dx$ empleando Cuadratura Gaussiana de 2 puntos.

**Desarrollo:**
Límites originales: $a=1, b=3$.
1. **Cambio de variable:**
$$x = \frac{3-1}{2}t + \frac{3+1}{2} = t + 2$$
$$dx = \frac{3-1}{2} dt = 1 dt$$

2. **Nueva integral en función de t:**
$$I \approx \int_{-1}^{1} e^{-(t+2)^2} dt$$

3. **Aplicación de Gauss-Legendre (2 puntos):**
Evaluamos la nueva función en los puntos $t_1 = -0.57735$ y $t_2 = 0.57735$, recordando que los pesos son $1$.

- Evaluando en $t_1$:
$$f(-0.57735) = e^{-(-0.57735+2)^2} = e^{-(1.42265)^2} = e^{-2.0239} = 0.1321$$

- Evaluando en $t_2$:
$$f(0.57735) = e^{-(0.57735+2)^2} = e^{-(2.57735)^2} = e^{-6.6427} = 0.0013$$

4. **Suma ponderada:**
$$I \approx (1)(0.1321) + (1)(0.0013) = 0.1334$$

**Resultado:** La integral es aproximadamente **0.1334**. Este método demuestra su poder al transformar un problema intratable analíticamente en unas pocas operaciones aritméticas de alta precisión.


## Código contenido en:

https://github.com/neonhdz/M-todosNum-ricos/tree/main/Tema4/Code

## Problemario contenido en: 

https://github.com/neonhdz/M-todosNum-ricos/tree/main/Tema4/Problemario

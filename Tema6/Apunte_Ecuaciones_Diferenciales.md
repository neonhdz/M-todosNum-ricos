# Unidad 6: Solución Numérica de Ecuaciones Diferenciales Ordinarias (EDO)

Esta unidad se enfoca en el desarrollo, análisis y programación de algoritmos numéricos para resolver problemas de condiciones iniciales descritos por ecuaciones diferenciales ordinarias. Estos métodos son fundamentales en ingeniería cuando las ecuaciones no poseen soluciones analíticas exactas debido a términos no lineales o geometrías complejas.

---

## 6.1 Fundamentos de Ecuaciones Diferenciales

Una **Ecuación Diferencial Ordinaria (EDO)** es una ecuación que establece una relación entre una variable independiente $t$ (a menudo el tiempo), una función desconocida $y(t)$ y una o más de sus derivadas ($y', y'', \dots, y^{(n)}$).

### Conceptos Clave:
1. **Orden:** Es el orden de la derivada más alta presente en la ecuación.
2. **Grado:** Es el exponente algebraico de la derivada de mayor orden.
3. **Linealidad:** Una EDO es lineal si la variable dependiente $y$ y todas sus derivadas aparecen de forma lineal (elevadas a la primera potencia y no multiplicadas entre sí ni contenidas dentro de funciones no lineales como $\sin(y)$ o $e^y$).

### Problemas de Valores Iniciales (PVI) vs. Valores de Frontera (PVF):
- **Problema de Valores Iniciales (PVI):** Las condiciones necesarias para resolver la EDO se especifican todas en un **único punto inicial** común (por ejemplo, $y(t_0) = y_0$, $y'(t_0) = y'_0$). Es el enfoque principal de los métodos de un solo paso y de pasos múltiples.
- **Problema de Valores de Frontera (PVF):** Las condiciones se especifican en **puntos diferentes** del dominio (por ejemplo, $y(0) = 0$ y $y(L) = 5$). Requieren métodos distintos como el método de disparo o de diferencias finitas.

Formulación estándar de un PVI de primer orden:
$$\frac{dy}{dt} = f(t, y), \quad \text{con la condición inicial } y(t_0) = y_0$$

---

## 6.2 Métodos de Un Solo Paso

Los métodos de un solo paso calculan el valor estimado del siguiente punto de la solución, $y_{i+1}$, utilizando **únicamente la información del punto inmediatamente anterior** $(t_i, y_i)$.

### 1. Método de Euler
Es el algoritmo más simple. Utiliza la pendiente al inicio del intervalo como una aproximación de la pendiente promedio en todo el paso de tamaño $h$.

**Fórmula de Recurrencia:**
$$y_{i+1} = y_i + h \cdot f(t_i, y_i)$$
$$t_{i+1} = t_i + h$$

- **Error de Truncamiento Global:** $\mathcal{O}(h)$ (Método de primer orden; requiere pasos muy pequeños para ser preciso).

### 2. Método de Euler Mejorado (Método de Heun)
Es un método de Predictor-Corrector que mejora la precisión promediando las pendientes al inicio y al final estimado del intervalo.

1. **Paso de Predicción (Euler Estándar):**
   $$u_{i+1} = y_i + h \cdot f(t_i, y_i)$$
2. **Paso de Corrección (Promedio de pendientes):**
   $$y_{i+1} = y_i + \frac{h}{2} \left[ f(t_i, y_i) + f(t_{i+1}, u_{i+1}) \right]$$

- **Error de Truncamiento Global:** $\mathcal{O}(h^2)$ (Método de segundo orden).

### 3. Método de Runge-Kutta de Cuarto Orden (RK4)
Es el método clásico por excelencia en la ingeniería debido a su altísima precisión y balance de cómputo. Evalúa cuatro pendientes combinadas de manera ponderada en diferentes puntos del intervalo.

**Fórmula de Recurrencia:**
$$y_{i+1} = y_i + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

Donde los componentes de pendiente son:
- $k_1 = f(t_i, y_i)$
- $k_2 = f\left(t_i + \frac{h}{2}, y_i + \frac{h}{2}k_1\right)$
- $k_3 = f\left(t_i + \frac{h}{2}, y_i + \frac{h}{2}k_2\right)$
- $k_4 = f(t_i + h, y_i + h k_3)$

- **Error de Truncamiento Global:** $\mathcal{O}(h^4)$ (Método de cuarto orden).

---

## 6.3 Métodos de Pasos Múltiples

A diferencia de los métodos de un solo paso, los **métodos de pasos múltiples** guardan en memoria la información de varios puntos calculados previamente ($y_i, y_{i-1}, y_{i-2}, \dots$) para proyectar una aproximación polinomial de mayor orden del siguiente punto $y_{i+1}$.

### Esquema Adams-Bashforth (Explícito de 2 pasos):
Requiere conocer un punto inicial $y_0$ y un primer paso calculado con un método de un solo paso (como RK4) $y_1$. A partir de ahí, calcula el siguiente mediante:

$$y_{i+1} = y_i + \frac{h}{2} \left[ 3f(t_i, y_i) - f(t_{i-1}, y_{i-1}) \right]$$

- **Ventaja:** Requiere menos evaluaciones directas de la función $f(t,y)$ por cada paso que un método como RK4, haciéndolo computacionalmente eficiente en sistemas complejos.

---

## 6.4 Ejercicio Práctico Resuelto (Análisis Comparativo)

### Problema de Aplicación:
Un tanque cilíndrico drena fluido a través de un orificio en su base. El cambio de la altura del fluido $y$ respecto al tiempo $t$ se modela mediante el siguiente PVI:

$$\frac{dy}{dt} = -0.2 \sqrt{y}, \quad \text{con condición inicial } y(0) = 4\text{ metros}$$

Determine la altura del fluido a los $t = 1.0$ segundo utilizando un tamaño de paso $h = 0.5$ s mediante los métodos de **Euler**, **Heun** y **RK4**.

### Solución Analítica Exacta (Separación de Variables):
$$\int y^{-1/2} dy = \int -0.2 dt \implies 2\sqrt{y} = -0.2t + C$$
Aplicando $y(0)=4 \rightarrow 2\sqrt{4} = 4 = C$. Por lo tanto, la solución exacta es:
$$y(t) = \left( 2 - 0.1t \right)^2 \implies y(1.0) = (2 - 0.1)^2 = \mathbf{3.6100\text{ m}}$$

---

### Desarrollo Numérico Paso a Paso

#### 1. Aplicación del Método de Euler ($h=0.5$)
- **Paso 1 ($t_0 = 0, y_0 = 4$):**
  $$f(0, 4) = -0.2\sqrt{4} = -0.4$$
  $$y(0.5) = 4 + 0.5(-0.4) = \mathbf{3.8000\text{ m}}$$
- **Paso 2 ($t_1 = 0.5, y_1 = 3.8$):**
  $$f(0.5, 3.8) = -0.2\sqrt{3.8} = -0.38987$$
  $$y(1.0) = 3.8 + 0.5(-0.38987) = \mathbf{3.60506\text{ m}}$$
- *Error Absoluto de Euler:* $|3.6100 - 3.60506| = 0.00494$ m

#### 2. Aplicación del Método de Heun ($h=0.5$)
- **Paso 1 ($t_0 = 0, y_0 = 4$):**
  - Predicción: $u_1 = 4 + 0.5(-0.2\sqrt{4}) = 3.8$
  - Corrección: $y(0.5) = 4 + \frac{0.5}{2} \left[ -0.2\sqrt{4} + (-0.2\sqrt{3.8}) \right] = 4 + 0.25[-0.4 - 0.38987] = \mathbf{3.80253\text{ m}}$
- **Paso 2 ($t_1 = 0.5, y_1 = 3.80253$):**
  - Predicción: $u_2 = 3.80253 + 0.5(-0.2\sqrt{3.80253}) = 3.60503$
  - Corrección: $y(1.0) = 3.80253 + 0.25 \left[ -0.2\sqrt{3.80253} + (-0.2\sqrt{3.60503}) \right] = \mathbf{3.61003\text{ m}}$
- *Error Absoluto de Heun:* $|3.6100 - 3.61003| = 0.00003$ m

#### 3. Aplicación del Método RK4 ($h=0.5$)
- Realizando las evaluaciones ponderadas de $k_1, k_2, k_3, k_4$, se obtiene:
  - $y(0.5) = 3.80250\text{ m}$
  - $y(1.0) = \mathbf{3.61000\text{ m}}$
- *Error Absoluto de RK4:* $< 10^{-6}$ m (Prácticamente idéntico al valor real analítico).

---

### Análisis de Resultados del Problemario:
Como se observa en los cálculos, el método de **Euler** subestima levemente la curva debido a que mantiene una pendiente constante en pasos lineales planos. **Heun** corrige la trayectoria de forma notable usando dos pendientes extremas reduciendo el error al orden de diezmilésimas. Finalmente, **RK4** calza con exactitud milimétrica sobre la curva real, validando por qué es la herramienta estándar para simulaciones de EDOs complejas en la industria.

# Unidad 2: Solución de Ecuaciones No Lineales (Métodos de Intervalo e Interpolación)

## 2.1 Métodos de Intervalo (Métodos Cerrados)

### Concepto Fundamental
Los **métodos de intervalo** (o métodos cerrados) se basan en el aprovechamiento de la continuidad de una función dentro de un intervalo acotado $[a, b]$. Si una función continua $f(x)$ cambia de signo en los extremos del intervalo, es decir, si $f(a) \cdot f(b) < 0$, entonces se garantiza que existe al menos una raíz real dentro de ese intervalo.

### El Teorema del Valor Intermedio (Teorema de Bolzano)
Sea $f: [a, b] \to \mathbb{R}$ una función continua en el intervalo cerrado $[a, b]$. Si $f(a)$ y $f(b)$ tienen signos opuestos, entonces existe al menos un número $c \in (a, b)$ tal que:
$$f(c) = 0$$

### Características Principales
- **Convergencia Asegurada:** Al estar acotados dentro de un intervalo donde se conoce el cambio de signo, estos métodos siempre convergen a la raíz (siempre que la función sea continua).
- **Velocidad de Convergencia:** Suelen ser más lentos en comparación con los métodos abiertos (como Newton-Raphson), ya que no utilizan información sobre la pendiente o curvatura de la función, solo el signo.


## 2.2 Método de Bisección

### Fundamento Teórico
Es el método más simple y robusto de los métodos cerrados. Consiste en dividir repetidamente el intervalo $[a, b]$ a la mitad hasta que el tamaño del subintervalo sea menor que una tolerancia predefinida.

### Algoritmo Paso a Paso
1. **Definir el intervalo:** Elegir $a$ y $b$ tales que $f(a) \cdot f(b) < 0$.
2. **Calcular el punto medio ($x_r$):**
   $$x_r = \frac{a + b}{2}$$
3. **Evaluar el cambio de signo:**
   - Si $f(a) \cdot f(x_r) < 0$, la raíz está en el subintervalo izquierdo. Hacer $b = x_r$.
   - Si $f(a) \cdot f(x_r) > 0$, la raíz está en el subintervalo derecho. Hacer $a = x_r$.
   - Si $f(a) \cdot f(x_r) = 0$, $x_r$ es la raíz exacta. Terminar el algoritmo.
4. **Calcular el error estimado:** A partir de la segunda iteración, calcular el error absoluto aproximado o relativo:
   $$E_{abs} = |x_{r}^{nuevo} - x_{r}^{anterior}|$$
5. **Criterio de parada:** Si $E_{abs} < \text{Tolerancia}$ o se alcanza el número máximo de iteraciones, detenerse; de lo contrario, volver al paso 2.

### Estimación del Error Máximo
Una gran ventaja de la bisección es que se puede calcular de antemano el número exacto de iteraciones $n$ requeridas para asegurar un error máximo $\epsilon$:
$$n > \frac{\ln(b - a) - \ln(\epsilon)}{\ln(2)}$$


## 2.3 Método de Aproximaciones Sucesivas (Iteración de Punto Fijo)

### Fundamento Teórico
El método de aproximaciones sucesivas, comúnmente llamado **Iteración de Punto Fijo**, transforma una ecuación no lineal $f(x) = 0$ en una forma algebraicamente equivalente:
$$x = g(x)$$
Un valor $x^*$ tal que $x^* = g(x^*)$ se denomina **punto fijo** de la función $g$, y coincide exactamente con la raíz de $f(x)$.

### Condición de Convergencia (Teorema del Punto Fijo)
No cualquier despeje $g(x)$ garantiza la convergencia del método. Para que las iteraciones converjan hacia la raíz, la derivada de la función de despeje $g(x)$ debe cumplir con la siguiente condición en un entorno de la raíz:
$$|g'(x)| < 1$$
- Si $|g'(x)| < 1$, el método converge (puede ser de forma monótona oaxilante).
- Si $|g'(x)| > 1$, el método diverge de forma exponencial.

### Algoritmo
1. Despejar linealmente una $x$ para obtener $x = g(x)$.
2. Proponer un valor inicial $x_0$.
3. Calcular la siguiente aproximación mediante:
   $$x_{k+1} = g(x_k)$$
4. Evaluar el error $|x_{k+1} - x_k|$. Si es menor que la tolerancia, terminar. Si no, repetir el paso 3.


## 2.4 Métodos de Interpolación y Métodos Abiertos

En este apartado se agrupan los métodos que utilizan aproximaciones lineales locales para estimar la raíz, ya sea encerrándola (Regla Falsa) o de forma libre (Secante y Newton-Raphson).

### 1. Método de la Regla Falsa (Falsa Posición)
Aunque es un método cerrado, la Regla Falsa utiliza una **interpolación lineal** entre los puntos $(a, f(a))$ y $(b, f(b))$. En lugar de cortar el intervalo a la mitad exacta (como bisección), traza una línea recta (secante) entre los dos puntos extremos; la intersección de esta línea recta con el eje $x$ define la nueva aproximación $x_r$.

**Fórmula de interpolación:**
$$x_r = b - \frac{f(b)(b - a)}{f(b) - f(a)}$$

El criterio de actualización del intervalo $[a, b]$ es exactamente el mismo que el de bisección.

### 2. Método de la Secante
Es una variante abierta del método de la regla falsa. No requiere que los puntos iniciales encierren la raíz. En lugar de mantener acotada la raíz, utiliza los últimos dos puntos calculados ($x_{k-1}$ y $x_k$) para trazar una recta secante y encontrar el siguiente punto $x_{k+1}$.

**Fórmula iterativa:**
$$x_{k+1} = x_k - \frac{f(x_k)(x_k - x_{k-1})}{f(x_k) - f(x_{k-1})}$$

- **Ventaja:** No requiere evaluar la derivada de la función.
- **Desventaja:** Puede divergir si los puntos iniciales no están lo suficientemente cerca de la raíz o si la pendiente se vuelve horizontal.

### 3. Método de Newton-Raphson
Es el método abierto más utilizado debido a su alta velocidad de convergencia (convergencia cuadrática). Se basa en la aproximación lineal de la función en un punto dado mediante la **recta tangente** a la curva en ese punto (derivada de primer orden o Serie de Taylor truncada).

**Fórmula iterativa:**
$$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$

- **Requisito fundamental:** La función debe ser derivable y $f'(x_k) \neq 0$.


## 2.5 Aplicaciones de los Métodos Numéricos

Los métodos de búsqueda de raíces tienen infinitas aplicaciones en la ciencia y la ingeniería donde las ecuaciones gobernantes no se pueden resolver por métodos analíticos tradicionales (como factorización o fórmula general).

### Ejemplos Prácticos de Aplicación:
1. **Ingeniería Química (Ecuaciones de Estado):** Cálculo del volumen molar de un gas real utilizando la ecuación de Van der Waals o Redlich-Kwong, las cuales son cúbicas respecto al volumen:
   $$\left( P + \frac{a}{v^2} \right) (v - b) = RT$$
2. **Ingeniería Civil / Mecánica (Análisis de Deflexiones y Estructuras):** Determinación de los puntos críticos de flexión máxima en una viga con cargas distribuidas complejas, resolviendo $f(x) = \frac{dy}{dx} = 0$.
3. **Física (Mecánica de Fluidos y Aerodinámica):** Cálculo del factor de fricción de un fluido en una tubería rugosa utilizando la ecuación implícita de Colebrook-White:
   $$\frac{1}{\sqrt{f}} = -2.0 \log_{10} \left( \frac{\varepsilon/D}{3.7} + \frac{2.51}{Re \sqrt{f}} \right)$$
   Esta ecuación no se puede despejar para $f$, por lo que requiere obligatoriamente métodos iterativos como el de aproximaciones sucesivas o Newton-Raphson.


## Código contenido en:

https://github.com/neonhdz/M-todosNum-ricos/tree/main/Tema2/Code

## Problemario contenido en: 

https://github.com/neonhdz/M-todosNum-ricos/tree/main/Tema2/Problemario

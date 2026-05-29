# Unidad 3: Sistemas de Ecuaciones Lineales

Este documento contiene el apunte teórico-práctico completo para la unidad de solución de sistemas de ecuaciones lineales (SEL), detallando métodos directos e iterativos, criterios de convergencia y análisis de resultados orientados a la ingeniería.

## 3.1 Introducción a los Sistemas de Ecuaciones Lineales (SEL)

Un sistema de $n$ ecuaciones lineales con $n$ incógnitas se expresa de la forma:

$$
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
\vdots \\
a_{n1}x_1 + a_{n2}x_2 + \dots + a_{nn}x_n &= b_n
\end{aligned}
$$

En forma matricial, esto se reduce a:
$$A \mathbf{x} = \mathbf{b}$$

Donde:
- $A$ es la **matriz de coeficientes** de dimensión $n \times n$.
- $\mathbf{x}$ es el **vector de incógnitas** de dimensión $n \times 1$.
- $\mathbf{b}$ es el **vector de términos independientes** de dimensión $n \times 1$.

### Clasificación de los Métodos Numéricos
1. **Métodos Directos:** Calculan la solución exacta en un número finito de pasos algebraicos (ignorando el error de redondeo de la máquina). Son ideales para sistemas densos y de tamaño moderado. Ejemplos: Eliminación Gaussiana, Gauss-Jordan, Descomposición LU.
2. **Métodos Iterativos:** Parten de una aproximación inicial $\mathbf{x}^{(0)}$ y generan una sucesión de vectores $\mathbf{x}^{(k)}$ que converge a la solución exacta bajo ciertas condiciones. Son ideales para sistemas gigantescos o matrices dispersas (con muchos ceros). Ejemplos: Jacobi, Gauss-Seidel.


## 3.2 Método de Eliminación Gaussiana

### Fundamento Teórico
Consiste en aplicar operaciones elementales por renglón a la **matriz aumentada** $[A | \mathbf{b}]$ con el fin de transformarla en una **matriz triangular superior**. Una vez obtenida esta forma, los valores de las variables se calculan de manera sistemática mediante **sustitución hacia atrás**.

### Operaciones Elementales Permitidas:
1. Intercambiar dos renglones ($R_i \leftrightarrow R_j$).
2. Multiplicar un renglón por un escalar no nulo ($R_i \leftarrow c \cdot R_i$).
3. Sumar a un renglón el múltiplo de otro ($R_i \leftarrow R_i + c \cdot R_j$).

### Algoritmo General:
1. **Eliminación hacia adelante:** Para cada columna $j$ desde $1$ hasta $n-1$:
   - Seleccionar el pivote $a_{jj}$. Si es cero (o muy cercano), realizar pivoteo parcial (intercambio de renglones).
   - Para cada renglón $i$ desde $j+1$ hasta $n$, calcular el factor multiplicador:
     $$m_{ij} = \frac{a_{ij}}{a_{jj}}$$
   - Actualizar el renglón: $R_i \leftarrow R_i - m_{ij} R_j$.
2. **Sustitución hacia atrás:**
   $$x_n = \frac{b_n}{a_{nn}}$$
   $$x_i = \frac{b_i - \sum_{j=i+1}^{n} a_{ij}x_j}{a_{ii}} \quad \text{para } i = n-1, n-2, \dots, 1$$


## 3.3 Método de Gauss-Jordan

### Fundamento Teórico
Es una variación directa de la eliminación gaussiana. La diferencia radica en que cuando se elimina una incógnita, se elimina de **todos los demás renglones**, tanto de los que están abajo como de los que están arriba del pivote. Además, cada renglón se normaliza dividiéndolo entre su elemento pivote. 

El objetivo final es transformar la matriz de coeficientes $A$ directamente en una **matriz identidad** ($I$). Al finalizar el proceso, el vector de términos independientes $\mathbf{b}$ se habrá transformado automáticamente en el vector solución $\mathbf{x}$, eliminando la necesidad de realizar la sustitución hacia atrás.

$$[A | \mathbf{b}] \longrightarrow [I | \mathbf{x}]$$


## 3.4 Método Iterativo de Jacobi

### Fundamento Teórico
El método de Jacobi resuelve cada ecuación de manera explícita para una variable de la diagonal. Supongamos que tenemos los valores de la iteración $k$, representados por $\mathbf{x}^{(k)}$. Para calcular el valor de la siguiente iteración $\mathbf{x}^{(k+1)}$, se utiliza **únicamente la información de la iteración anterior**.

### Fórmula de Recurrencia:
Para cada componente $i = 1, 2, \dots, n$:
$$x_i^{(k+1)} = \frac{b_i - \sum_{j \neq i} a_{ij} x_j^{(k)}}{a_{ii}}$$

### Requisito Crítico: Criterio de la Diagonal Dominante
Los métodos iterativos no siempre convergen. Una condición suficiente (pero no estrictamente necesaria) para garantizar la convergencia es que la matriz de coeficientes sea **Estrictamente Dominante por Diagonal (EDD)**. Esto significa que en cada renglón, el valor absoluto del elemento en la diagonal debe ser mayor que la suma de los valores absolutos de los demás elementos del mismo renglón:
$$|a_{ii}| > \sum_{j \neq i} |a_{ij}| \quad \forall i=1,2,\dots,n$$


## 3.5 Método Iterativo de Gauss-Seidel

### Fundamento Teórico
Gauss-Seidel es una optimización directa del método de Jacobi. En lugar de esperar a que termine toda la iteración para actualizar los valores del vector $\mathbf{x}$, Gauss-Seidel **emplea inmediatamente los nuevos valores calculados en la iteración actual** tan pronto como están disponibles. 

Dado que las variables modificadas suelen estar más cerca de la solución real que sus versiones de la iteración anterior, este método acelera drásticamente la velocidad de convergencia (aproximadamente al doble de velocidad que Jacobi).

### Fórmula de Recurrencia:
$$x_i^{(k+1)} = \frac{b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)}}{a_{ii}}$$


## 3.6 Ejercicio Resuelto Integral (Análisis Comparativo)

Resolveremos el siguiente sistema empleando los 4 métodos:

$$
\begin{aligned}
4x_1 - x_2 + x_3 &= 7 \\
4x_1 - 8x_2 + x_3 &= -21 \\
-2x_1 + x_2 + 5x_3 &= 15
\end{aligned}
$$

### Solución Exacta (Obtenida por Gauss y Gauss-Jordan):
Tras aplicar el proceso algebraico matricial, se llega a los valores exactos:
$$\mathbf{x} = \begin{bmatrix} 2 \\ 4 \\ 3 \end{bmatrix}$$

### Comportamiento Iterativo (Jacobi vs. Gauss-Seidel):
Utilizando un vector inicial $\mathbf{x}^{(0)} = [0, 0, 0]^T$ y una tolerancia de $10^{-4}$:

- **Método de Jacobi:** Requiere **10 iteraciones** para estabilizarse dentro del margen de error debido a que calcula las variables de forma aislada.
- **Método de Gauss-Seidel:** Requiere únicamente **5 iteraciones** (la mitad del tiempo computacional) porque aprovecha la retroalimentación inmediata de los datos actualizados.

### Conclusión del Análisis de Resultados
1. **Garantía de Convergencia:** El sistema propuesto cumple con la condición EDD ($|4| > |-1|+|1|$; $|-8| > |4|+|1|$; $|5| > |-2|+|1|$), razón por la cual ambos métodos convergieron rápidamente.
2. **Elección del Método:** Para aplicaciones en ingeniería con sistemas masivos (ej. simulación por Elementos Finitos o Redes Eléctricas), **Gauss-Seidel** o variantes avanzadas (como SOR) son preferibles sobre Jacobi por su alta eficiencia en memoria y velocidad.

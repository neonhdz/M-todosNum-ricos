# Unidad 5: Interpolación Numérica

La interpolación es un método numérico utilizado para estimar valores desconocidos que se encuentran dentro del rango de un conjunto discreto de datos tabulados conocidos. A diferencia de los métodos de regresión (que buscan una curva de mejor ajuste general), la interpolación exige que la función matemática construida pase **exactamente** por todos los puntos de datos dados.

---

## 4.1 Interpolación Lineal

Es la forma más simple y rápida de interpolación. Consiste en unir dos puntos de datos consecutivos con una línea recta. Si tenemos dos puntos coordenados $(x_0, y_0)$ y $(x_1, y_1)$, el valor interpolado $y$ para un punto intermedio $x$ se calcula asumiendo que la pendiente entre los puntos es constante (relación de triángulos semejantes):

$$f_1(x) = y_0 + \frac{y_1 - y_0}{x_1 - x_0} (x - x_0)$$

- **Ventaja:** Cálculo inmediato y sencillo.
- **Desventaja:** Tiene un error de truncamiento alto si la verdadera función subyacente tiene mucha curvatura, ya que asume un comportamiento completamente recto entre los puntos.

### Ejercicio Práctico
**Problema:** De acuerdo con tablas termodinámicas, la densidad del agua a **20°C** es de **0.9982 g/cm³** y a **30°C** es de **0.9956 g/cm³**. Estimar la densidad del agua a **24°C** utilizando interpolación lineal.

**Desarrollo:**
- $(x_0, y_0) = (20, 0.9982)$
- $(x_1, y_1) = (30, 0.9956)$
- $x = 24$

Sustituyendo en la fórmula:
$$f_1(24) = 0.9982 + \frac{0.9956 - 0.9982}{30 - 20} (24 - 20)$$
$$f_1(24) = 0.9982 + \frac{-0.0026}{10} (4)$$
$$f_1(24) = 0.9982 - 0.00104 = \mathbf{0.99716 \text{ g/cm}^3}$$

---

## 4.2 Interpolación Cuadrática

Para reducir el error asociado a las líneas rectas de la interpolación lineal, la interpolación cuadrática utiliza un polinomio de segundo grado (una parábola) para conectar **tres** puntos de datos: $(x_0, y_0)$, $(x_1, y_1)$ y $(x_2, y_2)$. Esto le permite capturar la curvatura de los datos.

Empleando el formato de los polinomios de Newton mediante diferencias divididas, la ecuación se define como:

$$f_2(x) = b_0 + b_1(x - x_0) + b_2(x - x_0)(x - x_1)$$

Donde los coeficientes se calculan evaluando las pendientes:
- $b_0 = y_0$
- $b_1 = \frac{y_1 - y_0}{x_1 - x_0}$
- $b_2 = \frac{\frac{y_2 - y_1}{x_2 - x_1} - b_1}{x_2 - x_0}$

### Ejercicio Práctico
**Problema:** Ampliando el problema anterior, agregamos un tercer punto de datos de las tablas: a **40°C**, la densidad es **0.9922 g/cm³**. Estimar nuevamente la densidad a **24°C** utilizando un polinomio cuadrático.

**Desarrollo:**
- Puntos conocidos: $(20, 0.9982)$, $(30, 0.9956)$, $(40, 0.9922)$
- Cálculo de coeficientes:
  - $b_0 = 0.9982$
  - $b_1 = \frac{0.9956 - 0.9982}{30 - 20} = -0.00026$
  - $b_2 = \frac{\frac{0.9922 - 0.9956}{40 - 30} - (-0.00026)}{40 - 20} = \frac{-0.00034 - (-0.00026)}{20} = \frac{-0.00008}{20} = -0.000004$

Sustituyendo en el polinomio con $x = 24$:
$$f_2(24) = 0.9982 - 0.00026(24 - 20) - 0.000004(24 - 20)(24 - 30)$$
$$f_2(24) = 0.9982 - 0.00026(4) - 0.000004(4)(-6)$$
$$f_2(24) = 0.9982 - 0.00104 + 0.000096 = \mathbf{0.997256 \text{ g/cm}^3}$$

*(Nota: Al considerar la curvatura, la estimación mejoró y se ajusta más a los valores experimentales reales de las tablas).*

---

## 4.3 Interpolación Segmentada (Splines)

Cuando se cuenta con un gran número de puntos de datos (por ejemplo, 15 puntos), la teoría clásica dictaría usar un polinomio de grado 14 para interconectar todos los puntos a la vez. Sin embargo, los polinomios de grado alto son extremadamente inestables y provocan oscilaciones violentas entre los puntos, un error drástico conocido matemáticamente como el **Fenómeno de Runge**.

Para solucionar este problema se utiliza la **interpolación segmentada o por trazadores (*splines*)**. En lugar de usar una sola ecuación de grado alto para todos los datos, se aplican sub-polinomios de grado bajo vinculados de manera sucesiva entre cada par de puntos (segmento por segmento), aplicando restricciones para asegurar que las uniones sean estables y suaves.

### Clasificación de Splines
1. **Splines Lineales (Grado 1):** Es básicamente conectar los puntos con múltiples rectas. La función es continua en los nodos (puntos de unión), pero su primera derivada no lo es, lo que genera cambios abruptos ("picos") en las esquinas de los datos.
2. **Splines Cuadráticos (Grado 2):** Utilizan tramos de parábolas. Garantizan que tanto la función como su primera derivada (la pendiente) sean continuas en los nodos. Esto elimina los picos de las uniones y genera transiciones suaves.
3. **Splines Cúbicos (Grado 3):** Es el estándar de oro en ingeniería y diseño asistido por computadora (CAD, renderizado, manufactura CNC). Conecta pares de puntos con ecuaciones cúbicas asegurando que:
   - La curva pase por todos los puntos.
   - Las primeras derivadas coincidan en los nodos (pendientes iguales = no hay picos).
   - Las segundas derivadas coincidan en los nodos (curvaturas iguales = transiciones orgánicas).

Al aplicar splines cúbicos sobre $n$ puntos de datos, se genera un sistema de ecuaciones lineales simultáneas para encontrar los coeficientes de las $n-1$ ecuaciones cúbicas resultantes, entregando un perfil de interpolación excepcionalmente pulido y exacto.

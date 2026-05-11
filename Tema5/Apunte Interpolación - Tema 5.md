# Interpolación
La interpolación es, en esencia, "conectar los puntos". Es el arte matemático de estimar un valor desconocido que se encuentra dentro del intervalo de unos datos que ya conocemos.
## 1. Interpolación Lineal
La interpolación lineal es el método más simple para estimar valores intermedios entre dos puntos conocidos $(x_0,y_0)$ y $(x_0,y_0)$ trazando una línea recta, usado frecuentemente en tablas de datos o funciones con comportamiento lineal.
La forma más sencilla de interpolación consiste en unir dos puntos con una línea recta
### Fórmula
Si queremos encontrar el valor $y$ para un punto $x$ situado entre $(x_0, y_0)$ y $(x_1, y_1)$:

$$y = y_0 + \frac{y_1 - y_0}{x_1 - x_0}(x - x_0)$$

- ¿Cuándo usarla? Cuando los puntos están muy cerca o cuando sabes que la relación es bastante directa.

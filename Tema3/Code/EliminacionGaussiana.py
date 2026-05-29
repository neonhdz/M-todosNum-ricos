import numpy as np
import time

def eliminacion_gaussiana(A, b):
    """
    Resuelve el sistema lineal Ax = b mediante Eliminacion
    Gaussiana con Pivoteo Parcial.

    Parametros:
    -----------
    A : lista de listas (matriz cuadrada n x n)
        Coeficientes del sistema de ecuaciones.
        Ejemplo: [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]

    b : lista (vector de n elementos)
        Terminos independientes (lado derecho del sistema).
        Ejemplo: [8, -11, -3]

    Retorna:
    --------
    x : numpy array con la solucion [x1, x2, ..., xn]
        o None si el sistema es incompatible o indeterminado.

    Representacion en codigo:
    -------------------------
    - A y b se combinan en una sola estructura llamada
      "matriz aumentada" M de tamaño n x (n+1), donde
      las primeras n columnas son A y la ultima es b.

    - Todas las operaciones se hacen directamente sobre M
      usando indexacion de numpy: M[fila], M[fila][col].

    - Los multiplicadores m_ij se calculan como el cociente
      entre el elemento a eliminar y el pivote actual.
    """

    M = np.array(
        [[float(A[i][j]) for j in range(n)] + [float(b[i])]
         for i in range(n)]
    )

    print("\n" + "=" * 60)
    print(" ELIMINACION GAUSSIANA CON PIVOTEO PARCIAL")
    print("=" * 60)

    print("\n [INICIO] Matriz aumentada [A|b]:")
    imprimir_matriz(M, n)

    for col in range(n):

        max_fila = col

        for fila in range(col + 1, n):
            if abs(M[fila][col]) > abs(M[max_fila][col]):
                max_fila = fila

        if max_fila != col:
            M[[col, max_fila]] = M[[max_fila, col]]

            print(f"\n [PIVOTEO] Intercambiamos F{col+1} con F{max_fila+1}")
            imprimir_matriz(M, n)

        if abs(M[col][col]) < 1e-12:

            for fila in range(col, n):
                if abs(M[fila][n]) > 1e-12:

                    tiempo_fin = time.perf_counter()

                    print("\n [RESULTADO] SISTEMA INCOMPATIBLE")
                    print(f" Fila {fila+1}: 0 = {M[fila][n]:.6f} -> Contradiccion")

                    print(f"\n [TIMER] Ejecucion detenida en: "
                          f"{(tiempo_fin - tiempo_inicio)*1000:.6f} ms")

                    return None

            tiempo_fin = time.perf_counter()

            print("\n [RESULTADO] SISTEMA INDETERMINADO (infinitas soluciones)")

            print(f"\n [TIMER] Ejecucion detenida en: "
                  f"{(tiempo_fin - tiempo_inicio)*1000:.6f} ms")

            return None

        print(f"\n [ITERACION {col+1}] Pivote = {M[col][col]:.6f}"
              f" (fila {col+1}, columna {col+1})")

        tiempo_iter_inicio = time.perf_counter()

        for fila in range(col + 1, n):

            if abs(M[fila][col]) > 1e-12:

                m = M[fila][col] / M[col][col]  # multiplicador

                M[fila] = M[fila] - m * M[col]  # operacion de fila

                print(f" m{fila+1}{col+1} = {m:.6f} -> "
                      f"F{fila+1} = F{fila+1} - ({m:.6f}) x F{col+1}")

        tiempo_iter_fin = time.perf_counter()

        tiempo_iter_ms = (tiempo_iter_fin - tiempo_iter_inicio) * 1000

        print(f"\n Matriz tras eliminar columna {col+1}:")
        imprimir_matriz(M, n)

        print(f" [TIMER ITERACION {col+1}] {tiempo_iter_ms:.6f} ms")

    print("\n" + "-" * 60)
    print(" ETAPA 2: SUSTITUCION HACIA ATRAS")
    print("-" * 60)

    tiempo_sust_inicio = time.perf_counter()

    x = np.zeros(n)  # Vector solucion inicializado en ceros

    for i in range(n - 1, -1, -1):

        # Suma de contribuciones de variables ya conocidas
        suma = sum(M[i][j] * x[j] for j in range(i + 1, n))

        # Despejamos x[i]
        x[i] = (M[i][n] - suma) / M[i][i]

        print(f" x{i+1} = ({M[i][n]:.6f} - {suma:.6f}) "
              f"/ {M[i][i]:.6f} = {x[i]:.6f}")

    tiempo_sust_fin = time.perf_counter()

    tiempo_sust_ms = (tiempo_sust_fin - tiempo_sust_inicio) * 1000
    tiempo_total_ms = (tiempo_sust_fin - tiempo_inicio) * 1000

    # Resumen de tiempos
    print("\n" + "=" * 60)
    print(" RESUMEN DE TIEMPOS")
    print("=" * 60)

    print(f" Eliminacion hacia adelante: incluida en iteraciones")
    print(f" Sustitucion hacia atras: {tiempo_sust_ms:.6f} ms")
    print(f" TIEMPO TOTAL DE EJECUCION: {tiempo_total_ms:.6f} ms")

    print("=" * 60)

    return x


# ══════════════════════════════════════════════════════════
# FUNCION AUXILIAR: imprimir_matriz
# ══════════════════════════════════════════════════════════

def imprimir_matriz(M, n):
    """
    Imprime la matriz aumentada M de forma legible.

    Las primeras n columnas son los coeficientes (A) y
    la columna n es el termino independiente (b),
    separados visualmente con el simbolo |.
    """

    for fila in M:
        coefs = " ".join(f"{v:9.4f}" for v in fila[:n])
        ind = f"{fila[n]:9.4f}"

        print(f" [ {coefs} | {ind} ]")


# ══════════════════════════════════════════════════════════
# FUNCION AUXILIAR: verificar_solucion
# ══════════════════════════════════════════════════════════

def verificar_solucion(A, b, x):
    """
    Verifica la solucion sustituyendo x en Ax = b y calcula
    el porcentaje de error relativo para cada ecuacion.

    Porcentaje de error relativo:
    ------------------------------
    Mide que tan lejos esta el valor calculado del valor
    esperado, expresado como porcentaje:

    % error = | (valor_real - valor_calculado) / valor_real | * 100

    Donde:
    valor_real = b[i] (termino independiente original)
    valor_calculado = A[i] . x (producto punto de la fila con la solucion)

    Un % error cercano a 0.000000% indica que la solucion
    es numericamente exacta dentro de la precision de flotante.

    Representacion en codigo:
    -------------------------
    - Calculamos Ax[i] con sum() como producto punto.
    - El error absoluto es abs(b[i] - Ax[i]).
    - El error relativo evita dividir por cero usando
      max(abs(b[i]), 1e-12).
    - Multiplicamos por 100 para expresarlo en porcentaje.
    """

    print("\n" + "=" * 60)
    print(" VERIFICACION Y PORCENTAJE DE ERROR")
    print("=" * 60)

    print(f" {'Ecuacion':<12} {'Calculado':>12} {'Esperado':>12}"
          f" {'Error abs':>12} {'% Error':>12} Estado")

    print(" " + "-" * 68)

    todos_ok = True
    errores = []

    for i in range(len(b)):

        # Producto punto: A[i] · x = suma de a_ij * x_j
        calculado = sum(A[i][j] * x[j] for j in range(len(x)))

        # Error absoluto: diferencia entre esperado y calculado
        error_abs = abs(b[i] - calculado)

        # Error relativo porcentual
        # Usamos max(abs(b[i]), 1e-12) para evitar division por cero
        # cuando el termino independiente es exactamente 0
        error_pct = (error_abs / max(abs(b[i]), 1e-12)) * 100

        errores.append(error_pct)

        ok = "OK" if error_abs < 1e-8 else "ERROR"

        if ok == "ERROR":
            todos_ok = False

        print(f" Ec. {i+1:<8} {calculado:>12.6f} {b[i]:>12.6f}"
              f" {error_abs:>12.2e} {error_pct:>11.6f}% [{ok}]")

    # Error maximo y promedio entre todas las ecuaciones
    print(" " + "-" * 68)

    print(f" Error maximo: {max(errores):.6e}%")
    print(f" Error promedio: {sum(errores)/len(errores):.6e}%")

    if todos_ok:
        print("\n Solucion verificada correctamente.")
        print(" El % de error cercano a 0 confirma precision numerica.")

    print("=" * 60)


# ══════════════════════════════════════════════════════════
# INTERFAZ INTERACTIVA
# ══════════════════════════════════════════════════════════

def ingresar_sistema():
    """
    Permite ingresar un sistema personalizado desde consola.
    """

    print("\n" + "=" * 60)
    print(" INGRESA TU PROPIO SISTEMA")
    print("=" * 60)

    while True:
        try:
            n = int(input("\n Cuantas ecuaciones tiene tu sistema? (ej: 2, 3, 4): "))

            if n < 2:
                print(" Minimo 2 ecuaciones.")
                continue

            break

        except ValueError:
            print(" Ingresa un numero entero valido.")

    variables = ['x', 'y', 'z', 'w'] if n <= 4 else [f"x{i+1}" for i in range(n)]

    print(f"\n Ingresa los coeficientes separados por espacios.")
    print(f" Ejemplo: para 2x + y - z = 8 escribe: 2 1 -1\n")

    A = []

    for i in range(n):

        while True:
            try:
                entrada = input(f" Ecuacion {i+1} - coeficientes [{', '.join(variables)}]: ")

                coefs = list(map(float, entrada.strip().split()))

                if len(coefs) != n:
                    print(f" Necesitas exactamente {n} coeficientes.")
                    continue

                A.append(coefs)

                break

            except ValueError:
                print(" Solo numeros separados por espacios.")

    print(f"\n Ahora los terminos independientes (lado derecho del =).\n")

    while True:
        try:
            entrada = input(f" Terminos independientes [{n} valores]: ")

            b = list(map(float, entrada.strip().split()))

            if len(b) != n:
                print(f" Necesitas exactamente {n} valores.")
                continue

            break

        except ValueError:
            print(" Solo numeros separados por espacios.")

    print("\n Sistema ingresado:")

    for i in range(n):

        terminos = " + ".join(
            f"({int(A[i][j]) if float(A[i][j]).is_integer() else A[i][j]}){variables[j]}"
            for j in range(n)
        )

        bi = int(b[i]) if float(b[i]).is_integer() else b[i]

        print(f" {terminos} = {bi}")

    return A, b, variables


def menu_principal():
    """
    Menu principal interactivo con ejemplos predefinidos
    y opcion para ingresar sistemas personalizados.
    """

    print("\n" + "=" * 60)
    print(" ELIMINACION GAUSSIANA — MENU PRINCIPAL")
    print("=" * 60)

    while True:

        print("\n Que quieres hacer?")
        print(" [1] Ejemplo 1 — Sistema 3x3 (solucion unica)")
        print(" [2] Ejemplo 2 — Sistema 2x2 (incompatible)")
        print(" [3] Ejemplo 3 — Sistema 2x2 (indeterminado)")
        print(" [4] Ingresar mi propio sistema")
        print(" [0] Salir")

        opcion = input("\n Opcion: ").strip()

        if opcion == "1":

            A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
            b = [8, -11, -3]

            sol = eliminacion_gaussiana(A, b)

            if sol is not None:

                print("\n [SOLUCION]")

                for var, val in zip(['x', 'y', 'z'], sol):
                    print(f" {var} = {val:.6f}")

                verificar_solucion(A, b, sol)

        elif opcion == "2":

            A = [[1, 1], [2, 2]]
            b = [2, 5]

            sol = eliminacion_gaussiana(A, b)

            if sol is None:
                print("\n El sistema no tiene solucion.")

        elif opcion == "3":

            A = [[1, 1], [2, 2]]
            b = [4, 8]

            sol = eliminacion_gaussiana(A, b)

            if sol is None:
                print("\n El sistema tiene infinitas soluciones.")

        elif opcion == "4":

            A, b, variables = ingresar_sistema()

            sol = eliminacion_gaussiana(A, b)

            if sol is not None:

                print("\n [SOLUCION]")

                for var, val in zip(variables, sol):
                    print(f" {var} = {val:.6f}")

                verificar_solucion(A, b, sol)

        elif opcion == "0":

            print("\n Hasta luego!\n")
            break

        else:
            print(" Opcion no valida, intenta de nuevo.")

        input("\n Presiona Enter para continuar...")


if __name__ == "__main__":
    menu_principal()

import tkinter as tk
import time
from tkinter import messagebox

def gauss_jordan(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):

        # Hacer el pivote 1
        pivote = matriz[i][i]

        if pivote == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero")
            return None

        for j in range(columnas):
            matriz[i][j] /= pivote

        # Hacer ceros en la columna del pivote
        for k in range(filas):
            if k != i:
                factor = matriz[k][i]

                for j in range(columnas):
                    matriz[k][j] -= factor * matriz[i][j]

    return matriz

def resolver():
    try:
        matriz = []

        for i in range(n):
            fila = []

            for j in range(n + 1):
                valor = entradas[i][j].get()

                if valor == "":
                    valor = 0

                fila.append(float(valor))

            matriz.append(fila)

        # ⏱️ iniciar timer
        inicio = time.perf_counter()

        resultado = gauss_jordan(matriz)

        # ⏱️ terminar timer
        fin = time.perf_counter()

        tiempo = fin - inicio

        if resultado is None:
            return

        salida = ""

        for i in range(n):
            salida += f"x{i+1} = {resultado[i][-1]:.3f}\n"

        salida += f"\nTiempo de ejecución: {tiempo:.7f} segundos"

        resultado_label.config(text=salida)

    except ValueError:
        messagebox.showerror("Error", "Ingresa solo valores numéricos")

def crear_matriz():
    global entradas, n

    try:
        n = int(tamano_entry.get())

        if n <= 0:
            raise ValueError

        for widget in matriz_frame.winfo_children():
            widget.destroy()

        entradas = []

        for i in range(n):
            fila = []

            for j in range(n + 1):
                e = tk.Entry(matriz_frame, width=5)
                e.grid(row=i, column=j, padx=3, pady=3)

                fila.append(e)

            entradas.append(fila)

    except ValueError:
        messagebox.showerror("Error", "Ingresa un tamaño válido")

# Ventana principal
ventana = tk.Tk()

ventana.title("Método de Gauss-Jordan")
ventana.geometry("350x350")

# Tamaño de la matriz
tk.Label(ventana, text="Tamaño del sistema (n):").pack()

tamano_entry = tk.Entry(ventana)
tamano_entry.pack()

tk.Button(ventana, text="Crear matriz",
          command=crear_matriz).pack(pady=5)

# Frame para la matriz
matriz_frame = tk.Frame(ventana)
matriz_frame.pack()

# Botón resolver
tk.Button(ventana, text="Resolver", command=resolver).pack(pady=10)

# Resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
resultado_label.pack()

ventana.mainloop()

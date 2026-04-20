import tkinter as tk
from tkinter import messagebox
import math

def calcular_integral():
    """Obtiene los valores de la interfaz, realiza el cálculo y muestra el resultado."""
    try:
        # Obtener los valores de los campos de texto
        funcion_str = entrada_f.get()
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        n = int(entrada_n.get())

        if n <= 0:
            raise ValueError("El número de intervalos 'n' debe ser un entero positivo.")

        # Definir el entorno seguro para evaluar la función ingresada por el usuario
        entorno_matematico = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "exp": math.exp, "log": math.log, "sqrt": math.sqrt,
            "pi": math.pi, "e": math.e
        }

        # Función lambda para evaluar el string de forma dinámica
        def f(x):
            entorno_matematico["x"] = x
            # Se restringen los builtins por seguridad
            return eval(funcion_str, {"__builtins__": None}, entorno_matematico)

        # --- Lógica de la Regla del Trapecio ---
        h = (b - a) / n
        suma = f(a) + f(b)
        
        for i in range(1, n):
            x_i = a + i * h
            suma += 2 * f(x_i)
            
        resultado = (h / 2) * suma
        # --------------------------------------

        # Mostrar el resultado en la etiqueta
        etiqueta_resultado.config(text=f"Resultado: {resultado:.6f}")

    except Exception as e:
        # En caso de error (letras en vez de números, sintaxis de función mal, etc.)
        messagebox.showerror("Error en los datos", f"Por favor revisa tus entradas.\nDetalle: {e}")

# --- Configuración de la ventana de Tkinter ---
ventana = tk.Tk()
ventana.title("Regla del Trapecio")
ventana.geometry("350x250")
ventana.resizable(False, False)
ventana.config(padx=20, pady=20)

# Etiquetas y campos de entrada
tk.Label(ventana, text="Función f(x):").grid(row=0, column=0, sticky="e", pady=5)
entrada_f = tk.Entry(ventana, width=20)
entrada_f.grid(row=0, column=1, pady=5)
entrada_f.insert(0, "x**2") # Valor por defecto

tk.Label(ventana, text="Límite inferior (a):").grid(row=1, column=0, sticky="e", pady=5)
entrada_a = tk.Entry(ventana, width=20)
entrada_a.grid(row=1, column=1, pady=5)
entrada_a.insert(0, "0")

tk.Label(ventana, text="Límite superior (b):").grid(row=2, column=0, sticky="e", pady=5)
entrada_b = tk.Entry(ventana, width=20)
entrada_b.grid(row=2, column=1, pady=5)
entrada_b.insert(0, "1")

tk.Label(ventana, text="Intervalos (n):").grid(row=3, column=0, sticky="e", pady=5)
entrada_n = tk.Entry(ventana, width=20)
entrada_n.grid(row=3, column=1, pady=5)
entrada_n.insert(0, "100")

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular Integral", command=calcular_integral, bg="#4CAF50", fg="white")
boton_calcular.grid(row=4, column=0, columnspan=2, pady=15)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ---", font=("Arial", 12, "bold"))
etiqueta_resultado.grid(row=5, column=0, columnspan=2)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

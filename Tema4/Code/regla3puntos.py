import tkinter as tk
from tkinter import messagebox
import math

def derivacion_3_puntos():
    """Obtiene los valores, aplica la fórmula de 3 puntos seleccionada y muestra el resultado."""
    try:
        # Obtener valores de la interfaz
        funcion_str = entrada_f.get()
        x0 = float(entrada_x0.get())
        h = float(entrada_h.get())

        if h == 0:
            raise ValueError("El tamaño de paso 'h' no puede ser cero.")

        # Entorno matemático seguro
        entorno_matematico = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "exp": math.exp, "log": math.log, "sqrt": math.sqrt,
            "pi": math.pi, "e": math.e
        }

        # Función lambda dinámica
        def f(x):
            entorno_matematico["x"] = x
            return eval(funcion_str, {"__builtins__": None}, entorno_matematico)

        # Elegir el método según la selección
        metodo = opcion_metodo.get()
        
        # Fórmulas de diferenciación numérica de 3 puntos para la primera derivada
        if metodo == "adelante":
            resultado = (-3 * f(x0) + 4 * f(x0 + h) - f(x0 + 2 * h)) / (2 * h)
        elif metodo == "atras":
            resultado = (3 * f(x0) - 4 * f(x0 - h) + f(x0 - 2 * h)) / (2 * h)
        elif metodo == "centrada":
            resultado = (f(x0 + h) - f(x0 - h)) / (2 * h)
        else:
            raise ValueError("Selecciona una fórmula de diferenciación.")

        # Mostrar resultado
        etiqueta_resultado.config(text=f"f'({x0}) ≈ {resultado:.10f}", fg="#D84315")

    except Exception as e:
        messagebox.showerror("Error en los datos", f"Verifica tus entradas.\nDetalle: {e}")

# --- Configuración de la Interfaz (Tkinter) ---
ventana = tk.Tk()
ventana.title("Derivación: Regla de 3 Puntos")
ventana.geometry("380x350")
ventana.resizable(False, False)
ventana.config(padx=20, pady=20)

# Variables de control
opcion_metodo = tk.StringVar(value="centrada") # Centrada por defecto por ser más exacta

# Campos de entrada
tk.Label(ventana, text="Función f(x):").grid(row=0, column=0, sticky="e", pady=5)
entrada_f = tk.Entry(ventana, width=22)
entrada_f.grid(row=0, column=1, pady=5)
entrada_f.insert(0, "exp(x)") # Derivada de e^x es e^x, ideal para probar

tk.Label(ventana, text="Punto a evaluar (x0):").grid(row=1, column=0, sticky="e", pady=5)
entrada_x0 = tk.Entry(ventana, width=22)
entrada_x0.grid(row=1, column=1, pady=5)
entrada_x0.insert(0, "1.0")

tk.Label(ventana, text="Tamaño del paso (h):").grid(row=2, column=0, sticky="e", pady=5)
entrada_h = tk.Entry(ventana, width=22)
entrada_h.grid(row=2, column=1, pady=5)
entrada_h.insert(0, "0.01") # Un h pequeño suele dar mejores aproximaciones

# Selección de la fórmula
marco_metodo = tk.LabelFrame(ventana, text="Tipo de Fórmula (3 puntos)")
marco_metodo.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

tk.Radiobutton(marco_metodo, text="Hacia Adelante", variable=opcion_metodo, value="adelante").pack(anchor="w", padx=10)
tk.Radiobutton(marco_metodo, text="Hacia Atrás", variable=opcion_metodo, value="atras").pack(anchor="w", padx=10)
tk.Radiobutton(marco_metodo, text="Centrada", variable=opcion_metodo, value="centrada").pack(anchor="w", padx=10)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular Derivada", command=derivacion_3_puntos, bg="#FF9800", fg="white", font=("Arial", 10, "bold"))
boton_calcular.grid(row=4, column=0, columnspan=2, pady=15)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="f'(x0) ≈ ---", font=("Arial", 12, "bold"))
etiqueta_resultado.grid(row=5, column=0, columnspan=2)

# Iniciar aplicación
ventana.mainloop()

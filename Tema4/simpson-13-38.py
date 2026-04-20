import tkinter as tk
from tkinter import messagebox
import math

def simpson_1_3(f, a, b, n):
    """Lógica para la regla de Simpson 1/3 compuesta."""
    if n % 2 != 0:
        raise ValueError("Para Simpson 1/3, el número de intervalos 'n' debe ser PAR.")
    
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x_i = a + i * h
        # Si el índice es par, multiplicamos por 2; si es impar, por 4
        if i % 2 == 0:
            suma += 2 * f(x_i)
        else:
            suma += 4 * f(x_i)
            
    return (h / 3) * suma

def simpson_3_8(f, a, b, n):
    """Lógica para la regla de Simpson 3/8 compuesta."""
    if n % 3 != 0:
        raise ValueError("Para Simpson 3/8, el número de intervalos 'n' debe ser MÚLTIPLO DE 3.")
    
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x_i = a + i * h
        # Si el índice es múltiplo de 3, multiplicamos por 2; si no, por 3
        if i % 3 == 0:
            suma += 2 * f(x_i)
        else:
            suma += 3 * f(x_i)
            
    return (3 * h / 8) * suma

def calcular_integral():
    """Obtiene los valores, decide qué método usar y muestra el resultado."""
    try:
        # Obtener valores
        funcion_str = entrada_f.get()
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        n = int(entrada_n.get())

        if n <= 0:
            raise ValueError("El número de intervalos 'n' debe ser un entero positivo.")

        # Entorno seguro para la función
        entorno_matematico = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "exp": math.exp, "log": math.log, "sqrt": math.sqrt,
            "pi": math.pi, "e": math.e
        }

        def f(x):
            entorno_matematico["x"] = x
            return eval(funcion_str, {"__builtins__": None}, entorno_matematico)

        # Elegir método según el Radiobutton seleccionado
        metodo = opcion_metodo.get()
        
        if metodo == "1/3":
            resultado = simpson_1_3(f, a, b, n)
        elif metodo == "3/8":
            resultado = simpson_3_8(f, a, b, n)
        else:
            raise ValueError("Selecciona un método de integración.")

        # Mostrar resultado
        etiqueta_resultado.config(text=f"Resultado: {resultado:.6f}", fg="blue")

    except Exception as e:
        messagebox.showerror("Error", f"Verifica tus datos.\nDetalle: {e}")

# --- Interfaz Gráfica (Tkinter) ---
ventana = tk.Tk()
ventana.title("Integración por Simpson")
ventana.geometry("380x320")
ventana.resizable(False, False)
ventana.config(padx=20, pady=20)

# Variables de control
opcion_metodo = tk.StringVar(value="1/3") # Valor por defecto

# Campos de entrada
tk.Label(ventana, text="Función f(x):").grid(row=0, column=0, sticky="e", pady=5)
entrada_f = tk.Entry(ventana, width=22)
entrada_f.grid(row=0, column=1, pady=5)
entrada_f.insert(0, "sin(x)")

tk.Label(ventana, text="Límite inferior (a):").grid(row=1, column=0, sticky="e", pady=5)
entrada_a = tk.Entry(ventana, width=22)
entrada_a.grid(row=1, column=1, pady=5)
entrada_a.insert(0, "0")

tk.Label(ventana, text="Límite superior (b):").grid(row=2, column=0, sticky="e", pady=5)
entrada_b = tk.Entry(ventana, width=22)
entrada_b.grid(row=2, column=1, pady=5)
entrada_b.insert(0, "pi")

tk.Label(ventana, text="Intervalos (n):").grid(row=3, column=0, sticky="e", pady=5)
entrada_n = tk.Entry(ventana, width=22)
entrada_n.grid(row=3, column=1, pady=5)
entrada_n.insert(0, "6") # 6 es par y múltiplo de 3, funciona para ambos métodos

# Selección de método
marco_metodo = tk.LabelFrame(ventana, text="Método de Simpson")
marco_metodo.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

tk.Radiobutton(marco_metodo, text="Simpson 1/3 (n par)", variable=opcion_metodo, value="1/3").pack(side="left", padx=10, pady=5)
tk.Radiobutton(marco_metodo, text="Simpson 3/8 (n mult. de 3)", variable=opcion_metodo, value="3/8").pack(side="right", padx=10, pady=5)

# Botón calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_integral, bg="#2196F3", fg="white", width=15)
boton_calcular.grid(row=5, column=0, columnspan=2, pady=10)

# Etiqueta de resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ---", font=("Arial", 12, "bold"))
etiqueta_resultado.grid(row=6, column=0, columnspan=2)

ventana.mainloop()

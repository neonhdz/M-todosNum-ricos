import tkinter as tk
from tkinter import messagebox

def calcular_interpolacion():
    try:
        modo = var_modo.get()
        x_objetivo = float(entry_x_obj.get())

        # MODO 1: LINEAL o MODO 2: CUADRÁTICA
        if modo in [1, 2]:
            x0 = float(entry_x0.get())
            y0 = float(entry_y0.get())
            x1 = float(entry_x1.get())
            y1 = float(entry_y1.get())
            
            if x0 == x1:
                messagebox.showerror("Error", "Los valores de x0 y x1 no pueden ser iguales.")
                return

            if modo == 1:
                # Interpolación Lineal
                resultado = y0 + ((y1 - y0) / (x1 - x0)) * (x_objetivo - x0)
                lbl_resultado.config(text=f"Resultado f({x_objetivo}) = {resultado:.4f}")
                
            elif modo == 2:
                # Interpolación Cuadrática
                x2 = float(entry_x2.get())
                y2 = float(entry_y2.get())
                
                if x0 == x2 or x1 == x2:
                    messagebox.showerror("Error", "Los valores de X no pueden repetirse.")
                    return
                
                term1 = y0 * ((x_objetivo - x1) * (x_objetivo - x2)) / ((x0 - x1) * (x0 - x2))
                term2 = y1 * ((x_objetivo - x0) * (x_objetivo - x2)) / ((x1 - x0) * (x1 - x2))
                term3 = y2 * ((x_objetivo - x0) * (x_objetivo - x1)) / ((x2 - x0) * (x2 - x1))
                
                resultado = term1 + term2 + term3
                lbl_resultado.config(text=f"Resultado f({x_objetivo}) = {resultado:.4f}")

        # MODO 3: SEGMENTADA (A trozos)
        elif modo == 3:
            # Obtener y convertir las listas de valores
            str_xs = entry_xs.get().split(',')
            str_ys = entry_ys.get().split(',')
            
            xs = [float(x.strip()) for x in str_xs]
            ys = [float(y.strip()) for y in str_ys]
            
            if len(xs) != len(ys):
                messagebox.showerror("Error", "Debe haber la misma cantidad de valores X e Y.")
                return
            if len(xs) < 2:
                messagebox.showerror("Error", "Se necesitan al menos 2 puntos para interpolar.")
                return
                
            # Ordenar los puntos de menor a mayor respecto a X
            puntos = sorted(zip(xs, ys))
            xs = [p[0] for p in puntos]
            ys = [p[1] for p in puntos]
            
            # Encontrar el segmento correspondiente
            indice = 0
            if x_objetivo <= xs[0]:
                indice = 0 # Extrapolación hacia atrás
            elif x_objetivo >= xs[-1]:
                indice = len(xs) - 2 # Extrapolación hacia adelante
            else:
                for i in range(len(xs) - 1):
                    if xs[i] <= x_objetivo <= xs[i+1]:
                        indice = i
                        break
                        
            # Aplicar interpolación lineal en ese segmento específico
            x0, y0 = xs[indice], ys[indice]
            x1, y1 = xs[indice+1], ys[indice+1]
            
            if x0 == x1:
                messagebox.showerror("Error", "Hay valores de X duplicados en tus datos.")
                return
                
            resultado = y0 + ((y1 - y0) / (x1 - x0)) * (x_objetivo - x0)
            lbl_resultado.config(text=f"Resultado f({x_objetivo}) = {resultado:.4f}")

    except ValueError:
        messagebox.showerror("Error de entrada", "Asegúrate de ingresar solo números (usa puntos para decimales).")

def cambiar_modo():
    modo = var_modo.get()
    if modo == 1:
        frame_segmentada.pack_forget()
        frame_datos.pack(pady=10)
        frame_punto2.grid_remove()
    elif modo == 2:
        frame_segmentada.pack_forget()
        frame_datos.pack(pady=10)
        frame_punto2.grid()
    elif modo == 3:
        frame_datos.pack_forget()
        frame_segmentada.pack(pady=10)

# --- CONFIGURACIÓN DE LA VENTANA ---
root = tk.Tk()
root.title("Calculadora de Interpolación Múltiple")
root.geometry("400x500")
root.resizable(False, False)

var_modo = tk.IntVar(value=1)

tk.Label(root, text="Selecciona el tipo de interpolación:", font=("Arial", 12, "bold")).pack(pady=10)

# Radiobuttons para los 3 modos
frame_radios = tk.Frame(root)
frame_radios.pack()
tk.Radiobutton(frame_radios, text="Lineal", variable=var_modo, value=1, command=cambiar_modo).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(frame_radios, text="Cuadrática", variable=var_modo, value=2, command=cambiar_modo).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(frame_radios, text="Segmentada", variable=var_modo, value=3, command=cambiar_modo).pack(side=tk.LEFT, padx=5)

# --- FRAME PARA DATOS LINEAL/CUADRÁTICA ---
frame_datos = tk.Frame(root)
tk.Label(frame_datos, text="Punto 0 (x0, y0):").grid(row=0, column=0, sticky="e", pady=5)
entry_x0 = tk.Entry(frame_datos, width=10)
entry_x0.grid(row=0, column=1, padx=5)
entry_y0 = tk.Entry(frame_datos, width=10)
entry_y0.grid(row=0, column=2, padx=5)

tk.Label(frame_datos, text="Punto 1 (x1, y1):").grid(row=1, column=0, sticky="e", pady=5)
entry_x1 = tk.Entry(frame_datos, width=10)
entry_x1.grid(row=1, column=1, padx=5)
entry_y1 = tk.Entry(frame_datos, width=10)
entry_y1.grid(row=1, column=2, padx=5)

frame_punto2 = tk.Frame(frame_datos)
tk.Label(frame_punto2, text="Punto 2 (x2, y2):").grid(row=0, column=0, sticky="e", pady=5)
entry_x2 = tk.Entry(frame_punto2, width=10)
entry_x2.grid(row=0, column=1, padx=5)
entry_y2 = tk.Entry(frame_punto2, width=10)
entry_y2.grid(row=0, column=2, padx=5)
frame_punto2.grid(row=2, column=0, columnspan=3)

frame_datos.pack(pady=10)
frame_punto2.grid_remove() # Oculto al inicio

# --- FRAME PARA DATOS SEGMENTADA ---
frame_segmentada = tk.Frame(root)
tk.Label(frame_segmentada, text="Valores de X separados por coma:\n(Ej: 1, 4, 7, 10)").pack()
entry_xs = tk.Entry(frame_segmentada, width=40)
entry_xs.pack(pady=5)

tk.Label(frame_segmentada, text="Valores de Y separados por coma:\n(Ej: 3, 24, 67, 80)").pack()
entry_ys = tk.Entry(frame_segmentada, width=40)
entry_ys.pack(pady=5)

# Oculto al inicio
frame_segmentada.pack_forget()

# --- VALOR A ESTIMAR ---
frame_objetivo = tk.Frame(root)
frame_objetivo.pack(pady=10)
tk.Label(frame_objetivo, text="Valor de X a estimar:", font=("Arial", 10, "bold")).pack()
entry_x_obj = tk.Entry(frame_objetivo, width=15)
entry_x_obj.pack(pady=5)

tk.Button(root, text="Calcular", command=calcular_interpolacion, bg="#4CAF50", fg="white", font=("Arial", 11, "bold")).pack(pady=15)

lbl_resultado = tk.Label(root, text="Resultado f(x) = ---", font=("Arial", 14, "bold"), fg="#333333")
lbl_resultado.pack(pady=5)

# Iniciar por defecto en modo Lineal
cambiar_modo()

root.mainloop()

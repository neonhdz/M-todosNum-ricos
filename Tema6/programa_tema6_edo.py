import tkinter as tk
from tkinter import ttk, messagebox
import math

class SimuladorEDOApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Ecuaciones Diferenciales Ordinarias (EDO) - Tema 6")
        self.root.geometry("1180x720")
        self.root.minsize(1050, 650)
        
        # Estilos visuales refinados
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), background="#27ae60", foreground="white")
        style.map("TButton", background=[("active", "#2ecc71")])
        style.configure("Header.TLabel", font=("Segoe UI", 13, "bold"), foreground="#2c3e50")
        
        self.create_layout()
        
    def create_layout(self):
        # Panel Izquierdo de Entradas y Configuración
        left_frame = ttk.Frame(self.root, padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # Selección de la Ecuación Diferencial f(t, y)
        ode_frame = ttk.LabelFrame(left_frame, text=" Configuración del PVI [dy/dt = f(t,y)] ", padding=10)
        ode_frame.pack(fill=tk.X, pady=(0,10))
        
        ttk.Label(ode_frame, text="Expresión f(t,y):").pack(anchor=tk.W)
        self.ode_var = tk.StringVar(value="-0.2 * sqrt(y)")
        
        # Desplegable con ejemplos preestablecidos comunes
        self.ode_presets = ttk.Combobox(ode_frame, values=[
            "-0.2 * sqrt(y)      (Vaciado de Tanque)",
            "y - t**2 + 1        (Modelo No Lineal)",
            "-2 * t * y          (Campana Gaussiana)",
            "0.5 * y             (Crecimiento Exponencial)"
        ], width=32)
        self.ode_presets.pack(fill=tk.X, pady=(2,5))
        self.ode_presets.current(0)
        self.ode_presets.bind("<<ComboboxSelected>>", self.on_preset_changed)
        
        ttk.Label(ode_frame, text="Escribir/Editar fórmula manualmente:").pack(anchor=tk.W, pady=(5,0))
        self.ode_entry = ttk.Entry(ode_frame, textvariable=self.ode_var, font=("Consolas", 10))
        self.ode_entry.pack(fill=tk.X, pady=2)
        
        # Parámetros del Método Numérico
        param_frame = ttk.LabelFrame(left_frame, text=" Condiciones Iniciales y Parámetros ", padding=10)
        param_frame.pack(fill=tk.X, pady=5)
        
        # t0
        ttk.Label(param_frame, text="Tiempo inicial (t0):").grid(row=0, column=0, sticky=tk.W, pady=3)
        self.t0_entry = ttk.Entry(param_frame, width=10, justify=tk.CENTER)
        self.t0_entry.insert(0, "0.0")
        self.t0_entry.grid(row=0, column=1, padx=5, pady=3)
        
        # y0
        ttk.Label(param_frame, text="Valor inicial (y0):").grid(row=1, column=0, sticky=tk.W, pady=3)
        self.y0_entry = ttk.Entry(param_frame, width=10, justify=tk.CENTER)
        self.y0_entry.insert(0, "4.0")
        self.y0_entry.grid(row=1, column=1, padx=5, pady=3)
        
        # h (Paso)
        ttk.Label(param_frame, text="Tamaño de paso (h):").grid(row=2, column=0, sticky=tk.W, pady=3)
        self.h_entry = ttk.Entry(param_frame, width=10, justify=tk.CENTER)
        self.h_entry.insert(0, "0.1")
        self.h_entry.grid(row=2, column=1, padx=5, pady=3)
        
        # t_end
        ttk.Label(param_frame, text="Tiempo final (t_final):").grid(row=3, column=0, sticky=tk.W, pady=3)
        self.tend_entry = ttk.Entry(param_frame, width=10, justify=tk.CENTER)
        self.tend_entry.insert(0, "2.0")
        self.tend_entry.grid(row=3, column=1, padx=5, pady=3)
        
        # Selección de algoritmo
        ttk.Label(left_frame, text="Algoritmo de Integración Numérica:", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W, pady=(10,2))
        self.method_var = tk.StringVar(value="Runge-Kutta 4to Orden (RK4)")
        self.method_combo = ttk.Combobox(left_frame, textvariable=self.method_var, state="readonly", width=30)
        self.method_combo['values'] = ("Euler Estándar", "Euler Mejorado (Heun)", "Runge-Kutta 4to Orden (RK4)")
        self.method_combo.pack(fill=tk.X, pady=(0,15))
        
        # Botón Calcular
        self.btn_solve = ttk.Button(left_frame, text="SIMULAR MODELO (EDO)", command=self.solve_ode)
        self.btn_solve.pack(fill=tk.X, pady=5)
        
        # Panel Derecho de Resultados Visuales e Impresión
        right_frame = ttk.Frame(self.root, padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Título superior derecho
        ttk.Label(right_frame, text="Monitoreo Analítico e Historial de Pasos", style="Header.TLabel").pack(anchor=tk.W, pady=(0,5))
        
        # Cuaderno de pestañas (Tabs) para separar Tabla de Gráfico
        self.notebook = ttk.Notebook(right_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab 1: Tabla de Datos
        self.tab_table = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_table, text=" Tabla de Datos ")
        
        self.txt_output = tk.Text(self.tab_table, font=("Consolas", 10), wrap=tk.NONE, bg="#fafafa", fg="#2c3e50")
        sb_y = ttk.Scrollbar(self.tab_table, orient=tk.VERTICAL, command=self.txt_output.yview)
        sb_x = ttk.Scrollbar(self.tab_table, orient=tk.HORIZONTAL, command=self.txt_output.xview)
        self.txt_output.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)
        
        self.txt_output.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        sb_y.pack(side=tk.RIGHT, fill=tk.Y, before=self.txt_output)
        sb_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Tab 2: Gráfico Integrado (Canvas)
        self.tab_graph = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_graph, text=" Curva de Solución Aproximada ")
        
        self.canvas = tk.Canvas(self.tab_graph, bg="white", highlightthickness=1, highlightbackground="#ccc")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.canvas.bind("<Configure>", lambda e: self.redraw_graph_if_data())
        
        self.history_points = [] # Guarda pares (t, y) para graficar

    def on_preset_changed(self, event):
        selection = self.ode_presets.get()
        if "Vaciado" in selection:
            self.ode_var.set("-0.2 * sqrt(y)")
            self.t0_entry.delete(0, tk.END); self.t0_entry.insert(0, "0.0")
            self.y0_entry.delete(0, tk.END); self.y0_entry.insert(0, "4.0")
            self.tend_entry.delete(0, tk.END); self.tend_entry.insert(0, "2.0")
        elif "Modelo No Lineal" in selection:
            self.ode_var.set("y - t**2 + 1")
            self.t0_entry.delete(0, tk.END); self.t0_entry.insert(0, "0.0")
            self.y0_entry.delete(0, tk.END); self.y0_entry.insert(0, "0.5")
            self.tend_entry.delete(0, tk.END); self.tend_entry.insert(0, "2.0")
        elif "Campana" in selection:
            self.ode_var.set("-2 * t * y")
            self.t0_entry.delete(0, tk.END); self.t0_entry.insert(0, "0.0")
            self.y0_entry.delete(0, tk.END); self.y0_entry.insert(0, "1.0")
            self.tend_entry.delete(0, tk.END); self.tend_entry.insert(0, "2.5")
        elif "Crecimiento" in selection:
            self.ode_var.set("0.5 * y")
            self.t0_entry.delete(0, tk.END); self.t0_entry.insert(0, "0.0")
            self.y0_entry.delete(0, tk.END); self.y0_entry.insert(0, "10.0")
            self.tend_entry.delete(0, tk.END); self.tend_entry.insert(0, "5.0")

    def eval_f(self, t, y):
        # Evaluación matemática segura mapeando funciones estándar
        expr = self.ode_var.get()
        allowed_words = {
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'exp': math.exp, 'log': math.log, 'sqrt': math.sqrt,
            'pi': math.pi, 'e': math.e, 't': t, 'y': y
        }
        try:
            return eval(expr, {"__builtins__": None}, allowed_words)
        except Exception as err:
            raise ValueError(f"Fórmula inválida o indeterminación matemática en la evaluación: {err}")

    def solve_ode(self):
        self.txt_output.delete("1.0", tk.END)
        self.history_points = []
        
        try:
            t = float(self.t0_entry.get())
            y = float(self.y0_entry.get())
            h = float(self.h_entry.get())
            t_final = float(self.tend_entry.get())
        except ValueError:
            messagebox.showerror("Error de entrada", "Asegúrese de rellenar los parámetros con valores numéricos flotantes válidos.")
            return
            
        if h <= 0:
            messagebox.showerror("Error numérico", "El tamaño de paso h debe ser mayor a cero.")
            return
        if t_final < t:
            messagebox.showerror("Error numérico", "El tiempo final t_final debe ser mayor o igual al tiempo inicial t0.")
            return

        method = self.method_var.get()
        
        self.txt_output.insert(tk.END, f"=== REPORTE NUMÉRICO: INTEGRACIÓN DE EDO ===\n")
        self.txt_output.insert(tk.END, f"Método aplicado: {method}\n")
        self.txt_output.insert(tk.END, f"Ecuación dy/dt = {self.ode_var.get()}\n")
        self.txt_output.insert(tk.END, f"Parámetros: h = {h}, Rango = [{t}, {t_final}]\n")
        self.txt_output.insert(tk.END, "-" * 55 + "\n")
        self.txt_output.insert(tk.END, f"{'Paso (i)':<12}{'Tiempo (t)':<18}{'Solución Aprox. (y)':<20}\n")
        self.txt_output.insert(tk.END, "-" * 55 + "\n")
        
        step_count = 0
        self.history_points.append((t, y))
        self.txt_output.insert(tk.END, f"{step_count:<12}{t:<18.4f}{y:<20.6f}\n")
        
        # Lazo iterativo principal de integración numérica
        # Agregamos un epsilon pequeño para mitigar imprecisiones de coma flotante en el límite
        while t + 1e-9 < t_final:
            try:
                if method == "Euler Estándar":
                    slope = self.eval_f(t, y)
                    y_next = y + h * slope
                    t_next = t + h
                    
                elif method == "Euler Mejorado (Heun)":
                    slope_start = self.eval_f(t, y)
                    y_predictor = y + h * slope_start
                    t_next = t + h
                    slope_end = self.eval_f(t_next, y_predictor)
                    y_next = y + (h / 2.0) * (slope_start + slope_end)
                    
                elif method == "Runge-Kutta 4to Orden (RK4)":
                    k1 = self.eval_f(t, y)
                    k2 = self.eval_f(t + h/2.0, y + (h/2.0)*k1)
                    k3 = self.eval_f(t + h/2.0, y + (h/2.0)*k2)
                    k4 = self.eval_f(t + h, y + h*k3)
                    y_next = y + (h / 6.0) * (k1 + 2.0*k2 + 2.0*k3 + k4)
                    t_next = t + h
                
                # Actualizar variables de estado
                t = t_next
                y = y_next
                step_count += 1
                
                self.history_points.append((t, y))
                self.txt_output.insert(tk.END, f"{step_count:<12}{t:<18.4f}{y:<20.6f}\n")
                
            except ValueError as err_msg:
                messagebox.showerror("Falla de convergencia", str(err_msg))
                return
            except OverflowError:
                messagebox.showerror("Desbordamiento", "La solución ha divergido al infinito (Overflow). Intente reduciendo el paso h o modificando la EDO.")
                return

        # Dibujar gráfico de inmediato en el Canvas integrado
        self.draw_graph()
        self.notebook.select(0) # Regresa a la vista de tabla para revisar los datos

    def redraw_graph_if_data(self):
        if self.history_points:
            self.draw_graph()

    def draw_graph(self):
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        
        if w < 50 or h < 50 or not self.history_points:
            return
            
        margin = 45
        plot_w = w - 2 * margin
        plot_h = h - 2 * margin
        
        # Encontrar extremos para el escalado automático en el Canvas
        ts = [p[0] for p in self.history_points]
        ys = [p[1] for p in self.history_points]
        
        min_t, max_t = min(ts), max(ts)
        min_y, max_y = min(ys), max(ys)
        
        # Prevenir divisiones entre cero si los rangos son planos
        range_t = (max_t - min_t) if max_t != min_t else 1.0
        range_y = (max_y - min_y) if max_y != min_y else 1.0
        
        # Función auxiliar de transformación de coordenadas a pixeles del Canvas
        def to_pixels(t_val, y_val):
            x_pix = margin + ((t_val - min_t) / range_t) * plot_w
            # En graficación computacional el eje Y va hacia abajo, invertimos la proyección:
            y_pix = h - margin - ((y_val - min_y) / range_y) * plot_w if range_y == 0 else h - margin - ((y_val - min_y) / range_y) * plot_h
            return x_pix, y_pix
            
        # Dibujar Cuadrícula de Fondo y Ejes principales
        self.canvas.create_rectangle(margin, margin, w - margin, h - margin, outline="#bdc3c7", fill="#fbfbfb")
        
        # Líneas de ejes cartesianos de referencia (Etiquetas base)
        self.canvas.create_text(margin, h - margin + 15, text=f"{min_t:.2f}", font=("Segoe UI", 9))
        self.canvas.create_text(w - margin, h - margin + 15, text=f"{max_t:.2f}", font=("Segoe UI", 9))
        self.canvas.create_text(margin - 22, h - margin, text=f"{min_y:.2f}", font=("Segoe UI", 9))
        self.canvas.create_text(margin - 22, margin, text=f"{max_y:.2f}", font=("Segoe UI", 9))
        
        # Títulos de Ejes
        self.canvas.create_text(w/2, h - margin + 25, text="Variable Independiente (t)", font=("Segoe UI", 10, "bold"), fill="#34495e")
        self.canvas.create_text(18, h/2, text="Solución (y)", font=("Segoe UI", 10, "bold"), fill="#34495e", angle=90)
        
        # Mapear e interconectar los puntos calculados
        pixel_points = [to_pixels(pt[0], pt[1]) for pt in self.history_points]
        
        # Dibujar líneas de tendencia de la curva aproximada
        for i in range(len(pixel_points) - 1):
            x1, y1 = pixel_points[i]
            x2, y2 = pixel_points[i+1]
            self.canvas.create_line(x1, y1, x2, y2, fill="#27ae60", width=3, smooth=True)
            
        # Dibujar nodos puntuales sobre la curva
        for x_p, y_p in pixel_points:
            self.canvas.create_oval(x_p - 3, y_p - 3, x_p + 3, y_p + 3, fill="#e74c3c", outline="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorEDOApp(root)
    root.mainloop()

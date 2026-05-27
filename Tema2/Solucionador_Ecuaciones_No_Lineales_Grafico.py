import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
import math

class MetodosNumericosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Software de Métodos Numéricos - Solución de Ecuaciones")
        self.root.geometry("1100x650")
        self.root.minsize(950, 550)
        
        # Configurar tema visual estilizado
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), background="#2c3e50", foreground="white")
        style.map("TButton", background=[("active", "#34495e")])
        style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"), foreground="#2c3e50")
        
        # Símbolo matemático de Sympy para parsing
        self.x_sym = sp.symbols('x')
        
        self.create_widgets()
        
    def create_widgets(self):
        # Contenedor Principal Izquierdo: Controles
        control_frame = ttk.LabelFrame(self.root, text=" Configuración del Problema ", padding=15)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=15, pady=15)
        
        # Selector de Método
        ttk.Label(control_frame, text="Seleccione el Método:").pack(anchor=tk.W, pady=(0,2))
        self.method_var = tk.StringVar()
        self.method_combo = ttk.Combobox(control_frame, textvariable=self.method_var, state="readonly", width=25)
        self.method_combo['values'] = ("Bisección", "Regla Falsa", "Newton-Raphson", "Secante")
        self.method_combo.current(0)
        self.method_combo.pack(anchor=tk.W, pady=(0,15))
        self.method_combo.bind("<<ComboboxSelected>>", self.on_method_change)
        
        # Entrada de la Función
        ttk.Label(control_frame, text="Función f(x) (Sintaxis Python, ej: x**3 - 2*x - 5):").pack(anchor=tk.W, pady=(0,2))
        self.func_entry = ttk.Entry(control_frame, width=28, font=("Consolas", 11))
        self.func_entry.insert(0, "x**3 - 2*x - 5")
        self.func_entry.pack(anchor=tk.W, pady=(0,15))
        
        # Parámetros numéricos dinámicos
        self.param_frame = ttk.Frame(control_frame)
        self.param_frame.pack(anchor=tk.W, fill=tk.X, pady=(0,15))
        
        self.lbl_p1 = ttk.Label(self.param_frame, text="Límite inferior (a):")
        self.lbl_p1.grid(row=0, column=0, sticky=tk.W, pady=2)
        self.p1_entry = ttk.Entry(self.param_frame, width=12)
        self.p1_entry.insert(0, "2.0")
        self.p1_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
        
        self.lbl_p2 = ttk.Label(self.param_frame, text="Límite superior (b):")
        self.lbl_p2.grid(row=1, column=0, sticky=tk.W, pady=2)
        self.p2_entry = ttk.Entry(self.param_frame, width=12)
        self.p2_entry.insert(0, "3.0")
        self.p2_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Tolerancia y Máximo de Iteraciones
        ttk.Label(control_frame, text="Tolerancia (Error Máximo):").pack(anchor=tk.W, pady=(0,2))
        self.tol_entry = ttk.Entry(control_frame, width=28)
        self.tol_entry.insert(0, "0.0001")
        self.tol_entry.pack(anchor=tk.W, pady=(0,15))
        
        ttk.Label(control_frame, text="Máximo de Iteraciones:").pack(anchor=tk.W, pady=(0,2))
        self.iter_entry = ttk.Entry(control_frame, width=28)
        self.iter_entry.insert(0, "50")
        self.iter_entry.pack(anchor=tk.W, pady=(0,20))
        
        # Botón Calcular
        self.btn_calc = ttk.Button(control_frame, text="CALCULAR RAÍZ", command=self.execute_method)
        self.btn_calc.pack(fill=tk.X, pady=5)
        
        # Contenedor Derecho: Resultados y Tabla
        result_frame = ttk.Frame(self.root, padding=15)
        result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        ttk.Label(result_frame, text="Resultados e Historial de Iteraciones", style="Header.TLabel").pack(anchor=tk.W, pady=(0,10))
        
        # Tabla de Iteraciones
        table_frame = ttk.Frame(result_frame)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(table_frame, columns=("iter", "p1", "p2", "xr", "fxr", "error"), show="headings")
        self.tree.heading("iter", text="Iteración")
        self.tree.heading("p1", text="Parámetro 1")
        self.tree.heading("p2", text="Parámetro 2")
        self.tree.heading("xr", text="Raíz aprox (Xr)")
        self.tree.heading("fxr", text="f(Xr)")
        self.tree.heading("error", text="Error Abs.")
        
        self.tree.column("iter", width=70, anchor=tk.CENTER)
        self.tree.column("p1", width=120, anchor=tk.CENTER)
        self.tree.column("p2", width=120, anchor=tk.CENTER)
        self.tree.column("xr", width=140, anchor=tk.CENTER)
        self.tree.column("fxr", width=140, anchor=tk.CENTER)
        self.tree.column("error", width=140, anchor=tk.CENTER)
        
        sb_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        sb_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        sb_y.grid(row=0, column=1, sticky="ns")
        sb_x.grid(row=1, column=0, sticky="ew")
        
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Cuadro de Resumen Final
        self.summary_lbl = ttk.Label(result_frame, text="Resumen de ejecución: Esperando cálculo...", font=("Segoe UI", 11, "italic"), foreground="#555")
        self.summary_lbl.pack(anchor=tk.W, pady=(15, 0))

    def on_method_change(self, event=None):
        method = self.method_var.get()
        # Modificar etiquetas dinámicamente según las necesidades del método seleccionado
        if method in ("Bisección", "Regla Falsa"):
            self.lbl_p1.config(text="Límite inferior (a):")
            self.lbl_p2.config(text="Límite superior (b):")
            self.p2_entry.config(state="normal")
        elif method == "Newton-Raphson":
            self.lbl_p1.config(text="Valor Inicial (x0):")
            self.lbl_p2.config(text="[No requerido]:")
            self.p2_entry.delete(0, tk.END)
            self.p2_entry.config(state="disabled")
        elif method == "Secante":
            self.lbl_p1.config(text="Aproximación x0:")
            self.lbl_p2.config(text="Aproximación x1:")
            self.p2_entry.config(state="normal")

    def parse_function(self, func_str):
        try:
            expr = sp.sympify(func_str)
            f = lambda val: float(expr.evalf(subs={self.x_sym: val}))
            return expr, f
        except Exception as e:
            raise ValueError(f"Error en la sintaxis de la función matemática: {e}")

    def execute_method(self):
        # Limpiar tabla previa
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        method = self.method_var.get()
        func_str = self.func_entry.get().strip()
        
        try:
            expr, f = self.parse_function(func_str)
            tol = float(self.tol_entry.get())
            max_iter = int(self.iter_entry.get())
            p1 = float(self.p1_entry.get())
            p2 = float(self.p2_entry.get()) if method != "Newton-Raphson" else 0.0
        except ValueError as err:
            messagebox.showerror("Error de Entrada", str(err))
            return
        except Exception as e:
            messagebox.showerror("Error", f"Verifique sus datos numéricos de entrada: {e}")
            return

        # Cambiar encabezados de columnas de la tabla de acuerdo al método
        if method in ("Bisección", "Regla Falsa"):
            self.tree.heading("p1", text="a")
            self.tree.heading("p2", text="b")
        elif method == "Newton-Raphson":
            self.tree.heading("p1", text="x_k")
            self.tree.heading("p2", text="-")
        elif method == "Secante":
            self.tree.heading("p1", text="x_{k-1}")
            self.tree.heading("p2", text="x_k")

        # Ejecución del algoritmo correspondiente
        try:
            if method == "Bisección":
                self.run_biseccion(f, p1, p2, tol, max_iter)
            elif method == "Regla Falsa":
                self.run_regla_falsa(f, p1, p2, tol, max_iter)
            elif method == "Newton-Raphson":
                self.run_newton(expr, f, p1, tol, max_iter)
            elif method == "Secante":
                self.run_secante(f, p1, p2, tol, max_iter)
        except Exception as e:
            messagebox.showerror("Error de Ejecución", f"Ocurrió un error inesperado durante las iteraciones: {e}")

    def run_biseccion(self, f, a, b, tol, max_iter):
        if f(a) * f(b) >= 0:
            messagebox.showerror("Error de Teorema", "f(a) y f(b) deben tener signos opuestos en Bisección.")
            return
            
        xr_old = 0.0
        for i in range(1, max_iter + 1):
            xr = (a + b) / 2.0
            fxr = f(xr)
            error = abs(xr - xr_old) if i > 1 else "-"
            
            # Insertar a la tabla
            err_str = f"{error:.6f}" if isinstance(error, float) else str(error)
            self.tree.insert("", tk.END, values=(i, f"{a:.6f}", f"{b:.6f}", f"{xr:.6f}", f"{fxr:.6f}", err_str))
            
            if error != "-" and error < tol:
                self.summary_lbl.config(text=f"Convergencia lograda en la iteración {i}. Raíz aprox = {xr:.6f} con error = {error:.6f}", foreground="green")
                return
                
            if f(a) * fxr < 0:
                b = xr
            else:
                a = xr
            xr_old = xr
            
        self.summary_lbl.config(text=f"Se alcanzó el límite de iteraciones sin lograr la tolerancia esperada. Raíz aprox = {xr:.6f}", foreground="orange")

    def run_regla_falsa(self, f, a, b, tol, max_iter):
        if f(a) * f(b) >= 0:
            messagebox.showerror("Error de Teorema", "f(a) y f(b) deben tener signos opuestos en Regla Falsa.")
            return
            
        xr_old = 0.0
        for i in range(1, max_iter + 1):
            fa, fb = f(a), f(b)
            if (fb - fa) == 0:
                messagebox.showerror("División por Cero", "División por cero detectada en el método de Regla Falsa.")
                return
            xr = b - (fb * (b - a)) / (fb - fa)
            fxr = f(xr)
            error = abs(xr - xr_old) if i > 1 else "-"
            
            err_str = f"{error:.6f}" if isinstance(error, float) else str(error)
            self.tree.insert("", tk.END, values=(i, f"{a:.6f}", f"{b:.6f}", f"{xr:.6f}", f"{fxr:.6f}", err_str))
            
            if error != "-" and error < tol:
                self.summary_lbl.config(text=f"Convergencia lograda en la iteración {i}. Raíz aprox = {xr:.6f} con error = {error:.6f}", foreground="green")
                return
                
            if f(a) * fxr < 0:
                b = xr
            else:
                a = xr
            xr_old = xr
            
        self.summary_lbl.config(text=f"Se alcanzó el límite de iteraciones. Raíz aprox = {xr:.6f}", foreground="orange")

    def run_newton(self, expr, f, x0, tol, max_iter):
        # Derivar de forma analítica usando sympy
        dexpr = sp.diff(expr, self.x_sym)
        df = lambda val: float(dexpr.evalf(subs={self.x_sym: val}))
        
        xk = x0
        for i in range(1, max_iter + 1):
            fxk = f(xk)
            dfxk = df(xk)
            
            if dfxk == 0:
                messagebox.showerror("División por Cero", f"La derivada se hizo cero en x = {xk}. Newton-Raphson falló.")
                return
                
            xk_next = xk - (fxk / dfxk)
            error = abs(xk_next - xk)
            
            self.tree.insert("", tk.END, values=(i, f"{xk:.6f}", "-", f"{xk_next:.6f}", f"{fxk:.6f}", f"{error:.6f}"))
            
            if error < tol:
                self.summary_lbl.config(text=f"Convergencia lograda en la iteración {i}. Raíz aprox = {xk_next:.6f} con error = {error:.6f}", foreground="green")
                return
                
            xk = xk_next
            
        self.summary_lbl.config(text=f"Se alcanzó el límite de iteraciones. Raíz aprox = {xk:.6f}", foreground="orange")

    def run_secante(self, f, x0, x1, tol, max_iter):
        for i in range(1, max_iter + 1):
            fx0, fx1 = f(x0), f(x1)
            if (fx1 - fx0) == 0:
                messagebox.showerror("División por Cero", "División por cero detectada en el método de la Secante.")
                return
                
            x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
            error = abs(x2 - x1)
            
            self.tree.insert("", tk.END, values=(i, f"{x0:.6f}", f"{x1:.6f}", f"{x2:.6f}", f"{f(x2):.6f}", f"{error:.6f}"))
            
            if error < tol:
                self.summary_lbl.config(text=f"Convergencia lograda en la iteración {i}. Raíz aprox = {x2:.6f} con error = {error:.6f}", foreground="green")
                return
                
            x0 = x1
            x1 = x2
            
        self.summary_lbl.config(text=f"Se alcanzó el límite de iteraciones. Raíz aprox = {x2:.6f}", foreground="orange")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetodosNumericosApp(root)
    root.mainloop()

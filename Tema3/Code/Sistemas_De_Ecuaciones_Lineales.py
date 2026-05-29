import tkinter as tk
from tkinter import ttk, messagebox

class SistemaEcuacionesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solucionador de Sistemas de Ecuaciones Lineales - Tema 3")
        self.root.geometry("1150x700")
        self.root.minsize(1000, 600)
        
        # Configuración de estilos visuales profesionales
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), background="#2980b9", foreground="white")
        style.map("TButton", background=[("active", "#3498db")])
        style.configure("Header.TLabel", font=("Segoe UI", 13, "bold"), foreground="#2c3e50")
        
        self.matrix_size = 3
        self.entry_A = []
        self.entry_b = []
        
        self.create_layout()
        self.build_matrix_grid()
        
    def create_layout(self):
        # Contenedor Izquierdo: Configuración y Entradas
        left_frame = ttk.Frame(self.root, padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # Selección de Tamaño de Matriz
        size_frame = ttk.Frame(left_frame)
        size_frame.pack(anchor=tk.W, pady=(0,10))
        ttk.Label(size_frame, text="Dimensión del Sistema (n x n): ", font=("Segoe UI", 10, "bold")).pack(side=tk.LEFT)
        self.size_var = tk.IntVar(value=3)
        self.size_combo = ttk.Combobox(size_frame, textvariable=self.size_var, values=[2, 3, 4, 5], width=5, state="readonly")
        self.size_combo.pack(side=tk.LEFT, padx=5)
        self.size_combo.bind("<<ComboboxSelected>>", self.on_size_changed)
        
        # Selección del Método
        ttk.Label(left_frame, text="Método de Solución:", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W, pady=(5,2))
        self.method_var = tk.StringVar(value="Gauss-Seidel")
        self.method_combo = ttk.Combobox(left_frame, textvariable=self.method_var, width=25, state="readonly")
        self.method_combo['values'] = ("Eliminación Gaussiana", "Gauss-Jordan", "Jacobi", "Gauss-Seidel")
        self.method_combo.pack(anchor=tk.W, pady=(0,15))
        self.method_combo.bind("<<ComboboxSelected>>", self.toggle_iterative_fields)
        
        # Contenedor Dinámico para la Matriz Aumentada
        self.matrix_label_frame = ttk.LabelFrame(left_frame, text=" Matriz de Coeficientes [A] y Vector [b] ", padding=10)
        self.matrix_label_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Parámetros para Métodos Iterativos (Jacobi / Gauss-Seidel)
        self.iter_frame = ttk.LabelFrame(left_frame, text=" Parámetros Iterativos ", padding=10)
        self.iter_frame.pack(fill=tk.X, pady=(10,15))
        
        ttk.Label(self.iter_frame, text="Tolerancia:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.tol_entry = ttk.Entry(self.iter_frame, width=10)
        self.tol_entry.insert(0, "0.0001")
        self.tol_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(self.iter_frame, text="Max Iteraciones:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.max_iter_entry = ttk.Entry(self.iter_frame, width=10)
        self.max_iter_entry.insert(0, "50")
        self.max_iter_entry.grid(row=1, column=1, padx=5, pady=2)
        
        # Botón Calcular
        self.btn_solve = ttk.Button(left_frame, text="RESOLVER SISTEMA", command=self.solve_system)
        self.btn_solve.pack(fill=tk.X, pady=5)
        
        # Contenedor Derecho: Resultados
        right_frame = ttk.Frame(self.root, padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        ttk.Label(right_frame, text="Consola de Resultados e Historial", style="Header.TLabel").pack(anchor=tk.W, pady=(0,5))
        
        # Caja de Texto para logs de resultados
        self.txt_output = tk.Text(right_frame, font=("Consolas", 10), wrap=tk.NONE, bg="#fcfcfc", fg="#2c3e50")
        sb_y = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.txt_output.yview)
        sb_x = ttk.Scrollbar(right_frame, orient=tk.HORIZONTAL, command=self.txt_output.xview)
        self.txt_output.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)
        
        # Ubicar elementos de salida
        self.txt_output.pack(fill=tk.BOTH, expand=True)
        sb_y.pack(side=tk.RIGHT, fill=tk.Y, before=self.txt_output)
        sb_x.pack(side=tk.BOTTOM, fill=tk.X)

    def on_size_changed(self, event):
        self.matrix_size = self.size_var.get()
        self.build_matrix_grid()
        
    def toggle_iterative_fields(self, event=None):
        method = self.method_var.get()
        if method in ("Jacobi", "Gauss-Seidel"):
            self.tol_entry.config(state="normal")
            self.max_iter_entry.config(state="normal")
        else:
            self.tol_entry.config(state="disabled")
            self.max_iter_entry.config(state="disabled")

    def build_matrix_grid(self):
        # Destruir elementos previos en la cuadrícula
        for widget in self.matrix_label_frame.winfo_children():
            widget.destroy()
            
        self.entry_A = []
        self.entry_b = []
        
        # Crear encabezados explicativos
        for j in range(self.matrix_size):
            ttk.Label(self.matrix_label_frame, text=f"x{j+1}", font=("Segoe UI", 9, "bold")).grid(row=0, column=j, padx=5, pady=2)
        ttk.Label(self.matrix_label_frame, text=" | ", font=("Segoe UI", 10, "bold")).grid(row=0, column=self.matrix_size, padx=2)
        ttk.Label(self.matrix_label_frame, text="b", font=("Segoe UI", 9, "bold")).grid(row=0, column=self.matrix_size+1, padx=5, pady=2)
        
        # Valores de ejemplo predeterminados (Sistema dominante de 3x3 del ejercicio base)
        default_A = [
            [4.0, -1.0, 1.0],
            [4.0, -8.0, 1.0],
            [-2.0, 1.0, 5.0]
        ]
        default_b = [7.0, -21.0, 15.0]
        
        # Construcción de la malla de cajas de texto
        for i in range(self.matrix_size):
            row_entries = []
            for j in range(self.matrix_size):
                ent = ttk.Entry(self.matrix_label_frame, width=7, font=("Consolas", 10), justify=tk.CENTER)
                ent.grid(row=i+1, column=j, padx=3, pady=3)
                # Rellenar con valores default si corresponde al tamaño 3
                if self.matrix_size == 3:
                    ent.insert(0, str(default_A[i][j]))
                else:
                    ent.insert(0, "0.0" if i!=j else "4.0")
                row_entries.append(ent)
            self.entry_A.append(row_entries)
            
            # Línea divisoria visual para la matriz aumentada
            ttk.Label(self.matrix_label_frame, text="|").grid(row=i+1, column=self.matrix_size, padx=2)
            
            # Entrada del vector de términos independientes b
            ent_b = ttk.Entry(self.matrix_label_frame, width=7, font=("Consolas", 10), justify=tk.CENTER, background="#e8f4f8")
            ent_b.grid(row=i+1, column=self.matrix_size+1, padx=3, pady=3)
            if self.matrix_size == 3:
                ent_b.insert(0, str(default_b[i]))
            else:
                ent_b.insert(0, "1.0")
            self.entry_b.append(ent_b)

    def get_matrix_data(self):
        n = self.matrix_size
        A = [[0.0]*n for _ in range(n)]
        b = [0.0]*n
        try:
            for i in range(n):
                for j in range(n):
                    A[i][j] = float(self.entry_A[i][j].get())
                b[i] = float(self.entry_b[i].get())
            return A, b
        except ValueError:
            raise ValueError("Por favor asegúrese de que todos los coeficientes sean valores numéricos válidos.")

    def log(self, text):
        self.txt_output.insert(tk.END, text + " \n")

    def solve_system(self):
        self.txt_output.delete("1.0", tk.END)
        try:
            A, b = self.get_matrix_data()
        except ValueError as e:
            messagebox.showerror("Error de Entrada", str(e))
            return
            
        method = self.method_var.get()
        self.log(f"=== EJECUCIÓN: {method.upper()} ===")
        self.log(f"Dimensión del sistema: {self.matrix_size} x {self.matrix_size}\n")
        
        if method == "Eliminación Gaussiana":
            self.run_eliminacion_gaussiana(A, b)
        elif method == "Gauss-Jordan":
            self.run_gauss_jordan(A, b)
        elif method == "Jacobi":
            self.run_jacobi(A, b)
        elif method == "Gauss-Seidel":
            self.run_gauss_seidel(A, b)

    def run_eliminacion_gaussiana(self, A, b):
        n = self.matrix_size
        # Fase de eliminación hacia adelante
        for j in range(n):
            # Pivoteo parcial simple
            max_row = j
            for r in range(j+1, n):
                if abs(A[r][j]) > abs(A[max_row][j]):
                    max_row = r
            if max_row != j:
                A[j], A[max_row] = A[max_row], A[j]
                b[j], b[max_row] = b[max_row], b[j]
                self.log(f"-> Pivoteo: Renglón {j+1} intercambiado con Renglón {max_row+1}")
                
            if abs(A[j][j]) < 1e-12:
                messagebox.showerror("Error Matemático", "El sistema no tiene solución única (pivote nulo).")
                return
                
            for i in range(j+1, n):
                factor = A[i][j] / A[j][j]
                self.log(f"Haciendo cero en posición A[{i+1}][{j+1}] usando factor {factor:.4f}")
                for k in range(j, n):
                    A[i][k] -= factor * A[j][k]
                b[i] -= factor * b[j]
                
        # Mostrar Matriz Triangular Superior
        self.log("\nMatriz Triangular Superior Resultante:")
        for r in range(n):
            row_str = " ".join([f"{A[r][c]:10.4f}" for c in range(n)])
            self.log(f"[ {row_str} | {b[r]:10.4f} ]")
            
        # Sustitución hacia atrás
        x = [0.0] * n
        for i in range(n-1, -1, -1):
            suma = sum(A[i][col] * x[col] for col in range(i+1, n))
            x[i] = (b[i] - suma) / A[i][i]
            
        self.log("\n=== SOLUCIÓN FINAL ===")
        for idx, val in enumerate(x):
            self.log(f"x{idx+1} = {val:.6f}")

    def run_gauss_jordan(self, A, b):
        n = self.matrix_size
        for j in range(n):
            # Pivoteo parcial
            max_row = j
            for r in range(j+1, n):
                if abs(A[r][j]) > abs(A[max_row][j]):
                    max_row = r
            if max_row != j:
                A[j], A[max_row] = A[max_row], A[j]
                b[j], b[max_row] = b[max_row], b[j]
                
            if abs(A[j][j]) < 1e-12:
                messagebox.showerror("Error Matemático", "Pivote nulo detectado. El método no puede continuar.")
                return
                
            # Normalizar fila del pivote
            pivote = A[j][j]
            for k in range(j, n):
                A[j][k] /= pivote
            b[j] /= pivote
            
            # Eliminación en filas superiores e inferiores
            for i in range(n):
                if i != j:
                    factor = A[i][j]
                    for k in range(j, n):
                        A[i][k] -= factor * A[j][k]
                    b[i] -= factor * b[j]
                    
            self.log(f"Paso {j+1}: Eliminación completada respecto a columna {j+1}")
            
        self.log("\n=== SOLUCIÓN FINAL ===")
        for idx, val in enumerate(b):
            self.log(f"x{idx+1} = {val:.6f}")

    def verificar_diagonal_dominante(self, A):
        n = self.matrix_size
        dominante = True
        for i in range(n):
            suma_fila = sum(abs(A[i][j]) for j in range(n) if j != i)
            if abs(A[i][i]) <= suma_fila:
                dominante = False
        if not dominante:
            self.log("ADVERTENCIA: La matriz NO es estrictamente dominante por la diagonal. El método podría divergir.\n")

    def run_jacobi(self, A, b):
        n = self.matrix_size
        tol = float(self.tol_entry.get())
        max_iter = int(self.max_iter_entry.get())
        
        self.verificar_diagonal_dominante(A)
        
        # Inicializar vectores
        x = [0.0] * n
        x_new = [0.0] * n
        
        self.log(f"{'Iteración':<10}" + "".join([f"{f'x{i+1}':<15}" for i in range(n)]) + f"{'Error Máx':<15}")
        self.log("-" * (25 + 15*n))
        self.log(f"{0:<10}" + "".join([f"{x[i]:<15.6f}" for i in range(n)]) + f"{'-':<15}")
        
        for k in range(1, max_iter + 1):
            for i in range(n):
                if abs(A[i][i]) < 1e-12:
                    messagebox.showerror("Error", f"Elemento diagonal nulo en fila {i+1}.")
                    return
                suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
                x_new[i] = (b[i] - suma) / A[i][i]
                
            # Calcular error (Norma infinito de la diferencia)
            error = max(abs(x_new[i] - x[i]) for i in range(n))
            
            # Registrar iteración en la caja de texto
            row_str = f"{k:<10}" + "".join([f"{x_new[i]:<15.6f}" for i in range(n)]) + f"{error:<15.6f}"
            self.log(row_str)
            
            # Actualizar vector completo para la siguiente iteración
            x = list(x_new)
            
            if error < tol:
                self.log(f"\nConvergencia exitosa alcanzada en {k} iteraciones.")
                return
                
        self.log(f"\nSe alcanzó el límite máximo de {max_iter} iteraciones sin lograr la tolerancia deseada.")

    def run_gauss_seidel(self, A, b):
        n = self.matrix_size
        tol = float(self.tol_entry.get())
        max_iter = int(self.max_iter_entry.get())
        
        self.verificar_diagonal_dominante(A)
        
        x = [0.0] * n
        self.log(f"{'Iteración':<10}" + "".join([f"{f'x{i+1}':<15}" for i in range(n)]) + f"{'Error Máx':<15}")
        self.log("-" * (25 + 15*n))
        self.log(f"{0:<10}" + "".join([f"{x[i]:<15.6f}" for i in range(n)]) + f"{'-':<15}")
        
        for k in range(1, max_iter + 1):
            error_max = 0.0
            for i in range(n):
                if abs(A[i][i]) < 1e-12:
                    messagebox.showerror("Error", f"Elemento diagonal nulo en fila {i+1}.")
                    return
                suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
                x_new_val = (b[i] - suma) / A[i][i]
                
                # Calcular error local e inmediatamente actualizar el elemento del vector
                err_local = abs(x_new_val - x[i])
                if err_local > error_max:
                    error_max = err_local
                    
                x[i] = x_new_val
                
            row_str = f"{k:<10}" + "".join([f"{x[i]:<15.6f}" for i in range(n)]) + f"{error_max:<15.6f}"
            self.log(row_str)
            
            if error_max < tol:
                self.log(f"\nConvergencia exitosa alcanzada en {k} iteraciones.")
                return
                
        self.log(f"\nSe alcanzó el límite máximo de {max_iter} iteraciones.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaEcuacionesApp(root)
    root.mainloop()
    app = SistemaEcuacionesApp(root)
    root.mainloop()

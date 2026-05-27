import numpy as np

def gauss_seidel(A, b, tolerance=1e-5, max_iterations=100):
    """
    Resuelve el sistema Ax = b usando el método de Gauss-Seidel.
    """
    n = len(b)
    
    # Vector inicial de ceros
    x = np.zeros_like(b, dtype=np.double)
    
    for k in range(max_iterations):
        x_old = x.copy()
        
        for i in range(n):
            # Suma de la parte ya actualizada (j < i)
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            
            # Suma de la parte de la iteración anterior (j > i)
            sum2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            
            # Cálculo del nuevo valor para x_i
            x[i] = (b[i] - sum1 - sum2) / A[i][i]
            
        # Calcular el error (norma máxima o infinita)
        error = np.linalg.norm(x - x_old, ord=np.inf)
        
        # Verificar convergencia
        if error < tolerance:
            print(f"Convergió en {k+1} iteraciones.")
            return x
            
    print("El método no convergió en el número máximo de iteraciones.")
    return x

# --- Ejemplo de uso ---
if __name__ == "__main__":
    A = np.array([[9, -1, -5],
                  [-3, 10, 7],
                  [8, 7, -3]], dtype=float)

    b = np.array([1, 5, 2], dtype=float)

    solucion = gauss_seidel(A, b)

    print("Solución:", solucion)

import sys

# Simulando el límite superior de la arquitectura (equivalente a Integer.MAX_VALUE)
max_val = sys.maxsize # Similar a 2,147,483,647 en 32-bit [cite: 151]
resultado = max_val + 1 # [cite: 151]

print("Máximo del sistema:", max_val) # [cite: 152]
print("Máximo + 1:", resultado) # [cite: 153]
# NOTA: En Python, esto simplemente dará el valor correcto positivo (ej. 9223372036854775808), 
# no lanzará error ni dará un número negativo, gracias a la gestión de memoria de Python.

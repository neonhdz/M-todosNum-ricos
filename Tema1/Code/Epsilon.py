import math

a = 0.1 + 0.1 + 0.1 # [cite: 57]
b = 0.3 # [cite: 58]

print("Valor de a (0.1*3):", a) # [cite: 59]
print("Valor de b:", b) # [cite: 60]

print("\n--- Comparación con '==' ---") # [cite: 62]
if a == b: # [cite: 63, 64]
    print("Resultado: Son iguales") # [cite: 65]
else:
    print("Resultado: SON DIFERENTES (Error esperado)") # [cite: 68]

# --- La Solución: Uso de un margen de error (Épsilon) ---
epsilon = 0.00001 # [cite: 70]
print(f"\n--- Comparación con Épsilon ({epsilon}) ---") # [cite: 71]

# También equivalente a: math.isclose(a, b, rel_tol=epsilon)
if abs(a - b) < epsilon: # [cite: 71]
    print("Resultado: Son iguales (dentro del margen de error)") # [cite: 72]
else:
    print("Resultado: Son diferentes") # [cite: 75]

import decimal

iteraciones = 1000000 # [cite: 91]
incremento = 0.1 # [cite: 92]

# 1. Acumulación usando 'float' (equivalente a double en Python)
suma_float = 0.0 # [cite: 94]
for _ in range(iteraciones): # [cite: 95]
    suma_float += incremento # [cite: 96]

esperado = iteraciones * incremento # [cite: 99]

print("Resultado esperado:", esperado) # [cite: 101]
print("Resultado float:", suma_float) # [cite: 102]
print("Diferencia (Error):", suma_float - esperado) # [cite: 103]

# 2. Solución usando 'Decimal' para precisión absoluta
suma_bd = decimal.Decimal("0.0") # [cite: 105]
incremento_bd = decimal.Decimal("0.1") # [cite: 106]

for _ in range(iteraciones): # [cite: 107]
    suma_bd += incremento_bd # [cite: 109]

print("\n--- Solución con Decimal ---") # [cite: 110]
print("Resultado exacto:", suma_bd) # [cite: 111]

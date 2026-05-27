import decimal

# Un float en Python (equivalente a double) pierde precisión
numero_grande = 1.0e16 # [cite: 26]
numero_pequeno = 1.0 # [cite: 27]
resultado = numero_grande + numero_pequeno # [cite: 28]

print("--- Demostración de Pérdida de Precisión ---") # [cite: 29]
print("Número Grande:", numero_grande) # [cite: 30]
print("Número Pequeño:", numero_pequeno) # [cite: 30]
print("Suma Resultante:", resultado) # [cite: 31]

if resultado == numero_grande: # [cite: 33]
    print("\nRESULTADO: El número pequeño 'desapareció'.") # [cite: 34]
    print("La suma es igual al número original debido a la falta de bits en la mantisa.") # [cite: 35, 36]

# --- SOLUCIÓN USANDO DECIMAL (Equivalente a BigDecimal) ---
decimal.getcontext().prec = 20 # Ajustamos la precisión necesaria
bd_grande = decimal.Decimal("1.0e16") # 
bd_pequeno = decimal.Decimal("1.0") # 
bd_resultado = bd_grande + bd_pequeno # 

print("\n--- Solución con Decimal ---") # [cite: 41]
print("Suma Exacta:", bd_resultado) # [cite: 41]

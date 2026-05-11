from decimal import Decimal

# --- Demostración de Pérdida de Precisión ---
# Un float en Python (que es un double de 64 bits) tiene ~15-17 dígitos de precisión.
numero_grande = 1.0e16  # 10,000,000,000,000,000.0
numero_pequeno = 1.0
resultado = numero_grande + numero_pequeno

print("--- Demostración de Pérdida de Precisión ---")
print(f"Número Grande:  {numero_grande:.1f}")
print(f"Número Pequeño: {numero_pequeno:.1f}")
print(f"Suma Resultante: {resultado:.1f}")

# Verificación lógica
if resultado == numero_grande:
    print("\nRESULTADO: El número pequeño 'desapareció'.")
    print("La suma es igual al número original debido a la falta de bits en la mantisa.")


# --- SOLUCIÓN USANDO DECIMAL ---
# Usamos strings para asegurar que la precisión sea absoluta desde el inicio
bd_grande = Decimal("1.0e16")
bd_pequeno = Decimal("1.0")
bd_resultado = bd_grande + bd_pequeno

print("\n--- Solución con Decimal (Python) ---")
# to_eng_string() o f-string directo para evitar notación científica si se desea
print(f"Suma Exacta:    {bd_resultado:f}")

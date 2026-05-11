import math
from decimal import Decimal, getcontext

# --- 1. EL PROBLEMA (Punto flotante estándar) ---
a = 0.1
b = 0.2
suma_float = a + b

print("--- El Problema ---")
print(f"Suma simple (0.1 + 0.2): {suma_float}")
print(f"¿Es igual a 0.3?: {suma_float == 0.3}\n")


# --- 2. SOLUCIÓN PARA DINERO/PRECISIÓN (Módulo Decimal) ---
# Nota: Siempre usa strings '0.1' para evitar que el float corrompa el Decimal
suma_decimal = Decimal('0.1') + Decimal('0.2')

print("--- Solución con Decimal (Exacto) ---")
print(f"Suma con Decimal: {suma_decimal}")
print(f"¿Es igual a 0.3?: {suma_decimal == Decimal('0.3')}\n")


# --- 3. SOLUCIÓN PARA COMPARACIONES (math.isclose) ---
print("--- Solución para Comparar Floats ---")
if math.isclose(suma_float, 0.3, rel_tol=1e-9):
    print("math.isclose dice: Son prácticamente iguales.\n")


# --- 4. SOLUCIÓN PARA PRESENTACIÓN (Redondeo) ---
print("--- Solución Visual (Redondeo) ---")
print(f"Resultado redondeado: {round(suma_float, 2)}")
print(f"Resultado formateado: {suma_float:.1f}")

import math

# Devuelve un float. En números gigantes, pierde precisión.
resultado_math = math.pow(2, 31) # [cite: 201]
print("Resultado con math.pow:", resultado_math) # [cite: 202]

# Solución Python: Usar el operador nativo de exponente que devuelve un INT exacto.
resultado_nativo = 2 ** 31
print("Resultado correcto con '**':", resultado_nativo)

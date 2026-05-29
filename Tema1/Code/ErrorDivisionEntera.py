a = 5 # [cite: 188]
b = 2 # [cite: 188]

# Operación clásica de Python (Resultado exacto 2.5)
resultado_correcto = a / b
print("Resultado en Python ('/'):", resultado_correcto)

# Replicando el error de Java (División entera que produce 2 en lugar de 2.5) [cite: 186]
resultado_java = a // b 
print("Resultado estilo Java ('//'):", resultado_java)

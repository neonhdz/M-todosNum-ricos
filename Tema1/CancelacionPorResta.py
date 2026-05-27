# Dos números muy grandes y muy cercanos
x = 1234567890.1234567 # [cite: 133]
y = 1234567890.1234560 # [cite: 134]

# El resultado esperado es 0.0000007, pero dará inexacto
resultado = x - y # [cite: 136]
print("Resultado real:", resultado) # [cite: 137]

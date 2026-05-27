numeros = [1, 2, 3] # [cite: 250]

try:
    print(numeros[3]) # Índice inválido [cite: 251]
except IndexError as e:
    print("Excepción generada:", e)

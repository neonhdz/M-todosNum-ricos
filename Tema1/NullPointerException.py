texto = None # [cite: 235]

try:
    print(len(texto)) # Intentar obtener la longitud de None [cite: 236]
except TypeError as e:
    # Capturamos la excepción en tiempo de ejecución
    print("Excepción generada:", e)

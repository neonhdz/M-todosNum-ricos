a = "Hola" # [cite: 212]
# Forzamos una nueva instancia en memoria para el ejemplo
b = "".join(['H', 'o', 'l', 'a']) 

# En Python, '==' compara el VALOR, que es lo correcto (equivalente a equals de Java)
if a == b: 
    print("Son iguales en contenido (correcto)")

# El operador 'is' compara MEMORIA (equivalente al '==' defectuoso de Java)
if a is b:
    print("Tienen la misma referencia")
else:
    print("SON DIFERENTES EN MEMORIA (Error simulado de Java)") # [cite: 220]

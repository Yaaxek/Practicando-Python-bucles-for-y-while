"""
André está probando una nueva función en el backend de 
Buscante que procesa datos en un bucle. Durante las 
, se dio cuenta de que el sistema dejó de responder y 
sospecha que el problema está en un bucle infinito.
¿Cuál es el problema del código de André y cómo resolverlo?
Que anteriorme no tenia una condicion de salida, por lo que 
el bucle se ejecutaba infinitamente. Se agregó la condicion 
de contador += 1 para que el bucle se ejecute 10 veces.
"""
contador = 0
while contador < 10:
    contador += 1
    print("Procesando datos...")
    
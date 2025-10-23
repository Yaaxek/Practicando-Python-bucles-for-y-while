"""
Estás recibiendo una lista de valores que representan 
los productos de tu tienda virtual y te gustaría 
calcular la suma total de esos productos para entender 
el desempeño financiero semanal.
Crea un programa para implementar la suma.
"""
"""
Opción 1:
valores = [10, 20, 30, 40, 50]
suma = sum(valores)
print(f'La suma total de los ingresos es: {suma}')
"""
valores = [10, 20, 30, 40, 50]
suma = 0
for valor in valores:
    suma += valor
print(f'La suma total de los ingresos es: {suma}')
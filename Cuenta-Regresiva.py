"""
Aline está implementando una funcionalidad que muestra 
mensajes personalizados para los clientes durante una 
promoción especial de su nueva librería. El sistema debe 
mostrar un mensaje de cuenta regresiva personalizado para 
cada número de 10 a 1, y al final mostrar el mensaje: 
"¡Aprovecha la promoción ahora!".
Crea un programa que utilice un bucle for para mostrar los 
siguientes mensajes:
Para números pares, muestra: "Faltan solo <número> segundos - 
¡No pierdas esta oportunidad!".
Para números impares, muestra: "La cuenta continúa: <número> 
segundos restantes.".
Al final de la cuenta, muestra el mensaje: "¡Aprovecha la 
promoción ahora!".
"""
cuenta_regresiva=10
while cuenta_regresiva > 0:
    if cuenta_regresiva%2 == 0:
        print(f"Faltan solo {cuenta_regresiva} segundos - ¡No pierdas esta oportunidad!")
    else:
        print(f"La cuenta continúa: {cuenta_regresiva} segundos restantes.")
    cuenta_regresiva -= 1
print( "¡Aprovecha la promoción ahora!")
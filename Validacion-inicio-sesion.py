while True:
    usuario=input("Ingrese su usuario: ")
    contrasena=input("Ingrese su contraseña: ")
    if len(usuario) >= 5 and len(contrasena) >= 8:
        print("¡Registro realizado con éxito!")
        break
    elif len(usuario) < 5:
        print("El nombre de usuario debe tener al menos 5 caracteres.")
    elif len(contrasena) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
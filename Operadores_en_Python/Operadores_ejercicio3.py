'''
Nombre:Patricia Pérez Cruz
Fecha: 25 de octubre de 2024
Descripción:
Tercer ejercicio para poner en práctica mis conocimientos adquiridos sobre
los operadores lógicos.
Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña.
'''

#a) Internamente declare dos cadenas constantes, una para el usuario y otra para la contraseña.
#➡️ Aquí declaro mis constantes las dos como cadenas para que no surjan errores 😀
USUARIO_CONSTANTE = "Patricia"
CONTRASEÑA_CONSTANTE = "1234"

#b) Pida al usuario una cadena con el usuario.
print(" *** SISTEMA DE AUTENTIFICACIÓN ***")
print()
usuario_entrada = input("Ingrese su usuario: ")

#c) Pida al usuario una cadena con la contraseña.
contraseña_entrada = input("Ingrese su contraseña: ")

#d) Si ambas cadenas son iguales a las cadenas declaradas internamente, entonces el usario se autenticó correctamente.
#⬆️ A continuación compararé las dos cadenas para saber si lo que ingresaron coincide con lo declarado internamente
#pero para eso primero voy a convertirlos a booleanos

#e) Muestre el resultado en consola como valor booleano (True/False).

print(f"¿El acceso fue correcto?: {usuario_entrada == USUARIO_CONSTANTE and contraseña_entrada == CONTRASEÑA_CONSTANTE}")

#d) Si ambas cadenas son iguales a las cadenas declaradas internamente, entonces el usario se autenticó correctamente.
#⬆️ Lo anterior se va a comprobar si el en "print" el resultado es "TRUE" o "FALSE"


"""
Nota: Las cadenas no tiene que ser convertidas a minúsculas.
"""
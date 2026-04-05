##Implemente el cifrado César, que consiste en desplazar cada letra del alfabeto
##una cantidad fija de posiciones. El programa debe:
##1. 
##2. 
##3. 
##4. 
##Solicitar un mensaje al usuario.
##Solicitar un valor de desplazamiento (número entero).
##Mostrar el mensaje cifrado.
##Mostrar el mensaje descifrado a partir del cifrado (para verificar que
##funciona).
##Las letras deben rotar (después de la Z viene la A). Los caracteres que no sean
##letras (espacios, signos de puntuación, números) se mantienen sin cambios. Debe
##funcionar tanto con mayúsculas como con minúsculas, preservando el formato
##original.

Mensaje = input("Ingrese el mensaje a encriptar: ")
Num_Cifrado = int(input("Ingrese numéricamente el número a desplazar: "))
Mensaje_Encriptado = ""

for letra in Mensaje:
    if "a" <= letra <= "z":
        letra_original = ord(letra) - 97 ##valor de 'a' en ASCII
        letra_encriptada = (letra_original + Num_Cifrado) % 26
        Mensaje_Encriptado = Mensaje_Encriptado + chr(letra_encriptada + 97)
    elif "A" <= letra <= "Z":
        letra_original = ord(letra) - 65 ##valor de 'a' en ASCII
        letra_encriptada = (letra_original + Num_Cifrado) % 26
        Mensaje_Encriptado = Mensaje_Encriptado + chr(letra_encriptada + 65)
    else:
        Mensaje_Encriptado = Mensaje_Encriptado + letra

print(f"Mensaje encriptado: {Mensaje_Encriptado}")
##Valide una dirección de email ingresada por el usuario con los siguientes criterios:
## Contiene exactamente un @.
## Tiene al menos un carácter antes del @.
## Tiene al menos un punto (.) después del @.
## No empieza ni termina con @ ni con ..
## La parte después del último punto tiene al menos 2 caracteres (el dominio).

mail = input("Ingrese dirección de e-mail: ").strip()
validez = False
cant_arroba = mail.count("@")
empieza_mal = mail.startswith("@") or mail.startswith(".")
termina_mal = mail.endswith("@") or mail.endswith(".")
if cant_arroba == 1 and not empieza_mal and not termina_mal:
    usuario, otro = mail.split("@")
    if len(usuario) > 0 and "." in otro:
        dominio = otro.split(".")
        largo = dominio[-1]
        if len(largo) >= 2:
            validez = True
if validez:
    print("El e-mail es válido.")
else:
    print("El e-mail es inválido.")
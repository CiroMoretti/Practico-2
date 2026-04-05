##Calcule el costo de envío de un paquete según su peso (en kg) y la zona de
##destino. El usuario debe ingresar ambos valores.
##Las zonas válidas son: local, regional, nacional.
##Si la zona no es válida, debe indicar el error

##Peso / Zona Local Regional Nacional
##1 kg         $500   $1000   $2000
##1 y 5 kg     $1000  $2500   $4500
##Más de 5 kg  $2000  $5000   $8000

Zonas = {"Local": {
            "1k": 500,
            "1-5k": 1000, 
            "mas-5k": 2000
        },
        "Regional": {
            "1k": 1000, 
            "1-5k": 2500, 
            "mas-5k": 5000
        },
        "Nacional": {
            "1k": 2000,
            "1-5k": 4500,
            "mas-5k": 8000
        }
        }

Peso_Paquete = float(input("Ingrese peso del paquete: "))
Destino_Paquete= input("Ingrese zona de destino: ").capitalize()

if Destino_Paquete in Zonas:
    if Peso_Paquete <= 1:
        Peso_Costo = "1k"
    elif Peso_Paquete >1 and Peso_Paquete <= 5:
        Peso_Costo = "1-5k"
    else:
        Peso_Costo = "mas-5k"
    Costo = Zonas[Destino_Paquete] [Peso_Costo]
    print(f"El costo del envío es: ${Costo}")
else:
    print("La zona ingresada no es valida")
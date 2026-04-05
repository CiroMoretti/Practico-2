##Eres ayudante en una cátedra que recibió registros de alumnos desde
##múltiples fuentes. Los datos llegaron con errores: nombres con formatos
##inconsistentes, notas faltantes, registros nulos y alumnos duplicados con distintas
##notas.
##Tu tarea es limpiar los datos y generar un listado final.
##Debe realizar las siguientes operaciones:
##Eliminar registros con nombre nulo, vacío o solo espacios.
##Eliminar registros con nota nula, vacía o no numérica (como "absent").
##Normalizar nombres a formato título y estados a formato título.
##Eliminar duplicados por nombre, quedándose con la nota más alta de
##cada alumno.
##Ordenar alfabéticamente por nombre.

students = [
{"name": "  Ana García ", "grade": "8", "status":
"aprobado"},
{"name": "pedro lópez", "grade": "4", "status":
"DESAPROBADO"},
{"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":
"Aprobado"},
{"name": "ana garcía", "grade": "9", "status":
"aprobado"},
{"name": None, "grade": "7", "status": "aprobado"},
{"name": "Luis Martínez  ", "grade": None, "status":
"aprobado"},
{"name": " carlos RUIZ", "grade": "6", "status":
"aprobado"},
{"name": "PEDRO LÓPEZ ", "grade": "3", "status":
"desaprobado"},
{"name": "  ", "grade": "5", "status": "aprobado"},
{"name": "María Fernández", "grade": "7", "status":
"APROBADO"},
{"name": "Sofía Torres", "grade": "9", "status":
"Aprobado"},
{"name": "  sofía torres ", "grade": "8", "status":
"aprobado"},
{"name": "Carlos Ruiz", "grade": "6", "status":
"APROBADO"},
{"name": "Roberto Díaz", "grade": "absent", "status":
"ausente"},
{"name": "roberto díaz", "grade": "", "status":
"Ausente"},
{"name": None, "grade": None, "status": None},
{"name": "Laura Méndez", "grade": "7", "status":
"aprobado"},
{"name": "  laura méndez", "grade": "8", "status":
"Aprobado"},
{"name": "GABRIELA RÍOS", "grade": "5", "status":
"aprobado"},
{"name": "gabriela ríos ", "grade": "4", "status":
"Desaprobado"},
]

Lista_Bien = []
for s in students:
    if s["name"] is not None and not s["name"].isspace():
        if s["grade"] is not None and str(s["grade"]).isdigit():
            nombre = s["name"].strip().title()
            estado = s["status"].strip().title()
            nota = int(s["grade"])
            Dato_Completo = {"name": nombre, 
                            "grade": nota, 
                            "status": estado}
            Repetido = next((n for n in Lista_Bien if n["name"] == nombre), None)
            if Repetido is None:
                Lista_Bien.append(Dato_Completo)
            elif nota > Repetido["grade"]:
                Repetido["grade"] = nota
                Repetido["status"] = estado


Lista_Bien.sort(key = lambda x: x["name"])
print(Lista_Bien)
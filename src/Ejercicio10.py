def procesamiento_de_rondas(rounds):
    Puntaje_Total = {}
    Ganadas= {}
    for i in rounds:
        Puntaje_Actual = []
        Ronda = i["scores"]
        for nombre, juez in Ronda.items():
            puntos = sum(juez.values())
            if nombre not in Puntaje_Total:
                Puntaje_Total[nombre]= [puntos]
            else:
                Puntaje_Total[nombre].append(puntos)
            Puntaje_Actual.append([nombre, puntos])
        Puntaje_Actual.sort(key= lambda x: x[1], reverse= True)
        ganador_nombre = Puntaje_Actual[0][0]
        ganador_puntos = Puntaje_Actual[0][1]
        print(f"Ganador de la ronda de {i["theme"]}: {ganador_nombre} ({ganador_puntos} puntos).")
        Ganadas[ganador_nombre] =Ganadas.get(ganador_nombre, 0) + 1
    return Puntaje_Total, Ganadas

def puntajes_finales (Puntaje_Total, Ganadas):
    Puntaje_Final = []
    for nombre, puntos in Puntaje_Total.items():
            total = sum(puntos)
            rond_ganadas = Ganadas.get(nombre, 0)
            mejor_ronda= max(puntos)
            promedio = total / len(puntos)
            datos = [nombre, total, rond_ganadas, mejor_ronda, promedio]
            Puntaje_Final.append(datos)
    Puntaje_Final.sort(key= lambda x: x[1], reverse= True)
    return Puntaje_Final

def imprimir_tabla_final(Puntaje_Final):
    print("Tabla de posiciones final:", "\n", "-" * 100)
    print(f"{"Posición": <2}    {"Cocinero": <20}{"Puntos": <8}{"Rondas Ganadas": <2}{"Mejor Ronda": <5}{"Promedio": <6}")
    for i, p in (enumerate(Puntaje_Final, start= 1)):
        print(f"{i: <4}     {p[0]:<20}      {p[1]:<8}       {p[2]:<2}       {p[3]:<5}       {p[4]:<6}")
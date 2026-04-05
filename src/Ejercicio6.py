##Dadas las siguientes publicaciones de una red social, extraiga todos los
##hashtags (palabras que comienzan con #), cuente la frecuencia de cada uno, y
##muestre los hashtags trending (los que aparecen más de una vez).
posts = [
"Arrancando el lunes con energía #Motivación #NuevaSemana",
"Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
"No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
"Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
"Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
"Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
"Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
"Finde de lluvia, maratón de series #SerieAdicta #Relax",
"Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]

Lista_Hashtags = {}
for p in posts:
    hashtag = p.split()
    for h in hashtag:
        if h.startswith("#"):
            Lista_Hashtags[h] = Lista_Hashtags.get(h, 0) + 1
print(len(Lista_Hashtags))

Hashtags_Unicos = 0

Hashtags_Ordenados = sorted(Lista_Hashtags.items(), key = lambda x: x[1], reverse=True) 

print("Hashtags trending:")
for h, c in Hashtags_Ordenados:
    Hashtags_Unicos = Hashtags_Unicos + 1
    if c > 1: 
        print(f"{h}: {c}")

print(f"Total de hashtags únicos: {Hashtags_Unicos}")
##Dada la siguiente playlist con canciones y sus duraciones en formato "m:ss"
##Calcule la duración total de la playlist en formato Xm Ys, y encuentre la
##canción más larga y la más corta.
##Nota: Deberá convertir las duraciones de string a valores
##numéricos para poder operar con ellas.

##Salida esperada:
##Duración total: 46m 53s
##Canción más larga: "Stairway to Heaven" (8:02)
##Canción más corta: "Imagine" (3:07)


playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

Duración_Playlist = 0
for cancion in playlist:
    dur = cancion["duration"].split(":")
    mins = int(dur[0])
    seg = int(dur[1])
    mins = mins * 60
    Duración_Playlist = Duración_Playlist + mins + seg
print(f"Duración total de la Playlist: {Duración_Playlist // 60}:{Duración_Playlist % 60}.")

def duracion_a_segundos(cancion): 
    dur = cancion["duration"].split(":")
    return int(dur[0]) * 60 + int(dur[1])
Canción_Más_Larga = max(playlist, key=duracion_a_segundos)
Canción_Más_Corta = min(playlist, key=duracion_a_segundos)
print(f"Canción más larga: {Canción_Más_Larga}")
print(f"Canción más corta: {Canción_Más_Corta}")
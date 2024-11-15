#Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
#ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino

#F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
#manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

#a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#b. mostrar los nombre de los superhéroes femeninos;
#c. mostrar los nombres de los personajes masculinos;
#d. determinar el nombre del superhéroe del personaje Scott Lang;
#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#con la letra S;
#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#de superhéroes.

from cola import Queue
personajes_mcu = [
    {"nombre_personaje": "Tony Stark", "nombre_superheroe": "Iron Man", "genero": "M"},
    {"nombre_personaje": "Steve Rogers", "nombre_superheroe": "Capitán América", "genero": "M"},
    {"nombre_personaje": "Natasha Romanoff", "nombre_superheroe": "Black Widow", "genero": "F"},
    {"nombre_personaje": "Thor Odinson", "nombre_superheroe": "Thor", "genero": "M"},
    {"nombre_personaje": "Bruce Banner", "nombre_superheroe": "Hulk", "genero": "M"},
    {"nombre_personaje": "Wanda Maximoff", "nombre_superheroe": "Scarlet Witch", "genero": "F"},
    {"nombre_personaje": "Peter Parker", "nombre_superheroe": "Spider-Man", "genero": "M"},
    {"nombre_personaje": "Carol Danvers", "nombre_superheroe": "Captain Marvel", "genero": "F"},
    {"nombre_personaje": "T'Challa", "nombre_superheroe": "Black Panther", "genero": "M"},
    {"nombre_personaje": "Gamora", "nombre_superheroe": "Gamora", "genero": "F"},
    {"nombre_personaje":"Scott Lang","nombre_superheroe":"Ant-Man","genero":"M"}
]
cola = Queue()
cola_aux = Queue()
list_femenino = []
lista_masculino = []
lista_letras = []
for char in personajes_mcu:
    cola.arrive(char)

for i in range(cola.size()):
    aux = cola.attention()
    
    #punto a  determinar el nombre del personaje de la superhéroe Capitana Marvel;
if aux["nombre_superheroe"] == "Captain Marvel":
    print("el nombre de la capitana marvel es: ",aux["nombre_personaje"])

    #punto b mostrar los nombre de los superhéroes femeninos;
    if aux["genero"] == "F" :
        list_femenino.append(aux["nombre_superheroe"])

     #punto c  mostrar los nombres de los personajes masculinos;
    if aux["genero"] == "M":
        lista_masculino.append(aux)

     #punto d  determinar el nombre del superhéroe del personaje Scott Lang;
    if aux["nombre_personaje"]== "Scott Lang":
        print("el nombre de superheroe de Scott Lang: ", aux["nombre_superheroe"])

     #punto e mostrar todos los datos de los personajes que coienzan con la letra "S"
    if aux["nombre_personaje"].startswith("S") == True:
        lista_letras.append(aux)

    #punto f determinar si el personaje carol danver se encuentra e indicar el nombre 
    if aux["nombre_personaje"]== "Carol Danvers":
        print("el nombre de superheroe de Carol Danvers es: ",aux["nombre_superheroe"])
    cola_aux.arrive(aux)
for i in range(cola_aux.size()):
    cola.arrive(cola_aux.attention())


print("personajes feminos: ",list_femenino)

print("personajes masculinos : ",lista_masculino)

print("personajes que empiezan con S: ", lista_letras)




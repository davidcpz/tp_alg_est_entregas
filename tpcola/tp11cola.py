
#Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
#de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
#a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
#b. indicar el plantea natal de Luke Skywalker y Han Solo
#c. insertar un nuevo personaje antes del maestro Yoda
#d. eliminar el personaje ubicado después de Jar Jar Bink
from cola import Queue

pj = [
    {"name": "Luke Skywalker", "planet": "Tatooine"},
    {"name": "Anakin Skywalker", "planet": "Tatooine"},
    {"name": "Leia Organa", "planet": "Alderaan"},
    {"name": "Yoda", "planet": "Dagobah"},
    {"name": "Han Solo", "planet": "Corellia"},
    {"name": "Jar Jar Binks", "planet": "Naboo"},
    {"name": "Padme Amidala", "planet": "Naboo"}
]

personajes = Queue()
queue_aux = Queue()


for personaje in pj:
    personajes.arrive(personaje)


personajes_especiales = []
planeta_luke = None
planeta_han = None


while personajes.size() > 0:
    aux = personajes.attention()
    

    if aux["planet"] in ["Alderaan", "Endor", "Tatooine"]:
        personajes_especiales.append(aux)
    

    if aux["name"] == "Luke Skywalker":
        planeta_luke = aux["planet"]
    if aux["name"] == "Han Solo":
        planeta_han = aux["planet"]


    queue_aux.arrive(aux)


while queue_aux.size() > 0:
    personajes.arrive(queue_aux.attention())


if personajes_especiales:
    print("Personajes de Alderaan, Endor o Tatooine:")
    for personaje in personajes_especiales:
        print(personaje)
        

if planeta_luke:
    print(f"Planeta de Luke Skywalker: {planeta_luke}")
if planeta_han:
    print(f"Planeta de Han Solo: {planeta_han}")
    

for personaje in pj:
    personajes.arrive(personaje)


nuevo_personaje = {"name": "Pereyra", "planet": "Endor"} 
yoda = False 


while personajes.size() > 0:
    aux = personajes.attention()
    

    if aux["name"] == "Yoda" and not yoda:
        queue_aux.arrive(nuevo_personaje)
        yoda = True 


    queue_aux.arrive(aux)


while queue_aux.size() > 0:
    personajes.arrive(queue_aux.attention())

print("Cola después de insertar a Pereyra antes de Yoda:")
while personajes.size() > 0:
    personaje = personajes.attention()
 
    print(f"Nombre: {personaje['name']}, Planeta: {personaje['planet']}")
    

queue_aux = Queue() 
eliminar_siguiente = False


while personajes.size() > 0:
    aux = personajes.attention()
    
    
    if aux["name"] == "Jar Jar Binks":
        eliminar_siguiente = True
        queue_aux.arrive(aux)  
        continue

    
    if eliminar_siguiente:
        eliminar_siguiente = False
        continue


    queue_aux.arrive(aux)

while queue_aux.size() > 0:
    personajes.arrive(queue_aux.attention())

print("mostrar despues de las modificaciones:")

while personajes.size() > 0:
    print(personajes.attention())
    





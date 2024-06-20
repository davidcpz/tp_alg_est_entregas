#Dada una lista de superhéroes de comics, de los cuales se 
# conoce su nombre, año aparición, casa de comic a la que
#pertenece (Marvel o DC) y biografía, implementar la 
#funciones necesarias para poder realizar las siguientes actividades:

#a. eliminar el nodo que contiene la información de Linterna 
# Verde;

superheroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
 {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
 {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
 {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
 {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hanbiografiak Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos. Usa un traje que lo hace pequeño."
}]




def eliminar_superheroe(superheroes, nombre):
    return [heroe for heroe in superheroes if heroe["nombre"] != nombre]

superheroes = eliminar_superheroe(superheroes, "Linterna Verde")


#b. Mostrar el año de aparición de Wolverine
def mostrar_ano_aparicion(superheroes, nombre):
    for heroe in superheroes:
        if heroe["nombre"] == nombre:
            return heroe["año_aparicion"]
    return None

ano_aparicion_wolverine = mostrar_ano_aparicion(superheroes, "Wolverine")
print(f"Año de aparición de Wolverine: {ano_aparicion_wolverine}")

#c. Cambiar la casa de Dr. Strange a Marvel

def cambiar_casa_comic(superheroes, nombre, nueva_casa):
    for heroe in superheroes:
        if heroe["nombre"] == nombre:
            heroe["casa_comic"] = nueva_casa

cambiar_casa_comic(superheroes, "Dr. Strange", "Marvel")


#d. Mostrar el nombre de aquellos superhéroes que en su 
#biografía menciona la palabra “traje” o “armadura”

def superheroes_con_palabra(superheroes, palabras):
    resultado = []
    for heroe in superheroes:
        for palabra in palabras:
            if palabra in heroe["biografia"]:
                resultado.append(heroe["nombre"])
                break
    return resultado

nombres_con_traje_o_armadura = superheroes_con_palabra(superheroes, ["traje", "armadura"])
print(f"Superhéroes con 'traje' o 'armadura' en su biografía: {nombres_con_traje_o_armadura}")


#e. Mostrar el nombre y la casa de los superhéroes cuya fecha
#  de aparición sea anterior a 1963

def superheroes_anteriores_a(superheroes, año):
    resultado = []
    for heroe in superheroes:
        if heroe["año_aparicion"] < año:
            resultado.append((heroe["nombre"], heroe["casa_comic"]))
    return resultado

superheroes_antes_1963 = superheroes_anteriores_a(superheroes, 1963)
print(f"Superhéroes anteriores a 1963: {superheroes_antes_1963}")


#f. Mostrar la casa a la que pertenece Capitana Marvel y Mujer
#  Maravilla

def casa_de_superheroes(superheroes, nombres):
    resultado = {}
    for heroe in superheroes:
        if heroe["nombre"] in nombres:
            resultado[heroe["nombre"]] = heroe["casa_comic"]
    return resultado

casas_capt_marvel_mujer_maravilla = casa_de_superheroes(superheroes, ["Capitana Marvel", "Mujer Maravilla"])
print(f"Casa de Capitana Marvel y Mujer Maravilla: {casas_capt_marvel_mujer_maravilla}")


#g. Mostrar toda la información de Flash y Star-Lord

def info_superheroes(superheroes, nombres):
    resultado = []
    for heroe in superheroes:
        if heroe["nombre"] in nombres:
            resultado.append(heroe)
    return resultado

info_flash_starlord = info_superheroes(superheroes, ["Flash", "Star-Lord"])
print(f"Información de Flash y Star-Lord: {info_flash_starlord}")

#h. Listar los superhéroes que comienzan con la letra B, M y S

def superheroes_con_letras(superheroes, letras):
    resultado = []
    for heroe in superheroes:
        if heroe["nombre"][0] in letras:
            resultado.append(heroe["nombre"])
    return resultado

superheroes_bms = superheroes_con_letras(superheroes, ["B", "M", "S"])
print(f"Superhéroes que comienzan con B, M y S: {superheroes_bms}")


#i. Determinar cuántos superhéroes hay de cada casa de comic

def contar_superheroes_por_casa(superheroes):
    contador = {"Marvel": 0, "DC": 0}
    for heroe in superheroes:
        if heroe["casa_comic"] in contador:
            contador[heroe["casa_comic"]] += 1
    return contador

cantidad_por_casa = contar_superheroes_por_casa(superheroes)
print(f"Cantidad de superhéroes por casa de cómic: {cantidad_por_casa}")


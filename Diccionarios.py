# Diccionario que almacena palabras en inglés y español (cadenas)
english_to_spanish = {'table': 'mesa', 'apple': 'manzana', 'dog': 'perro', 'clock': 'reloj'}

# Diccionario que almacena edades de personas (enteros)
ages = {'Claire': 24, 'Peter': 35, 'Rafael': 13, 'Mere': 4, 'Jhon': 39}

#Un diccionario de favoritos (valores de diferentes tipos)
my_favorites = {'color':'blue', 'food': 'butter paneer', 'decimal': 3.14159, 'number': 9}

/*****************************************************************************************/
# Diccionario que almacena palabras en inglés y español (cadenas)
english_to_spanish = {'table': 'mesa', 'apple': 'manzana', 'dog': 'perro', 'clock': 'reloj'}

# Diccionario que almacena edades de personas (enteros)
ages = {'Claire': 24, 'Peter': 35, 'Rafael': 13, 'Mere': 4, 'Monty': 68}

#Un diccionario de favoritos (valores de diferentes tipos)
my_favorites = {'color':'blue', 'food': 'butter paneer', 'decimal': 3.14159, 'number': 9}

#Imprimir valores
print(english_to_spanish)
print(ages["Rafael"])
print(my_favorites["food"])

/*********************************************************************************************/
names = ["Sarah", "Jose", "Tane", "Monty"]
fav_foods = ["Apples", "Salad", "Pizza", "Nachos"]

foods_dict = dict(zip(names, fav_foods))

#Imprimir el diccionario completo para ver el resultado
print(foods_dict)

#Imprimir la comida favorita de José.
print(foods_dict["Jose"])

/*************************************************************************************************/
# Diccionario que almacena edades de personas (enteros)
ages = {'Claire': 24, 'Peter': 35, 'Rafael': 13, 'Mere': 4, 'Monty': 68}

# Imprimir un valor
print(ages['Claire'])

# Modificar la edad de Claire
ages['Claire'] = 25


# Agregar a Lisa, que tiene 42 años
ages['Lisa'] = 42


# Eliminar a Monty del diccionario
del ages['Monty']


# Imprimir el diccionario completo 
print(ages)

/**********************************************************************************************/
mas sobre diccionarios*/
/****************************************************************************************
# Crear un diccionario de los primeros 3 estados de EE. UU. y sus abreviaturas.
us_states = {'alabama': 'AL', 'alaska': 'AK','arizona': 'AZ'}

# Crear un diccionario de nombres y direcciones de sitios web
websites = {'google' :'http://google.com','facebook': 'http://facebook.com','twitter': 'http://twitter.com'}

/*******************************************************/
# Crear un diccionario de valores calóricos por cada 100 g de alimentos comunes.
calorie_values = {'mantequilla': 770,'hojuelas de maíz' : 364,'apio' : 6,'fresas' : 26}
  
# Crear un diccionario de nombres de usuario y puntuaciones de jugadores
player_scores = {'CoolKiwi': 1125,'Avenger909' : 1275,'InfamousCandyKid' : 1050}
/*********************************************************
# Crear un diccionario de algunas de las lecciones del nivel 1 de Python de Code Avengers
ca_lessons = {1.2 :'Cadenas 1',1.6 : 'Gráficos de tortuga', 1.13 : 'booleano'}

# Crear un diccionario de alturas de caballeros
heights_of_knights = {'Godfree el Entusiasta' : 1.76,'Otto el Heroico' :1.8,'Magdalena la Conquistadora' : 1.75,'Isabel la Invencible': 1.7}

/*****************************************************************/
# ¡Un diccionario aleatorio! Es habitual que a los diccionarios más complejos se los escriba en líneas nuevas, como este, para que sean más fáciles de leer.
# ¡Por lo general no serán tan confusos!
random_dict = {1: 'manzana', 
        2.7: 'banana', 
        'tres': True, 
        'four': [1, 2, 3], 
        5: 6 * 5, 
        3 * 6: 'fecha'}

#sentencias Print
print(random_dict[2.7])
print(random_dict['four'])
print(random_dict[5])
print(random_dict[3 * 6])

/******************************************************************************/
Modulo 3

# Crear un diccionario de nombres y direcciones de sitios web
websites = {'google': 'http://google.com', 'facebook': 'http://facebook.com', 'twitter': 'http://twitter.com'}

# Sentencias Print:
print(websites['google'])
print("La dirección URL de Twitter es: {}".format(websites['twitter']))

/***************************************************************/
# Crear un diccionario de valores calóricos por cada 100 g de alimentos comunes.
calorie_values = {'mantequilla': 770, 'hojuelas de maíz': 364, 'apio': 6, 'fresas': 26}

# Pedir al usuario que busque un elemento
item = input("Ingresa el nombre del alimento que deseas buscar: ").strip().lower()

# Comprobar si un elemento está en el diccionario
if item in calorie_values:
  print("Sí, el valor calórico de {} es {} calorías por cada 100 g".format(item,calorie_values[item]))
else:
  print("Lo siento, ese elemento no está en el diccionario")
/******************************************************************/

# Crear un diccionario de algunas de las lecciones del nivel 1 de Python de Code Avengers
ca_lessons = {1.2: 'Strings 1', 1.6: 'Gráficos De Tortuga', 1.13: 'Boolean'}

# Pedir al usuario que busque un elemento
title = input("Ingresa el título de la lección que deseas buscar: ").strip().title()

# Comprobar si un elemento está en el diccionario
if title in ca_lessons.values():
  print("Sí, la lección {} está en el nivel 1 del curso de Python".format(title))
else:
  print("Lo siento, esa lección no parece estar en el curso.")
  
/******************************************************************/
# Crear un diccionario de nombres de usuario y puntuaciones de jugadores
player_scores = {'CoolKiwi': 1125, 'Avenger909': 1275, 'InfamousCandyKid': 1050}

# Comprobar si un jugador está en la tabla de posiciones, sin que se produzca un error
player = input("¿Qué nombre de usuario te gustaría buscar? ").strip()

#Buscar la puntuación de un usuario
score = player_scores.get(player)

if not score: #Comprueba si la puntuación es falsa
  print("Lo siento, {} no está en la tabla de posiciones".format(player))
else:
  print("La puntuación de {} es {}".format(player, score))

/**********************************************************************************/
# Crear un diccionario de valores calóricos por cada 100 g de alimentos comunes.
calorie_values = {'mantequilla': 770, 'hojuelas de maíz': 364, 'apio': 6, 'fresas': 26}

# Imprimir todas las claves del diccionario
for food in calorie_values:
  print(food)
  
/**************************************************************************************/
# Crear un diccionario de valores calóricos por cada 100 g de alimentos comunes.
calorie_values = {'mantequilla': 770, 'hojuelas de maíz': 364, 'apio': 6, 'fresas': 26}

# Imprimir todas las claves del diccionario
for food in calorie_values:
  print(food)

# Imprimir todas las claves y valores del diccionario
for food, calories in calorie_values.items():
  print(food,calories)


# Imprimir cada clave y valor en una cadena 
for food, calories in calorie_values.items():
  print("{} tiene {} calorias por cada 100 g".format(food,calories))
  
/***************************************************************************************/
# Diccionario de estados y abreviaturas
us_states = {'alaska':'AK', 'alabama': 'AL', 'arizona': 'AZ'}

# Pedir al usuario que busque un elemento
search = input("Ingresa la abreviatura del estado que quieres buscar: ").strip().upper()

for state, abbreviation in us_states.items():
  if abbreviation == search:
    print("{} es la abreviatura de {} ".format(abbreviation, state))
    break
else:
  print("Lo siento. Esa abreviatura no está en el diccionario.")

/*****************************************************************************************/
# Diccionarios para cada caballero
knight1 = {'name': 'Godfree the Eager', 'height': 1.76, 'weapon': 'Mace'}
knight2 = {'name': 'Otto the Heroic', 'height': 1.8, 'weapon': 'Broadsword'}
knight3 = {'name': 'Magdalin the Conquerer', 'height': 1.75, 'weapon': 'Warhammer'}
knight4 = {'name': 'Isabel the Invincible', 'height': 1.75, 'weapon': 'Lance'}

# Configurar la cadena para imprimir cada uno
knight_string = "Buenas tardes, me llamo {name}, mido {height:.2f} m de alto y mi arma preferida es un(a) {weapon}"

# Usar cada diccionario para imprimir la oración con los valores correctos
print(knight_string.format(**knight1))
print(knight_string.format(**knight2))
print(knight_string.format(**knight3))
print(knight_string.format(**knight4))
/******************************************************************************************/
# Crear un diccionario de detalles de estudiantes
student1 =  {"name": "Sally", "age": "19", "occupation": "student"}

# Agregar detalles nuevos
student1['hometown'] = 'Auckland'
student1['mobile'] = '012 345 6789'
print(student1)
/***************************************************************************************/
# Crear un diccionario de detalles de estudiantes
student1 = {'name':'Sally', 'age':'19', 'occupation':'student', 'hometown':'Auckland', 'mobile':'012 345 6789'}

# Agregar detalles nuevos
student1.update({'height': 1.56,'fav_food': 'nachos','fav_color': 'blue'})
print(student1)

/******************************************************************************************/
# Detalles del estudiante
student1 = {'name':'Sally', 'age':'19', 'occupation':'student', 'hometown':'Auckland', 'mobile':'012 345 6789', 'height':'1.56', 'fav_food':'nachos', 'fav_color':'blue'}

# Cambiar los detalles
student1['age']='20'
student1.update({'occupation': 'developer','fav_food': 'pizza','fav_color': 'lime green'})
print(student1)

/********************************************************************************************/
# Detalles del estudiante
student1 = {'name':'Sally','age':20,'occupation':'developer','hometown':'Auckland','mobile':'012 345 6789','height':'1.56','fav_food':'pizza','fav_color':'lime green'}

# Quitar el móvil con .pop() y almacenar como móvil
mobile = student1.pop('mobile')
print(mobile)
# Usar del para quitar fav_food y la ciudad natal
del student1['fav_food']
del student1['hometown']
# Imprimir el diccionario
print(student1)
/*************************************************************************************************/
# Crear un diccionario de valores calóricos por cada 100 g de alimentos comunes.
calorie_values = {'butter': 770, 'cornflakes': 364, 'celery': 6, 'strawberries': 26}
  
# Crear un diccionario de nombres de usuario y puntuaciones de jugadores
player_scores= {
                  'CoolKiwi': 1125,
                  'Avenger909': 1275, 
                  'InfamousCandyKid': 1050
                }

# Crear un diccionario de valores calóricos por cada 100 g de alimentos comunes.
calorie_values = {'butter': 770, 'cornflakes': 364, 'celery': 6, 'strawberries': 26}
  
# Crear un diccionario de nombres de usuario y puntuaciones de jugadores
player_scores.update({
                  'CoolKiwi': 1125,
                  'Avenger909': 1275, 
                  'InfamousCandyKid': 1050
                })
                
/*************************************************************************************************/
# Crear un diccionario de nombres y direcciones de sitios web
websites = {'google': 'http://google.com', 'facebook': 'http://facebook.com', 'twitter': 'http://twitter.com'}

# Sentencias Print:
print(websites['google'])
print(websites['facebook'])
print("The Twitter URL is: {}".format(websites['twitter']))

# Crear un diccionario de valores calóricos por cada 100g de alimentos comunes.
calorie_values = {'butter': 770, 'cornflakes': 364, 'celery': 6, 'strawberries': 26}

# Pedir al usuario que busque un elemento
item = input("Enter the name of the food item you would like to look up: ").strip().lower()
 
# Comprobar si un elemento está en el diccionario
if item in calorie_values:
  print("Yes the calorie value of {} is {} calories per 100g".format(item, calorie_values[item]))
else:
  print("Sorry, that item is not in the dictionary")

/***********************************************************************************************************/
# Diccionario de estados y abreviaturas
us_states = {'alaska':'AK', 'alabama': 'AL', 'arizona': 'AZ'}

# Imprimir todas las claves del diccionario
for state in us_states:
  print(state)
  
# Imprimir cada clave y valor en una cadena 
for state, abbreviation in us_states.items():
  print("{} is the abbreviation for {}".format(abbreviation, state))
 /*************************************************************************************************************/
 
 #Detalles del caballero
knight = {'name': 'Magdalin the Conquerer', 'weapon': 'Warhammer', 'warcry': 'Ni!', 'speed': 6, 'strength': 8}

knight['warcry'] = "Ekki-ekki-ekki-ptang-zoom-boing!"
knight.update({'speed': 7, 'strength': 9})
print(knight)

# Detalles del estudiante
student1 = {'name':'Sally', 'age':'20', 'occupation':'student', 'hometown':'Auckland', 'mobile':'012 345 6789', 'height':'1.56', 'fav_food':'nachos', 'fav_color':'blue'}

# Cambiar los detalles
student1['age'] = 20
student1.update({'occupation':'developer', 'fav_food': 'pizza', 'fav_color': 'lime green'})
print(student1)

/*********************************************************************************************************/
# Detalles del estudiante
student1 = {'name':'Sally','age':20,'occupation':'developer','hometown':'Auckland','mobile':'012 345 6789','height':'1.56','fav_food':'pizza','fav_color':'lime green'}

# Quitar valores con pop()
developer = student1.pop('occupation')
mobile = student1.pop('mobile')
print(mobile)

# Quitar fav_food y la ciudad natal
del student1['fav_food']
del student1['hometown']

# Imprimir el diccionario
print(student1)

/*****************************************************************************************/
programa diccionarios
*************************************************************************************/
# Diccionario de inglés a maorí
WORD_LIST = {'apple': 'aporo',
'chair': 'turu',
'book': 'pukapuka',
'hello': 'kia ora',
'goodbye': 'ka kite'}

# Función de menú
def menu():
  print(""" Tipo: 
 '1' para ver el menú
 '2' para ver la lista de palabras
 '3' para traducir una palabra
 '4' para dar fin al programa""")
menu()

/*************************************************/
# Diccionario de inglés a maorí
WORD_LIST = {'apple':'aporo','chair':'turu','book':'pukapuka','hello':'kia ora','goodbye':'ka kite'}

# Función de menú
def menu():
  print("Tipo: \n",
        "'1' para ver el menú\n",
        "'2' para ver la lista de palabras\n",
        "'3' para traducir una palabra\n",
        "'4' para dar fin al programa")

# Función para mostrar la lista de palabras
def show_list():
  for word, translation in WORD_LIST.items():
    print("{} = {}".format(word.title(), translation))
show_list()

/****************************************************/
# Diccionario de inglés a maorí
WORD_LIST = {'apple':'aporo','chair':'turu','book':'pukapuka','hello':'kia ora','goodbye':'ka kite'}

# Función de menú
def menu():
    print("Tipo: \n",
          "'1' para ver el menú\n",
          "'2' para ver la lista de palabras\n",
          "'3' para traducir una palabra\n",
          "'4' para dar fin al programa")

# Función para mostrar la lista de palabras
def show_list():
    for word, translation in WORD_LIST.items():
        print("{} = {}".format(word, translation))

# Función de traducción
def translate(word):
  if word in WORD_LIST:
    translation = WORD_LIST[word]
    print("{} en maorí es {}".format(word,translation))
  else:
    print("Lo siento, esa palabra no está en el diccionario")
    
translate('apple')

/********************************************************/
# Diccionario de inglés a maorí
WORD_LIST = {'apple':'aporo','chair':'turu','book':'pukapuka','hello':'kia ora','goodbye':'ka kite'}

# Función de menú
def menu():
  print("Tipo: \n",
        "'1' para ver el menú\n",
        "'2' para ver la lista de palabras\n",
        "'3' para traducir una palabra\n",
        "'4' para dar fin al programa")

# Función para mostrar la lista de palabras
def show_list():
  for word, translation in WORD_LIST.items():
    print("{} = {}".format(word, translation))

        
# Función de traducción
def translate(word):
  if word in WORD_LIST:
    translation = WORD_LIST[word]
    print("{} en maorí es {}".format(word, translation))
  else:
    print("Lo siento, esa palabra no está en el diccionario")

# Programa principal
print("Bienvenido al diccionario de inglés a maorí")
name = input("¿Cómo te llamas?").title()
print("Hola, {}".format(name))

# Imprimir menú
menu()

# Ejecutar el bucle del programa
repeat = True
while repeat == True:
  
    # Pedir información al usuario 
    option = input("¿Qué te gustaría hacer?").strip()
    break

/*******************************************************************/
# Diccionario de inglés a maorí
WORD_LIST = {'apple':'aporo','chair':'turu','book':'pukapuka','hello':'kia ora','goodbye':'ka kite'}

# Función de menú
def menu():
  print("Tipo: \n",
          "'1' para ver el menú\n",
          "'2' para ver la lista de palabras\n",
          "'3' para traducir una palabra\n",
          "'4' para dar fin al programa")

# Función para mostrar la lista de palabras
def show_list():
  for word, translation in WORD_LIST.items():
    print("{} = {}".format(word.title(), translation))

# Función de traducción
def translate(word):
  if word in WORD_LIST:
    translation = WORD_LIST[word]
    print("{} en maorí es {}".format(word.title(), translation))
  else:
    print("Lo siento, esa palabra no está en el diccionario")
        
# Programa principal
print("Bienvenido al diccionario de inglés a maorí")
name = input("¿Cómo te llamas?").title()
print("Hola, {}".format(name))

# Imprimir menú
menu()

# Ejecutar el bucle del programa
repeat = True
while repeat == True:

  # Pedir información al usuario y 
  option = input("¿Qué te gustaría hacer? ").strip()

  # Revisar la entrada y ejecutar la función elegida
  if option == '1':
    menu()
  elif option == '2':
    show_list()
  elif option == '3':
    word = input("¿Qué palabra te gustaría traducir?")
    translate(word)
  elif option == '4':
    print("Adiós, {}. ¡Gracias por usar el diccionario!".format(name))
    repeat = False
  else:
    print("Esa no era una opción")
    
/*******************************************************************/
# Diccionario de inglés a maorí
WORD_LIST = {'apple':'aporo','chair':'turu','book':'pukapuka','hello':'kia ora','goodbye':'ka kite'}
 
# Función de menú
def menu():
  print("Escribe: \n",
          "'1' para ver el menú\n",
          "'2' para ver la lista de palabras\n",
          "'3' para traducir una palabra\n",
          "'4' para dar fin al programa")
 
# Función para mostrar la lista de palabras
def show_list():
  for word, translation in WORD_LIST.items():
    print("{} = {}".format(word.title(), translation))
 
# Función de traducción
def translate(word):
  if word in WORD_LIST:
    translation = WORD_LIST[word]
    print("{} en maorí es {}".format(word.title(), translation))
  else:
    print("Lo siento, esa palabra no está en el diccionario")
        
# Programa principal
print("Bienvenido al diccionario de inglés a maorí")
name = input("¿Cómo te llamas?").title()
print("Hola, {}".format(name))
 
# Imprimir menú
menu()
 
# Ejecutar el bucle del programa
repeat = True
while repeat == True:
 
  # Pedir información al usuario y 
  option = input("¿Qué te gustaría hacer?").strip()
 
  # Revisar la entrada y ejecutar la función elegida
  if option == "1":
    menu()
  elif option == "2":
    show_list()
  elif option == "3":
    word = input("¿Qué palabra te gustaría traducir?").lower()
    translate(word)
  elif option == "4":
    print("Adiós, {}. ¡Gracias por usar el diccionario!".format(name))
    repeat = False
  else:
    print("Esa no era una opción")

/******************************************************************/

# Diccionario de inglés a maorí
WORD_LIST = {'apple':'aporo','chair':'turu','book':'pukapuka','hello':'kia ora','goodbye':'ka kite'}
 
# Función de menú, imprime las funciones que debe elegir el usuario.
def menu():
  """Imprime las instrucciones para que el usuario pueda elegir una opción de modo en el traductor"""
  print("Tipo: \n",
          "'1' para ver el menú\n",
          "'2' para ver la lista de palabras\n",
          "'3' para traducir una palabra\n",
          "'4' para dar fin al programa")
 
# Función para mostrar la lista de palabras, muestra el listado de palabras que existen en el diccionario
def show_list():
  """Recorre con un bucle cada elemento de la lista para que las claves y los valores impriman en un formato facil de leer"""
  for word, translation in WORD_LIST.items():
    print("{} = {}".format(word.title(), translation))
 
# Función de traducción traduce una palabra que recibe a partir del usuario
def translate(word):
  """Toma la palabra ingresada por el usuario, verifica si la palabra esta en el diccionario e imprime mensaje de error"""
  if word in WORD_LIST:
    translation = WORD_LIST[word]
    print("{} en maorí es {}".format(word.title(), translation))
  else:
    print("Lo siento, esa palabra no está en el diccionario")
        
# Programa principal
print("Bienvenido al diccionario de inglés a maorí")
name = input("¿Cómo te llamas?").title()
print("Hola, {}".format(name))
 
# Imprimir menú
menu()
 
# Ejecutar el bucle del programa
repeat = True
while repeat == True:
 
  # Pedir información al usuario
  option = input("¿Qué te gustaría hacer? ").strip()
 
  # Revisar la entrada y ejecutar la función elegida
  if option == "1":
    print(help(menu))
    menu()
  elif option == "2":
    print(help(show_list))
    show_list()
  elif option == "3":
    print(help(translate))
    # Pregúntale al usuario qué palabra quiere traducir, ejecuta la función de traducción que imprime la traducción o el mensaje de error.
    word = input("¿Qué palabra te gustaría traducir? ").strip().lower()
    translate(word)
    
  elif option == "4":
    # Si el usuario elige salir, despídete y detén el bucle.
    print("Adiós, {}. ¡Gracias por usar el diccionario!".format(name))
    repeat = False
  else:
    # Si el usuario elige una opción no válida, indícale el error antes de que la pregunta se repita
    print("Esa no era una opción")
    
/**********************************************************************/
tortuga con diccionarios.

*******************************************************************/
import turtle

# Crear 4 diccionarios con diferentes especificaciones de tortugas para usar como valores en el diccionario de tortugas
turtle1 = {'color': 'red', 'pensize': 1, 'fillcolor': 'yellow', 'squaresize': 50, 'x': 50, 'y': 100}
turtle2 = {'color': 'blue', 'pensize': 5, 'fillcolor': 'red', 'squaresize': 100, 'x': 300, 'y': 150}
turtle3 = {'color': 'green', 'pensize': 7, 'fillcolor': 'blue', 'squaresize': 150, 'x': 50, 'y': 400}
turtle4 = {'color': 'yellow', 'pensize': 10, 'fillcolor': 'green', 'squaresize': 200, 'x': 250, 'y': 450}

/************************************************************************/
import turtle

# Crear 4 diccionarios con diferentes especificaciones de tortugas para usar como valores en el diccionario de tortugas
turtle1 = {'color': 'red', 'pensize': 1, 'fillcolor': 'yellow', 'squaresize': 50, 'x': 50, 'y': 100}
turtle2 = {'color': 'blue', 'pensize': 5, 'fillcolor': 'red', 'squaresize': 100, 'x': 300, 'y': 150}
turtle3 = {'color': 'green', 'pensize': 7, 'fillcolor': 'blue', 'squaresize': 150, 'x': 50, 'y': 400}
turtle4 = {'color': 'yellow', 'pensize': 10, 'fillcolor': 'green', 'squaresize': 200, 'x': 250, 'y': 450}

# Crear 4 objetos de tortuga para usar como claves en el diccionario de tortugas
todd = turtle.Turtle()
tina = turtle.Turtle()
tyrell = turtle.Turtle()
talisha = turtle.Turtle()




# Asociar cada objeto de tortuga con un conjunto de especificaciones y crear así el diccionario de tortugas
turtles = {todd : turtle1, tina: turtle2, tyrell: turtle3, talisha : turtle4}

/********************************************************************************/

import turtle

# Crear 4 diccionarios con diferentes especificaciones de tortugas para usar como valores en el diccionario de tortugas
turtle1 = {'color': 'red', 'pensize': 1, 'fillcolor': 'yellow', 'squaresize': 50, 'x': 50, 'y': 100}
turtle2 = {'color': 'blue', 'pensize': 5, 'fillcolor': 'red', 'squaresize': 100, 'x': 300, 'y': 150}
turtle3 = {'color': 'green', 'pensize': 7, 'fillcolor': 'blue', 'squaresize': 150, 'x': 50, 'y': 400}
turtle4 = {'color': 'yellow', 'pensize': 10, 'fillcolor': 'green', 'squaresize': 200, 'x': 250, 'y': 450}

# Crear 4 objetos de tortuga para usar como claves en el diccionario de tortugas
todd = turtle.Turtle()
tina = turtle.Turtle()
tyrell = turtle.Turtle()
talisha = turtle.Turtle()

# Asociar cada objeto de tortuga con un conjunto de especificaciones y crear así el diccionario de tortugas
turtles = {todd: turtle1, tina: turtle2, tyrell: turtle3, talisha: turtle4}

# La función creadora de tortugas asigna a la tortuga ingresada el color, el tamaño, el relleno, etc. correctos a partir de las especificaciones ingresadas
def turtle_maker(turtle,specs):
  turtle.color(specs['color'])
  turtle.pensize(specs['pensize'])
  turtle.fillcolor(specs['fillcolor'])
  turtle.penup()

/***************************************************************************/
import turtle

# Crear 4 diccionarios con diferentes especificaciones de tortugas para usar como valores en el diccionario de tortugas
turtle1 = {'color': 'red', 'pensize': 1, 'fillcolor': 'yellow', 'squaresize': 50, 'x': 50, 'y': 100}
turtle2 = {'color': 'blue', 'pensize': 5, 'fillcolor': 'red', 'squaresize': 100, 'x': 300, 'y': 150}
turtle3 = {'color': 'green', 'pensize': 7, 'fillcolor': 'blue', 'squaresize': 150, 'x': 50, 'y': 400}
turtle4 = {'color': 'yellow', 'pensize': 10, 'fillcolor': 'green', 'squaresize': 200, 'x': 250, 'y': 450}

# Crear 4 objetos de tortuga para usar como claves en el diccionario de tortugas
todd = turtle.Turtle()
tina = turtle.Turtle()
tyrell = turtle.Turtle()
talisha = turtle.Turtle()

# Asociar cada objeto de tortuga con un conjunto de especificaciones y crear así el diccionario de tortugas
turtles = {todd: turtle1, tina: turtle2, tyrell: turtle3, talisha: turtle4}

# La función creadora de tortugas asigna a la tortuga ingresada el color, el tamaño, el relleno, etc. correctos a partir de las especificaciones ingresadas
def turtle_maker(turtle, specs):
  turtle.color(specs['color'])
  turtle.pensize(specs['pensize'])
  turtle.fillcolor(specs['fillcolor'])
  turtle.penup()

# La función de dibujar un cuadrado envía a la tortuga a sus coordenadas y luego dibuja y rellena un cuadrado del tamaño correcto
def draw_square(turtle, size, x, y):
  turtle.goto(x, y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(size)
    turtle.left(90)
  turtle.end_fill()
  
/******************************************************************/
import turtle

# Crear 4 diccionarios con diferentes especificaciones de tortugas para usar como valores en el diccionario de tortugas
turtle1 = {'color': 'red', 'pensize': 1, 'fillcolor': 'yellow', 'squaresize': 50, 'x': 50, 'y': 100}
turtle2 = {'color': 'blue', 'pensize': 5, 'fillcolor': 'red', 'squaresize': 100, 'x': 300, 'y': 150}
turtle3 = {'color': 'green', 'pensize': 7, 'fillcolor': 'blue', 'squaresize': 150, 'x': 50, 'y': 400}
turtle4 = {'color': 'yellow', 'pensize': 10, 'fillcolor': 'green', 'squaresize': 200, 'x': 250, 'y': 450}

# Crear 4 objetos de tortuga para usar como claves en el diccionario de tortugas
todd = turtle.Turtle()
tina = turtle.Turtle()
tyrell = turtle.Turtle()
talisha = turtle.Turtle()

# Asociar cada objeto de tortuga con un conjunto de especificaciones y crear así el diccionario de tortugas
turtles = {todd: turtle1, tina: turtle2, tyrell: turtle3, talisha: turtle4}

# La función creadora de tortugas asigna a la tortuga ingresada el color, el tamaño, el relleno, etc. correctos a partir de las especificaciones ingresadas
def turtle_maker(turtle, specs):
  turtle.color(specs['color'])
  turtle.pensize(specs['pensize'])
  turtle.fillcolor(specs['fillcolor'])
  turtle.penup()

# La función de dibujar un cuadrado envía a la tortuga a sus coordenadas y luego dibuja y rellena un cuadrado del tamaño correcto
def draw_square(turtle, size, x, y):
  turtle.goto(x, y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(size)
    turtle.left(90)
  turtle.end_fill()

# El bucle del programa principal recorre con un bucle las tortugas del diccionario, crea una tortuga y luego dibuja su cuadrado
for turtle, specs in turtles.items():
  turtle_maker(turtle, specs)
  draw_square(turtle, specs['squaresize'], specs['x'], specs['y'])

/**************************************************************/
Repaso diccionarios
***************************************************************/
# Crear el diccionario
ages = {'Claire': 29,'Monty': 65, 'Josh': 30}

# Imprimir algunos valores
print(ages['Claire'])
print(ages['Monty'])
print(ages['Josh'])
# Actualizar la edad de Claire y Josh porque cumplieron años
ages.update({'Claire': 30, 'Josh': 31})

# Agregar tu edad
ages['Jhon'] = 39

# Imprimir todo el diccionario (sin formato)
print(ages)

/*****************************************************************/
# Diccionario de nombres y edades
ages = {'Claire': 29, 'Monty': 65, 'Josh': 30}

# Comprobar si existe una clave e imprimir un valor.
if 'Josh' in ages:
  print(ages['Josh'])
else:
  print('¡No!')

# Comprobar si existe un valor.
if 65 in ages.values():
  print("Sí")
else:
  print("¡No!")
# Usar un bucle para comprobar si existe un valor, y si existe, imprimir la clave.

/***********************************************************************/
# Diccionario de nombres y edades
ages = {'Claire': 29, 'Monty': 65, 'Josh': 30}

# Recorrer con un bucle todas las claves e imprimirlas
for name in ages:
  print(name)


# Recorrer con un bucle todos los valores e imprimirlos
for age in ages.values():
  print(age)



# Recorrer con un bucle todas las claves y valores e imprimir cada par en una oración con formato.
for name, age in ages.items():
  print("{} tiene {} años".format(name, age))
  
  
/****************************************************************/
POO inicio
*****************************************************************/
# Print out the menu so the user knows what options there are and get user's choice
def menu():

    mode = input("""Choose a mode by entering the number:
    1: Add a task
    2: View list
    3: Exit
    """).strip()

    return mode


# Function that allows user to add a task to their to do list
def add_tasks():
    while True:
        new_task = input("Enter the task to add or type 'end' to return to menu: ").strip().lower()
        if new_task == "end":
            break
        else:
            # If the user hasn't entered end, append their new task to the to do list
            todo_list.append(new_task)


# Function that shows current tasks in the To Do List
def view_list():
  for task in todo_list:
    print("- {}".format(task))
    
# Create an empty list to store the tasks
todo_list = []

# Run the main program in a loop.
while True:
    chosen_option = menu()

    if chosen_option == "1":
        #Run the add_tasks function if the user chooses 1
        add_tasks()   
    elif chosen_option == "2":
        print("Here is your To Do List:")
        view_list()
    elif chosen_option == "3":
        break
    else:
        print("That wasn't an option, please try again")

print("Goodbye!")

/****************************************************/
tkinter
/**********************************
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

# ------------------- FUNCTION CODE ---------------------#

# Greet me function, run when button is clicked and says greeting with name e.g. Hello Bob!
def greet_me():
    greeting_message.set("{} {}".format(greeting.get(), name.get()))


# -------------------- USER INTERFACE CODE --------------#
# Create the main window with title
root = Tk()
root.title("My Python GUI Demo")

# Create an outer label frame - puts a labeled border around its child widgets, can help to organise UI
container = ttk.LabelFrame(root, text="Greeting Program")
container.grid(column=0, row=0)

# ---------------------- GREETING CHOICES --------------#
# Adding a combo box - dropdown with text entry, can disable free text entry (read only)
greeting_box_label = ttk.Label(container, text="Choose/enter a greeting:").grid(column=0, row=0)
greeting = StringVar()

greeting_box = ttk.Combobox(container, textvariable=greeting)
greeting_box['values'] = ["Hello", "Goodbye", "Good Morning", "Good Afternoon", "Good Night"]
greeting_box.grid(column=0, row=1)
greeting_box.current(0)

# -----------------------NAME ENTRY --------------------#
#Adding a Label - Text labels that can go anywhere
name_label = ttk.Label(container, text="Enter a name: ")
name_label.grid(column=1, row=0)

#Adding a textbox entry widget - just a basic 1 line input you can set the width of
#Can assign it a textvariable which it will automatically change to if that variable is changed
name = StringVar()
name_entered = ttk.Entry(container, textvariable=name)
name_entered.grid(column=1, row=1)
name_entered.focus()

# ------------------- GREETING OUTPUT AND BUTTON --------#
# Label to put text into
greeting_message = StringVar()
greeting_label = ttk.Label(container, textvariable=greeting_message).grid(column=2, row=0)

#Adding a Button - just a button, with text, can run a function when clicked
action_button = ttk.Button(container, text="Greet me", command=greet_me)
action_button.grid(column=2, row=1)

# Adding checkboxes in different states
use_name = IntVar()
check_box = Checkbutton(container, text="Use my name", variable=use_name, state='disabled')
check_box.select()
check_box.grid(column=0, row=2, sticky=W)

# ------------------- STYLES/PADDING --------------------#
container.grid_configure(padx=10, pady=10)

for child in container.winfo_children():
    child.grid_configure(padx=10, pady=10, sticky=W)

# Up to page 41 with tabbed widgets up next
root.mainloop()


  
    
    

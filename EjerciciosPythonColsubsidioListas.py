#Enumerar los favoritos de la computadora
favorites = ['azul', 9, 'pizza', 3.14159]

#Sentencia Print
print(favorites[0].upper())

#Preguntar al usuario cuál es su comida favorita, comprobar si es la misma que la de la computadora
food = input("¿Cuál es tu comida favorita?")
food = food.strip().lower()

if food == favorites[2]:
  #Se usa una función para asegurarse de que haya una letra mayúscula al inicio de la sentencia print
  print("¡{} también es mi comida favorita!".format(favorites[2].capitalize()))
  
else:
  print("{} está bien, pero prefiero {}.".format(food.capitalize(), favorites[2]))
  
"""#Una lista de nombres"""
names =  ["charlotte", "olivia", "isla", "emily", "sophie", "oliver", "jack", "james", "mason", "liam"]

#Preguntar el nombre al usuario y ver si es 
name = input("¿Cómo te llamas?").strip().lower()

if name in names:
  print("¿Adivina qué? Tu nombre fue uno de los 10 nombres de bebé más elegidos en 2014.  ¡Bien por ti!")
else:
  print("{} es un buen nombre, pero no estuvo entre los 10 más elegidos en 2014.".format(name.capitalize()))
  
#Una lista de los colores primarios de luz, que se usan en los píxeles de tu pantalla
primary_colors = ["amarillo","azul","rojo"]

#Pedir al usuario que elija un color
color = input("Por favor ingresa un color").strip().lower()

#Dile si es uno de los colores primarios de luz
if color in primary_colors:
  print("{} es un color primario de luz".format(color))
else:
  print("{} no es un color primario de luz".format(color))
  
"""------------------------------------------------------"""
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]
students_absent = ["iliana", "olympia", "juan", "kelsey"]

print("Hoy hay {} estudiantes presentes y {} estudiantes ausentes".format(len(students_present), len(students_absent)))

student = input("Ingresa un nombre para averiguar si el estudiante está presente o ausente: ").strip().lower()

if student in students_present:
  print("{} está presente hoy.".format(student.title()))
elif student in students_absent:
  print("{} está ausente hoy.".format(student.title()))
else:
  print("Lo lamento, no existe ningún estudiante que se llame {}.".format(student.title()))
  
"""-----------------Ejercicio Listas colsubsidio--------------------------"""
# Los 5 videojuegos más vendidos de esta semana
top_games = ["Battlefield: Hardline", "Final Fantasy: Type-0", "Mario Party 10", "Resident Evil: Revelations 2", "Grand Theft Auto V"]
print(top_games)

# Cambiar el quinto lugar
top_games[4] = "Assassin's Creed: Unity"

# Intercambiar el primer y el segundo lugar
top_games[1],top_games[0] = top_games[0],top_games[1]
print(top_games)

"""----------------------------------------------------------------------------"""
#Caballeros de ¡Ni! actuales
order_knights = ["Stevyn the Kind", "Selle the Swift","Nigs the Fierce", "Jacomynus the Honorable", "Janyn the Warrior", "Mauger the Dragon", "Viliame the Stubborn", "Dreues the Unbreakable"]
print(order_knights)

#Agregar al miembro nuevo e imprimir la lista
order_knights.append("Raymond the Brute")
print(order_knights)

#Lista de armas disponibles
weapons_available = ["Dagger", "Lance", "Flail", "Medieval Sword", "Broadsword", "Falchion sword", "Greatsword", "Longsword"]
print(weapons_available)

#Agregar 'mace' a la lista e imprimir
weapons_available.append("mace")
print(weapons_available)

"""--------------------------------------------------------------------------------"""
#Lista incompleta de los meses del año
months = ["Jan", "Mar", "Apr", "May", "Jul", "Aug", "Sep", "Nov"]

#Agregar los meses faltantes en orden (abreviaturas de 3 letras)
months.insert(1,"Feb")
months.insert(5,"Jun")
months.insert(9,"Oct")
months.append("Dic")

#Imprimir la longitud de la lista
print(len(months))

"""-----------------------------------------------------"""

Al igual que agregar valores, hay dos maneras de quitar valores de una lista:

my_list = ["bolígrafo", "lápiz", "borrador"]
#Pop quita de una posición según el índice 
my_list.pop(1) #Quita 'lápiz' 
#Remove() usa el valor en sí, quita el primer 
  # valor que coincide
my_list.remove("borrador")#quita 'borrador'
En la batalla más reciente, los Caballeros que dicen ¡Ni! perdieron todos sus puñales y, lamentablemente, a Selle the Swift, quien no era tan veloz como su nombre lo sugería.

/***************************************************************/
#Listas de estudiantes
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocío"]
students_absent = ["iliana", "olympia", "juan", "kelsey"]

#Imprimir los estudiantes presentes:
for student_present in students_present:
  print(student_present)


#Imprimir la cantidad de estudiantes presentes
print("Total de estudiantes presentes: {}.".format(len(students_present)))

#Imprimir los estudiantes ausentes
for student_absent in students_absent:
  print(student_absent)



#Imprimir la cantidad de estudiantes ausentes
print("Total de estudiantes ausentes: {}.".format(len(students_absent)))

/**********************************************************************************/
#Join in python

#Lista de armas disponibles
weapons_available = ["Puñal", "Lanza", "Mangual", "Espada medieval", "Sable", "Bracamarte", "Espada magna", "Espada de mano y media"]

#Imprimir la lista con comas de separación
print(", ".join(weapons_available))

#Imprimir la lista con espacios de separación
print(" ".join(weapons_available))

#Imprimir la lista con tildes ~ de separación
print("~".join(weapons_available))

#Imprimir la lista con rosas @-->-- de separación
print("@-->--".join(weapons_available))

/**********************************************************************/
#Indice de un elemento en una lista.
#Lista de armas disponibles
weapons_available = ["Puñal", "Lanza", "Mangual", "Espada medieval", "Sable", "Bracamarte", "Espada magna", "Espada de mano y media"]

#Imprimir la posición del Sable
print(weapons_available.index("Sable"))
#Buscar la posición del Mangual y almacenarla como índice
index = weapons_available.index("Mangual")

#Imprimir el índice del Mangual en la oración.
print("El Mangual está en la posición {}".format(index))

/*************************************************************************/
"""Contar cuántas veces aparece un valor en una lista
Sabemos cómo determinar la longitud de una lista completa, pero también es útil poder averiguar cuántas veces aparece un valor en una lista. Esto es útil por varias razones:

Para averiguar si un valor ya está en una lista, por ejemplo, antes de volver a agregarlo.
Para averiguar si un valor aparece más de una vez, por ejemplo, para quitar duplicados.
Para simplemente averiguar cuántas veces aparece ese valor en la lista.
Para hacerlo, usamos la función count(). Ejecuta el código de ejemplo para ver cómo funciona.

Veamos un código en el que la entrada del usuario se almacena en una lista."""

favorite_foods = []

#Iniciar un bucle para pedir al usuario que ingrese sus comidas favoritas
repeat = True
while repeat == True:
  food = input("Ingresa una comida favorita o 'listo' para finalizar una entrada: ").strip().lower()
  
  #Comprobar si el usuario ingresó 'listo' para poder detener el bucle
  if food == 'listo':
    repeat = False
  else:
    #Comprobar si la comida ya está en la lista
    count = favorite_foods.count(food)
    
    #Si ya lo está, mostrar al usuario un mensaje de error, de lo contrario, agregar la comida y mostrar un mensaje de proceso completado con éxito
    if count > 0:
      print("Lo sentimos, {} ya está en la lista.".format(food))
    else:
      favorite_foods.append(food)
      print("¡{} se ha agregado a la lista!".format(food))

#Cuando el usuario haya terminado, imprimirle la lista
print("Tus comidas favoritas son: ")

for food in favorite_foods:
  print(food.title()) #Agregar una letra mayúscula
  
/***********************************************************************************/
Ordenar listas
En esta lección veremos otras funciones que te permitirán ordenar, ordenar al azar y elegir valores al azar con listas.

La primera función que veremos es sort(). ¡Seguro que puedes adivinar qué hace! Hay ciertas cosas que debes recordar del nivel 1:

Las mayúsculas van antes de las minúsculas.
No puedes ordenar una lista que tenga tanto cadenas como enteros, a menos que conviertas los números en cadenas (para eso tienes que ponerlos entre comillas "").
Observa que la función sort() realmente cambia la lista al orden nuevo, por lo que no puedes volver a tener el orden inicial después de usarla.
**************************************************************************************/
#Listas de estudiantes
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocío"]
students_absent = ["iliana", "olympia", "juan", "kelsey"]

#Ordenar la lista de estudiantes presentes e imprimir
print("Estudiantes presentes: ")

students_present.sort()

for student in students_present:
  print(student.title())
  
#Ordenar la lista de estudiantes ausentes e imprimir
print("Estudiantes ausentes: ")
students_absent.sort()
for student in students_absent:
  print(student.title())
  
  /*****************************************************************************************
  Obtener y ordenar una lista de compras
Intentemos usar sort() en un programa algo más grande donde podría ser más útil.

El código que está en el editor usa un bucle para preguntar al usuario por todos los artículos en su lista del supermercado. Cuando el usuario escribe listo, imprimimos su lista de artículos en orden alfabético.

Vamos a usar el código que vimos en la última lección para asegurarnos de que no haya duplicados en la lista.
******************************************************************************************************/
#Crear una grocery_list vacía
grocery_list = []

#Iniciar un bucle para pedir al usuario que ingrese su lista del supermercado
repeat = True
while repeat == True:
  item = input("Ingresa un artículo o 'listo' para finalizar las entradas: ").strip().lower()
  
  #Comprobar si el usuario ingresó listo para poder detener el bucle
  if item == "listo":
    repeat = False
  else:
    #Comprobar si el artículo ya está en la lista
    count = grocery_list.count(item)
    
    #Si ya está, mostrar al usuario un mensaje de error; si no, agregar el artículo y mostrar un mensaje de proceso completado con éxito
    if count > 0:
      print("Lo sentimos, {} ya está en la lista.".format(item))
    else:
      grocery_list.append(item)
      print("¡{} se ha agregado a la lista!".format(item))

#Cuando el usuario esté listo, ordena la lista y luego imprímesela
print("Tu lista del supermercado es: ")
grocery_list.sort()

for item in grocery_list:
  print(item.title()) #Agregar una letra mayúscula
/*****************************************************************************************************
Mezclar una baraja
En el curso de nivel 1, aprendimos sobre usar el random módulo para generar números al azar. Podemos usar otras funciones que vienen con el módulo aleatorio para trabajar con listas.

Demos un vistazo a shuffle(), y recordemos que debemos importar el módulo aleatorio si queremos usarlo:

import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
************************************************************************************************************/
#Importar el módulo aleatorio
import random

#Una lista de cartas
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Mezclar las cartas e imprimir
random.shuffle(cards)
print(cards)


#Usar un bucle para imprimir las primeras 3 cartas
for i in range(3):
  print(cards[i])
  
 /******************************************************************************************************
 Usar shuffle() para elegir un elemento de una lista al azar.
Con el código que hemos aprendido, hay dos maneras posibles de elegir un elemento al azar de una lista:

Elige un número al azar (i) y luego pon el elemento en esa posición, por ejemplo, my_list[i]
Ordena la lista al azar y obtén el primer elemento, por ejemplo, my_list[0].
Vamos a ver dos formas de crear un programa simple de Bola 8 Mágica.
******************************************************************************************************/
import random

#Crear una lista de respuestas
responses = ["Sí", "No", "Talvez", "Pronóstico dudoso", "Es imposible saberlo", "Inténtalo de nuevo más tarde","es posible","para nada"]

#Preguntar al usuario su nombre y almacenarlo; darle la bienvenida
name = input("¿Cómo te llamas?").title()
print("Hola, {}. Esta Bola 8 Mágica puede responder todas las preguntas que ansías saber.".format(name))

#Usar un bucle para permitir que el usuario haga las preguntas
repeat = True
while repeat == True:
  question = input("Haz una pregunta para responder con sí o no, o escribe 'listo' para salir:").strip().lower()
  
  if question == "listo":
    print("Los mejores deseos para el futuro, {}. ¡Adiós!".format(name))
    repeat = False
  else:
    random.shuffle(responses)
    print(responses[0])
 /****************************************************************************************************
 Reestructurar código para elegir un elemento al azar por medio de números al azar.
Ahora probemos de nuevo ese mismo código, usando un número al azar para obtener la respuesta en lugar de mezclar la lista al azar.

Usa la referencia si necesitas un recordatorio sobre cómo obtener números al azar.

*********************************************************************************************************/

import random

#Crear una lista de respuestas
responses = ["Sí", "No", "Talvez", "Pronóstico dudoso", "Es imposible saberlo", "Inténtalo de nuevo más tarde", "Hay posibilidad", "Sin duda"]

#Preguntar al usuario su nombre y almacenarlo; darle la bienvenida
name = input("¿Cómo te llamas?").title()
print("Hola, {}. Esta Bola 8 Mágica puede responder todas las preguntas que ansías saber.".format(name))

#Usar un bucle para permitir que el usuario haga las preguntas
repeat = True
while repeat == True:
  question = input("Haz una pregunta para responder con sí o no, o escribe 'listo' para salir:").strip().lower()
  
  if question == "listo":
    print("Los mejores deseos para el futuro, {}. ¡Adiós!".format(name))
    repeat = False
  else:
    i = random.randrange(len(responses))
    print(responses[i])
/************************************************************************************************************
Hallar un subconjunto de una lista
Si tenemos una lista, podemos obtener una parte de esa lista para usarla. En esta lección verás diferentes maneras de obtener subconjuntos de listas, que se conocen como segmentos.

La sintaxis de los segmentos es: my_list[start:stop], donde start y stop son ambos enteros. Al igual que en la función range(), el valor stop no se incluye, por lo que la lista terminará con el valor anterior a él
*******************************************************************************************************/
import random

#Una lista de estudiantes
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocío"]

#Tenemos que elegir 3 estudiantes de la lista
print(students_present[0:3])

#Una lista de cartas
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Imprimir las primeras 5 cartas
print(cards[0:5])

#Mezclar las cartas
random.shuffle(cards)

#Imprimir de nuevo las primeras 5 cartas
print(cards[0:5])
/*****************************************************************************************************
Obtener un segmento del medio de la lista
Nuestra notación de segmento se así: my_list[a:b]

Si a es 0, obtendremos los primeros b elementos, comenzando desde el principio de la lista, por ejemplo, si b es 6, obtendremos los primeros 6 elementos (my_list[0:6]).

Si queremos tomar un segmento del medio de la lista, podemos usar otro número para a. El primer valor debe ser el índice del primer elemento que queremos.
***********************************************************************************************************/
#Una lista de estudiantes
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocío"]

#Tenemos que elegir 3 estudiantes de la lista y luego los segundos 3
print(students_present[0:3])
print(students_present[3:6])


#Una lista de cartas
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Imprimir las primeras 5 cartas y luego las segundas 5 cartas
print(cards[0:5])
print(cards[5:10])


/********************************************************************************************************
Obtener el segmento final de la lista
********************************************************************************************************/
#Una lista de estudiantes
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocío"]

#Tenemos que elegir 3 estudiantes de la lista
print(students_present[0:3])
print(students_present[3:6])
print(students_present[6:])


#Una lista de cartas
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Imprimir las segundas 5 cartas
print(cards[0:5])
print(cards[5:10])
print(cards[10:])

/*********************************************************************
Obtener el último valor de una lista.
Si quisiéramos encontrar el último valor de la lista, podríamos usar una combinación de habilidades, como usar len() para hallar su longitud, y así sucesivamente… PERO eso implica muchos pasos confusos; afortunadamente, Python tiene una manera fácil de hacerlo.

El último valor de cualquier lista también tiene un índice de -1. Entonces:

my_list[-1] obtiene el último valor de la lista. ¡Fácil!
******************************************************************/
#Una lista de estudiantes
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocío"]

#Tenemos que elegir 3 estudiantes de la lista
print(students_present[0:3])
print(students_present[3:6])
print(students_present[6:])
print(students_present[-1])

#Una lista de cartas
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Imprimir las segundas 5 cartas
print(cards[0:5])
print(cards[5:10])
print(cards[10:])
print(cards[-1])

/*****************************************************************
Cacería de errores n.º 1
Cuando trabajamos con listas, pueden producirse muchos errores comunes, ¡y puede ser un poco como buscar una aguja en un pajar!

Esta lección te ayudará a familiarizarte con los errores más comunes, al mismo tiempo que creas un programa básico tipo cuestionario.

¡Vayamos de cacería! Primero, a crear listas.
*******************
#Preguntas y respuestas de un cuestionario
questions = ["¿Cuántos bits tiene un byte?",
            "¿Verdadero o falso? Un cuarteto es medio byte.",
            "¿En qué año se fundó Google?",
            "¿Cuántos ceros hay en un gúgol?",
            "¿Cuántos bytes tiene un kilobyte?"]

answers = ["8", "verdadero", "1998", "100", "1024"]

#Preguntarle el nombre al usuario y darle la bienvenida al cuestionario
name = input("¿Cómo te llamas?")
print("¡Bienvenido al cuestionario, {}! Hay 5 preguntas.".format(name))

******************************************************
#Preguntas y respuestas de un cuestionario. Observa que estos elementos de lista más largos se escriben cada uno en una línea para que sean más fáciles de leer.
questions = ["¿Cuántos bits tiene un byte?",
            "¿Verdadero o falso? Un cuarteto es medio byte.",
            "¿En qué año se fundó Google?",
            "¿Cuántos ceros hay en un gúgol?",
            "¿Cuántos bytes tiene un kilobyte?"]

answers = ["8", "verdadero", "1998", "100", "1024"]

#Preguntarle el nombre al usuario y darle la bienvenida al cuestionario
name = input("¿Cómo te llamas?")
print("¡Bienvenido al cuestionario, {}! Hay 5 preguntas.".format(name))

#Hacer la primera pregunta y obtener la respuesta del usuario a partir de la entrada
guess = input(questions[0]).strip().lower()

if guess == answers[0]:
  print("¡Correcto!")
else:
  print("¡Incorrecto! La respuesta correcta era {}.".format(answers[0]))
******************************************************************************
#Este código le muestra al usuario una lista de juegos clásicos y le pide que elija su favorito. Este valor pasa a la parte superior de la lista y luego el usuario puede agregar otro juego a la lista.

#Crear una lista de algunos de los juegos clásicos más conocidos
top_games = ["pacman", "tetris", "space invaders", "sonic the hedgehog", "super mario brothers", "street fighter", "pong", "donkey kong", "paperboy"]

#Imprimir la lista de juegos
print("Esta es una lista de algunos de los juegos clásicos más conocidos: ", top_games)

#Preguntar al usuario cuál cree que es el mejor juego, y pasarlo a la primera posición
choice = input("¿Cuál crees que es el mejor juego? Escribe el nombre sin errores: ").strip().lower()

#Quitar el juego de su posición actual
top_games.remove(choice)

#Agregarlo al inicio de la lista
top_games.insert(0, choice)

#Preguntar al usuario si le gustaría agregar algún otro juego a la lista
add_more = input("¿Te gustaría agregar otro juego que creas que es genial? S/N: ").strip().lower()

if add_more in ["y", "sí", "sip", "claro"]:
  new_game = input("Escribe el título del juego: ").strip().lower()
  
  if not new_game in top_games:
    top_games.append(new_game)
  else:
    print("¡Ese juego ya está en la lista!")
    
else:
  print("Aceptar")
  
#Imprimir la lista nueva
print("Esta es la lista nueva: ", top_games)

/***********************************************************************************************
#Esta vez, nuestro código permite que el usuario especifique cuántos juegos famosos al azar le gustaría elegir de la lista, ordena la lista al azar y luego elige esa cantidad de juegos e imprime la lista en orden alfabético.

import random

#Crear una lista de algunos de los juegos clásicos más conocidos
top_games = ["pacman", "tetris", "space invaders", "sonic the hedgehog", "super mario brothers", "street fighter", "pong", "donkey kong", "paperboy"]

#Imprimir la lista de juegos, esta vez usando un bucle para mejorar el formato
print("Esta es una lista de algunos de los juegos clásicos más conocidos: ")

for game in top_games:
  print(game)
  
#Preguntar al usuario cuántos juegos quiere elegir
num_games = int(input("¿Cuántos juegos te gustaría elegir al azar?"))

#Ordenar la lista al azar
random.shuffle(top_games)

#Obtener los primeros "n" juegos, según el número elegido por el usuario
chosen_games = top_games[0:num_games]

#Ordenar alfabéticamente los juegos elegidos
chosen_games.sort()

#Imprimir la lista final
print("\nTu lista:")
for game in chosen_games:
  print(game)
  
  
******************************************************************************
#Usar la función list() para crear una lista del abecedario
alpha_string = "abcdefghijklmnopqrstuvwxyz"
alpha_list = list(alpha_string)

#Imprimir las primeras 3 letras en líneas nuevas
for letter in alpha_list[0:3]:
  print(letter)
  
#Imprimir l, m, n, o y p
print(alpha_list[11:16])

#Imprimir las últimas 3 letras
print(alpha_list[23:])

#Imprimir la últimas letra
print(alpha_list[-1])

/**********************************************************
Crear listas bidimensionales
Una lista puede contener cualquier tipo de datos, como cadenas, enteros, números de punto flotante y valores booleanos.

¡Una lista también puede contener listas! Esto convierte a la lista en bidimensional. Para crear una lista bidimensional, simplemente pones una lista, dentro de una lista, así:

a_2d_list = [[1, 2], [3, 4], [5, 6]]
El índice del número 3 en este ejemplo es [1][0]. Para acceder al valor, escribirías: a_2d_list[1][0] .

Esto es porque está en la segunda++++ lista (1 contando desde 0) y porque es el primer++++ elemento de esa lista (0).
************************************************************************/
#Crear una lista de opuestos
opposites = [["sí", "no"], ["caliente", "frío"], ["bajo", "alto"]]

#Imprimir "sí"
print(opposites[0][0])

#Imprimir "bajo"
print(opposites[2][0])

#Imprimir "frío"
print(opposites[1][1])

#Crear una lista bidimensional de los números 10, 20, 30, 40, 50, 60
numbers = [[10, 20, 30],[40, 50, 60]]


#Imprimir 30
print(numbers[0][2])

#Imprimir 40
print(numbers[1][0])

/*****************************************************************************

Cambiar valores en listas bidimensionales
Ahora que sabemos cómo acceder a los valores de una lista bidimensional, también podemos cambiar valores en la lista.

Esto funciona de la misma manera que cambiar valores en una lista unidimensional, solo debemos usar los dos índices al igual que hacemos cuando accedemos a los valores:

opposites = [["sí", "no"], ["caliente", "frío"], ["bajo", "alto"], ["dulce", "agrio"], ["alegre", "triste"]]
#Cambiar "alto" a "largo"
opposites[2][1] = "largo"
Puedes ejecutarlo en el editor de código.
*/***************************************************************************
opposites = [["sí", "no"], ["caliente", "frío"], ["bajo", "alto"], ["dulce", "agrio"], ["triste", "alegre"]]

#Cambiar "alto" a "largo"
opposites[2][1] = "largo"
print(opposites)

#Cambiar "agrio" a "salado"
opposites[3][1] = "salado"
print(opposites)


#Cambiar "triste" a "enojado"
opposites[4][0] = "enojado"
print(opposites)

/************************************************************************************
Comprobar e imprimir valores de listas.
Un término técnico para cada una de las listas que están dentro de nuestra lista principal es fila.

El código que está en el editor muestra algunas maneras en que podemos usar con las listas bidimensionales las técnicas que aprendimos para las listas unidimensionales.
************************************************************************************/
#Lista de opuestos
opposites = [["sí", "no"], ["caliente", "frío"], ["bajo", "alto"], ["dulce", "agrio"], ["alegre", "triste"]]

#Revisa si un valor está en una fila/sublista dada (revisa si "sí" está en la primera lista)
if "sí" in opposites[0]:
  print("¡Lo encontré!")
else:
  print("No está aquí :(")

#Hacer bucle para imprimir valores en una fila
for word in opposites[2]:
  print(word)
  
#Revisar si un valor está en alguna de las filas
for row in opposites:
  if "dulce" in row:
    print("¡Lo encontré!")
  else:
    print("No está aquí :(")
    
#Imprimir todos los valores
for row in opposites:
  print("---- Siguiente fila ----")#Solo para separar las filas visualmente
  for word in row:
    print(word)
    
print("-------- Extensión --------")
#Extensión: preguntar al usuario una palabra y decirle la opuesta
word = input("Elige una palabra y te diré su opuesto: ").strip().lower()

#Buscar la palabra en cada fila. Si se encuentra la palabra, averiguar si es el primer valor del par, y luego imprimir el segundo. O si es el segundo, imprimir el primero. Usar un bucle for/else para que podamos decirle al usuario si la palabra no está ahí
for row in opposites:
  if word in row:
    print("¡Lo encontré!")
    if row.index(word) == 0: #Revisar si es la primera palabra del par
      opposite = row[1]
    else:
      opposite = row[0]
    
    print("¡El opuesto de {} es {}!".format(word, opposite))
    
    break #Salir del bucle si encontramos la palabra
else:
  print("No conozco esa palabra :(")
  
 /*********************************************************************************
 opposites = [["sí", "no"], ["caliente", "frío"], ["bajo", "alto"], ["dulce", "agrio"], ["alegre", "triste"]]

#Quitar una lista ["sí", "no"] de la lista principal
opposites.pop(0)
print(opposites)

#Quitar el segundo valor (frío) de la (ahora) primera fila
opposites[0].pop(1)
print(opposites)

#Quitar una lista de la lista principal
opposites.remove(["dulce", "agrio"])
print(opposites)

#Quitar el segundo valor (alto) de la segunda fila
opposites[1].remove("alto")
print(opposites)

#Insertar una lista en la lista principal en la posición 1
opposites.insert(1, ["noche", "día"])
print(opposites)

#Insertar un elemento en la mitad de la última fila
opposites[-1].insert(1, "promedio")
print(opposites)

#Anexar una lista al final de la lista principal
opposites.append(["bueno", "malo"])
print(opposites)

#Anexar un elemento en la última fila
opposites[-1].append("horrible")
print(opposites)

/***********************************************************
Usar listas bidimensionales en un programa de cuestionario
Veamos cómo las listas bidimensionales pueden ser útiles en código que hemos visto antes. Para esta tarea se necesitan varias habilidades, ¡así que puede ser complicada!

En el editor está el código del cuestionario que vimos en la última lección. Vamos a usar una lista bidimensional para las respuestas correctas de manera que el programa sea un poco más robusto .

También vamos a usar un bucle para hacer las preguntas, así no tendremos que codificar 5 veces la parte de hacer las preguntas y comprobar.

En la línea 17 verás una nueva función llamada zip() que nos permite hacer recorrer con un bucle ambas listas a la vez. A continuación verás una explicación más detallada de esto.
**************************************************************/
#Preguntas y respuestas de un cuestionario. Observa que estos elementos de lista más largos se escriben cada uno en una línea para que sean más fáciles de leer.
questions = ["¿Cuántos bits tiene un byte?",
            "¿Verdadero o falso? Un cuarteto es medio byte.",
            "¿En qué año se fundó Google?",
            "¿Cuántos ceros hay en un gúgol?",
            "¿Cuántos bytes tiene un kilobyte?"]

answers = [["8","ocho"], ["verdadero","t"], ["1998","98"],["100","cien"], ["1024","mil veinticuatro"]]

score = 0

#Preguntarle el nombre al usuario y darle la bienvenida al cuestionario
name = input("¿Cómo te llamas?")
print("¡Bienvenido al cuestionario, {}! Hay 5 preguntas.".format(name))

#Usar un bucle para hacer las preguntas y tomar de la entrada la respuesta del usuario
for question, answer_list in zip(questions, answers):
  guess = input(question).strip().lower()

  #Comprobar que la respuesta del usuario esté en la fila correspondiente
  if guess in answer_list:
    print("¡Correcto!")
    score += 1
  else:
    print("¡Incorrecto! La respuesta correcta era {}.".format(answer_list[0]))

print("Tu puntuación es {}/5, {}".format(score, name))

**********************************************************************************
Repaso listas 
**********************************************************************************
#Crear una lista llamada números
numbers = [5, 10, 15, 20]

#Crear una lista de animales
animals = ["Dog","Cat","Horse","Bird","Bear"]

#Imprimir el primer número
print(numbers[0])

#Imprimir el último animal
print(animals[-1])

/****************************
#Crear una lista llamada números
numbers = [5, 10, 15, 20]

#Crear una lista de animales
animals = ["gato", "perro", "conejo", "tortuga", "ratón"]

#Insertar el número 0 al inicio de la lista de números
numbers.insert(0,0)


#Agregar "serpiente" al final de la lista de animales
animals.append("serpiente")


#Quitar 20 de la lista de números
numbers.remove(20)


#Quitar el tercer animal de la lista de animales
animals.pop(2)

#Imprimir las listas
print(numbers)
print(animals)

/***********************************************************
Repaso de ordenar al azar, ordenar y usar bucles para recorrer listas
Las listas tienen una función integrada llamada sort() que ordena listas. Esto funciona si el tipo de dato de toda la lista es el mismo, pero no es posible ordenar una lista con, por ejemplo, cadenas y enteros.

También podemos ordenarla al azar, pero para eso debemos importar el módulo random.

Si queremos usar cada uno de los valores, podemos usar in para recorrer la lista con un bucle for.
****************************************************************************************************/
#Agregar módulo aleatorio
import random

#Crear una lista de animales
animals = ["perro", "tortuga", "ratón", "gato", "serpiente"]

#Ordenar la lista alfabéticamente
animals.sort()

#Imprimir la lista con un bucle
for animal in animals:
  print(animal)



print("----------------")

#Ordenar la lista al azar
random.shuffle(animals)

#Imprimir la lista otra vez con un bucle
for animal in animals:
  print(animal)
  
/********************************************
#Crear una lista de estudiantes
students = ["lisa", "sebastian", "frank", "maia",  "alex"]

#Imprimir los primeros 2 estudiantes
print(students[0:2])

#Imprimir los últimos 3 estudiantes
print(students[2:])

#Imprimir los 3 estudiantes del medio
for student in students[1:4]:
  print(student)
  

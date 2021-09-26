/*************************************************************************************
Reconocer funciones que ya conoces
Ya sabes un montón acerca de las funciones gracias a las que vienen integradas en Python.

Las funciones tienen un nombre, y para usarlas escribes ese nombre y paréntesis, p. ej.,int().
A veces colocas información (argumentos) entre los paréntesis, p. ej., print("¡Hola!") o my_list.insert(0, "lince")
A veces las funciones te devuelven un valor que puedes usar o almacenar en un variable, p. ej.,
#Almacena información en una variable
name = input("¿Quién eres?")
#Imprime 5 porque len devuelve un número
print(len("Hola"))
********************************************************************************************/
#Crear funciones que suman una cantidad a un número ingresado.
def add_10(number):
  print(number + 10)
  
def add_20(number):
  return number + 20

#Llamar a la función add_10
add_10(5)

#Llamar a la función add_20
print(add_20(5))

/***********************************************************************
Crear una función con entradas del usuario.
Esta vez, armemos una nueva función desde cero y hagámosla un poco más interactiva.

Las funciones usan bloques como bucles, y sentencias if, por lo que el código que se incluye en la función es el código que tiene sangría:

def my_function():
  print("¡Estoy dentro de la función!")
  print("¡Yo también estoy dentro de la función!")

print("¡Estoy fuera de la función!")
****************************************************************************/
#Crear una función que le diga hola al usuario
def hello_user():
  name = input("Como te llamas")
  print("¡Hola,{}".format(name))
hello_user()

/***************************************************
Hacer cálculos con funciones
Esta vez vamos a usar una función para preguntarle al usuario la length y el width de un rectángulo, y luego darle el area de la figura.
*/******************************************************
#Crear una función que calcule un área
def calc_area():
  length = float(input("¿Cuál es la longitud del rectángulo en centímetros?"))
  width = float(input("¿Cuál es el ancho del rectángulo en centímetros?"))
  area = length * width
  print("El área es: {:.2f} cm²".format(area))
calc_area()
/****************************************************
Crear una función para el perímetro.
¡Fantástico! Con suerte estás entendiendo cómo está estructurada una función. Probemos crear una función más antes de pasar a usar parámetros en la próxima lección. Esta vez: perímetro.
*/*************************************************
#Crear una función para el perímetro de un rectángulo
def calc_perimeter():
  length = float(input("¿Cuál es la longitud del rectángulo en centímetros? "))
  width = float(input("¿Cuál es el ancho del rectángulo en centímetros? "))
  perimeter = length + width + length + width
  print("El perímetro es: {:.2f} cm".format(perimeter))

calc_perimeter()

/******************************************************
Entender las variables en las funciones.
Las funciones están pensadas para hacer que tu código sea modular, y para que no se repita a sí mismo. En nuestras funciones de calc_area() y calc_perimeter(), pedimos la length y el width dentro de la función.

Como estas variables se crean dentro de la función, se las llama variables locales, y solo es posible acceder a ellas dentro de la función. Veamos qué significa esto.

Obtenemos un mensaje de NameError (error de nombre) porque estamos tratando de usar las variables fuera de la función, o fuera de su ámbito, por eso el intérprete no encuentra una variable con ese nombre.

Las variables creadas dentro de una función son de ámbito local, y las variables creadas fuera de las funciones son de ámbito global porque es posible acceder a ellas desde cualquier lugar.
*********************************************************/

/*********************************************************
Establecer los parámetros de una función
Ahora que juntamos el código de las funciones del área y del perímetro en un programa, tenemos algo de código que se repite. Sería útil si solo tuviéramos que pedir las medidas una vez, y luego pudiéramos darle al usuario ambos cálculos a partir de las mismas medidas. ¡Para eso son los parámetros!

Para establecer los parámetros de una función, simplemente ponemos entre los paréntesis los nombres con los que queremos referirnos a ellos:

def my_function(a_parameter, another_parameter):
   #código que hace cosas
Puedes tener 0 o más parámetros en una función. En este caso, queremos 2. Modifiquemos el código para que las funciones acepten parámetros.
*/***********************************************************
#Crear una función que calcule un área
def calc_area(length,width):
  area = length * width
  print("El área es: {}cm".format(area))

#Crear una función para el perímetro de un rectángulo
def calc_perimeter(length,width):
  perimeter = 2 *length + 2 * width
  print("El perímetro es: {}cm".format(perimeter))

#Obtener las medidas a partir de las respuestas del usuario
length = float(input("¿Cuál es la longitud del rectángulo en centímetros? "))
width = float(input("¿Cuál es el ancho del rectángulo en centímetros? "))
/**********************************************************************
Usar variables globales.
Ahora que pusimos nuestras variables fuera de nuestras funciones, son de ámbito global, y deberíamos poder acceder a los valores en la parte principal de nuestro código.

Probemos eso antes de usar nuestras funciones.
**************************************************************************/
#Crear una función que calcule un área
def calc_area(length, width):
  area = length * width
  print("El área es: {}cm".format(area))

#Crear una función para el perímetro de un rectángulo
def calc_perimeter(length, width):
  perimeter = 2 *length + 2 * width
  print("El perímetro es: {}cm".format(perimeter))

#Obtener las medidas a partir de las respuestas del usuario
length = float(input("¿Cuál es la longitud del rectángulo en centímetros? "))
width = float(input("¿Cuál es el ancho del rectángulo en centímetros? "))

print(length)
print(width)

/*******************************************************************
Llamar a una función y usar argumentos .
Cuando llamamos a una función que tiene parámetros, debemos introducir la misma cantidad exacta de valores que establecimos cuando creamos la función. Los valores que introducimos en la función cuando la llamamos se llaman argumentos, aunque los nombres argumento y parámetro suelen usarse de forma indistinta.

Observa que estos valores no tienen que tener los mismos nombres, aunque en este ejemplo los tienen porque estamos almacenando la entrada del usuario en length y width.
******************************************************************/
#Crear una función que calcule un área
def calc_area(length, width):
  area = length * width
  print("El área es: {:.2f}cm".format(area))

#Crear una función para el perímetro de un rectángulo
def calc_perimeter(length, width):
  perimeter = 2 *length + 2 * width
  print("El perímetro es: {:.2f}cm".format(perimeter))

#Obtener las medidas a partir de las respuestas del usuario
length = float(input("¿Cuál es la longitud del rectángulo en centímetros? "))
width = float(input("¿Cuál es el ancho del rectángulo en centímetros? "))

calc_area(length, width)
calc_perimeter(length, width)
/**************************************************************************
Usar return para obtener un valor de una función
Los parámetros/argumentos nos permiten enviar valores a una función, pero a veces una función también necesita devolvernos un valor para que podamos usarlo. Para eso, usamos la palabra clave return (devolver) que ya hemos visto un par de veces.

En el editor hay dos funciones, una que devuelve un número y una que debe devolver una cadena. Veamos cómo funciona.
******************************************************************************/
#Una función que suma 100 a un número
def add_100(number):
  number += 100
  return number
  
#Una función que multiplica una cadena
def multiply_string(string, number):
  new_string = string * number
  return new_string
  

#Llamar a las funciones
print(add_100(5))
print(multiply_string("Hola", 3))
/*******************************************************************************
Almacenar valores devueltos para usarlos en el programa
Entonces, si un valor es devuelto por una función, podemos imprimirlo para verlo, pero eso no es muy útil. Lo más probable es que queramos usar el valor para algo más en nuestro programa, por eso tiene sentido almacenarlo en una variable.

Para ello, usamos nuestro operador habitual = para asignar un valor, y en este caso ponemos la llamada del lado derecho:

new_number = add_100(5)
Entonces podemos usar el nombre de variable new_number para acceder al valor devuelto.
**************************************************************************/
#Esta función calcula el precio después de un descuento y lo devuelve. Usa 2 parámetros: precio y descuento.
def calc_discount(price, discount):
  #Convertir el porcentaje de descuento en un número decimal
  discount_value = discount / 100 
  
  #Calcular la cantidad que se descuenta y restarla del precio
  discount_amount = price * discount_value
  price -= discount_amount
  
  return price
  
#Calcular el descuento sobre un precio y decírselo al usuario
new_price = calc_discount(39.99, 15)

print("El nuevo precio después del descuento es: ${}.".format(new_price))

/**************************************************************************

# Función para forzar una entrada numérica
def force_number(message):
  while True:
    try:
      number = float(input(message))
      break
    except ValueError:
      print("Por favor, ingresa un número")
      
  return number

#Esta función calcula el precio después de un descuento y lo devuelve. Usa 2 parámetros: precio y descuento.
def calc_discount(price, discount):
  #Convertir el porcentaje de descuento en un número decimal
  discount_value = discount / 100 
  
  #Calcular la cantidad que se descuenta y restarla del precio
  discount_amount = price * discount_value
  price -= discount_amount
  
  return price
  
#Preguntar al usuario el precio y el monto del descuento
price = force_number("Ingresa el precio del artículo, por ejemplo, 29.99:")
discount = force_number("Ingresa el porcentaje de descuento, por ejemplo, 10:")

#Calcular el nuevo precio y comunicárselo al usuario
new_price = calc_discount(price, discount)
print("El nuevo precio después del {:.1f} % de descuento sobre ${:.2f} es: ${:.2f}.".format(discount,price,new_price))

/**************************************************************************
Devolver y almacenar más de un valor.
A veces, una función podría tener que devolver más de un valor para que usemos en nuestro programa. Por suerte, eso es fácil en Python, y tal como vimos en el curso de nivel 1, también podemos asignar valores a más de una variable a la vez:

def some_function(param1, param2):
  param1 += 10
  param2 += 20
  return param1, param2

myvar1, myvar2 = some_function(arg1, arg2)
Solo separamos con comas , los valores que estamos devolviendo y hacemos lo mismo para los nombres de la variable donde los queremos almacenar cuando llamamos a la función.

Una característica útil de nuestro programa podría ser decirle al usuario cuánto dinero ahorró gracias al descuento.
*//////**************************************************************************
# Función para forzar una entrada numérica
def force_number(message):
  while True:
    try:
      number = float(input(message))
      break
    except ValueError:
      print("Por favor, ingresa un número")
      
  return number

#Esta función calcula el precio después de un descuento y lo devuelve. Usa 2 parámetros: precio y descuento.
def calc_discount(price, discount):
  #Convertir el porcentaje de descuento en un número decimal
  discount_value = discount / 100 
  
  #Calcular la cantidad que se descuenta y restarla del precio
  discount_amount = price * discount_value
  price -= discount_amount
  
  return price, discount_amount
  
#Preguntar al usuario el precio y el monto del descuento
price = force_number("Ingresa el precio del artículo, por ejemplo, 29.99: ")
discount = force_number("Ingresa el porcentaje de descuento, por ejemplo, 10: ")

#Calcular el nuevo precio y comunicárselo al usuario
new_price, money_saved = calc_discount(price, discount)
print("El nuevo precio después del {:.1f} % de descuento sobre ${:.2f} es: ${:.2f}. ¡Ahorraste ${:.2f}!".format(discount, price, new_price, money_saved))

/*******************************************************************************
Recordatorio de gráficos de tortuga
Si hiciste el curso de nivel 1, sabrás acerca de los gráficos de tortuga. Se trata de un módulo integrado en Python que te permite escribir instrucciones para que una tortuga haga dibujos en el lienzo por ti.

Hagamos un recordatorio de los conceptos básicos y luego pongamos en práctica lo que hemos aprendido sobre funciones, parámetros, argumentos y valores de devolución. En el panel de código de ejemplo hay un ejemplo de cómo comenzar a usar gráficos de tortuga que puede servirte de guía para estas tareas.
***********************************************************************************/
#Importar el módulo de tortuga
import turtle

#Crear una tortuga
tyrel = turtle.Turtle()

#Hacer que diga "Me llamo Tyrell" y luego se mueva y gire
tyrel.write("Me llamo Tyrell")
tyrel.forward(100)
tyrel.left(90)
tyrel.forward(50)

/******************************************************************************/
#Importar el módulo de tortuga
import turtle

#Crear una tortuga
tyrell = turtle.Turtle()

#Crear una función que dibuje un cuadrado
def draw_square(size):
  for i in range(4):
    tyrell.forward(size)
    tyrell.left(90)
  

draw_square(150)
draw_square(200)
draw_square(250)

/*******************************************************************************/
#Importar el módulo de tortuga
import turtle

#Crear una tortuga
tyrell = turtle.Turtle()

#Crear una función que dibuje un rectángulo
def draw_rectangle(width,height):
  for i in range(2):
    tyrell.forward(width)
    tyrell.left(90)
    tyrell.forward(height)
    tyrell.left(90)

# Pedir al usuario las dimensiones
width = float(input("Ingresa el ancho:"))
height = float(input("Ingresa el alto:"))
draw_rectangle(width,height)

/************************************************************************************/
#Importar el módulo de tortuga
import turtle

#Crear una tortuga
tyrell = turtle.Turtle()

#Crear una función que dibuje un cuadrado
def draw_rectangle(start_x, start_y, width, height, stroke_color, fill_color):
  tyrell.penup()
  tyrell.goto(start_x, start_y)
  tyrell.pendown()
  tyrell.color(stroke_color)
  tyrell.fillcolor(fill_color)
  tyrell.begin_fill()
  for i in range(2):
    tyrell.forward(width)
    tyrell.left(90)
    tyrell.forward(height)
    tyrell.left(90)
  tyrell.end_fill()

width = float(input("Ingresa el ancho: "))
height = float(input("Ingresa la altura: "))
start_x = 50
start_y = 50
stroke_color = 'red'
fill_color = 'green'
draw_rectangle(start_x,start_y,width, height,stroke_color,fill_color)

/********************************************************************************/
#Importar el módulo de tortuga
import turtle

#Crear una tortuga
tyrell = turtle.Turtle()

#Crear una función que dibuje un cuadrado
def draw_rectangle(start_x, start_y, width, height, stroke_color, fill_color):
  tyrell.penup()
  tyrell.goto(start_x, start_y)
  tyrell.pendown()
  tyrell.color(stroke_color)
  tyrell.fillcolor(fill_color)
  tyrell.begin_fill()
  for i in range(2):
    tyrell.forward(width)
    tyrell.left(90)
    tyrell.forward(height)
    tyrell.left(90)
  tyrell.end_fill()
x = float(input("Ingresa la coordenada x de la posición de inicio:"))
y = float(input("Ingresa la coordenada y de la posición de inicio:"))
width = input("Ingresa el ancho: ")
height = input("Ingresa la altura: ")
color1 = input("Elige un color de trazo:")
color2 = input("Elige un color de relleno:")


draw_rectangle(x, y, width, height, color1, color2)

/**********************************************************************/
#Función para calcular el monto del impuesto
def price_calculator(price, tax=15):
  tax_rate = tax / 100
  before_tax_price = price / (1 + tax_rate)
  #Calcular el componente impositivo
  tax_component = price - before_tax_price
  return price, tax_component

#Preguntar el precio al usuario
price = float(input("¿Cuál es el costo total del pedido? "))

#Comprobar si desea ingresar el impuesto y las tasas de descuento habituales
dif_rates = input("Si tu tasa impositiva es diferente de 15 %, escribe sí ahora:").strip().lower()

if dif_rates == "sí":
  tax = float(input("Ingresa la tasa impositiva: "))
  price, tax_component = price_calculator(price,tax)
else:
  price, tax_component = price_calculator(price)
  
print("Costo del impuesto: ${:.2f} Precio total = ${:.2f}".format(tax_component, price))

/************************************************************************************/
variables globales y variables locales*/

import random

#Función para cambiar números por cantidades al azar
def change_numbers(number1, number2):
  amount_to_change = random.randrange(-100, 100)
  new_number1 = number1 + amount_to_change
  new_number2 = number2 + amount_to_change
  
  return new_number1, new_number2, amount_to_change

#Explicar el programa al usuario y pedirle que elija 2 números para cambiar
print("Este programa te pedirá 2 números y los cambiará en la misma cantidad al azar. Luego puedes adivinar la cantidad")
num1 = int(input("Elige un número: "))
num2 = int(input("Elige otro número: "))

#Cambiar los números
new_num1, new_num2, amount_changed = change_numbers(num1, num2)

print("Tus nuevos números son {} y {}".format(new_num1, new_num2))

#Pedir al usuario que calcule en cuánto cambiaron
guess = int(input("¿En cuánto cambiaron?"))
if guess == amount_changed:
  print("¡Correcto!")
else:
  print("No, fue {}".format(amount_changed))
  
/**************************************************************************/
#Crear una función que calcule un área
def calc_area(length, width):
  area = length * width
  print("El área es: {}cm".format(area))

#Crear una función para el perímetro de un rectángulo
def calc_perimeter(length, width):
  perimeter = 2 *length + 2 * width
  print("El perímetro es: {}cm".format(perimeter))

#Obtener las medidas a partir de las respuestas del usuario
length = float(input("¿Cuál es la longitud del rectángulo en centímetros? "))
width = float(input("¿Cuál es el ancho del rectángulo en centímetros? "))

/****************************************************************************
Ejercicio funciones Calculadora
*////*********************************************************************
#Crear una función de menú que enumere los modos en la calculadora
def menu():
  mode = input("""Choose a mode by entering the number:
  1: Addition
  2: Subtraction
  3: Multiplication
  4: Division
  5: Powers
  6: Exit""").strip()
  return mode
*************************
#Crear una función de menú que enumere los modos en la calculadora
def menu():
  mode = input("""Ingresa un número para elegir un modo:
"1: Suma
"2: Resta
"3: Multiplicación
"4: División
"5: Potencias
              "6: Salir""").strip()
  return mode
  
#Función de suma
def add(number1, number2):
  answer = number1 + number2
  return answer

#Función de resta
def subtract(number1, number2):
  answer = number2 - number1
  return answer

#Función de multiplicación


#Función de división


#Función de potencias


#Bucle del programa principal
*************************************************************/
#Crear una función de menú que enumere los modos en la calculadora
def menu():
  mode = input("""Ingresa un número para elegir un modo:
"1: Suma
"2: Resta
"3: Multiplicación
"4: División
"5: Potencias
"6: Salir""").strip()
  return mode
  
#Función de suma
def add(number1, number2):
  answer = number1 + number2
  return answer

#Función de resta
def subtract(number1, number2):
  answer = number1 - number2
  return answer

#Función de multiplicación
def multiply(number1, number2):
  answer = number1 * number2
  return answer

#Función de división
def divide(number1, number2):
  answer = number1 / number2
  return answer

#Función de potencias
def powers(number1, number2):
  answer = number1 ** number2
  return answer

#Bucle del programa principal
solution = add(2,2)
print(solution)

/*********************************************************/
#Crear una función de menú que enumere los modos en la calculadora
def menu():
  mode = input("""Ingresa un número para elegir un modo:
"1: Suma
"2: Resta
"3: Multiplicación
"4: División
"5: Potencias
              "6: Salir""").strip()
  return mode
  
#Función de suma
def add(number1, number2):
  answer = number1 + number2
  return answer

#Función de resta
def subtract(number1, number2):
  answer = number1 - number2
  return answer

#Función de multiplicación
def multiply(number1, number2):
  answer = number1 * number2
  return answer

#Función de división
def divide(number1, number2):
  answer = number1 / number2
  return answer

#Función de potencias
def powers(number1, number2):
  answer = number1 ** number2
  return answer

#Bucle del programa principal
while True:
 
  

  #Imprimir el menú y obtener la elección de modo del usuario
  mode = menu()
  
  #Comprobar que sea una opción válida
  if mode in ["1", "2", "3", "4", "5", "6"]:
    
    #Pedir números al usuario
    num1 = int(input("Ingresa el primer número:"))
    num2 = int(input("Ingresa el segundo número:"))
  else:
    print("Oh, oh… esa no era una opción. ¡Inténtalo de nuevo!")
    
    #Hacer la operación matemática elegida con números, o salir del bucle si se elige la salida
    
    
  #De lo contrario, decirle al usuario que esa no era una opción

#Despedir al usuario cuando salga


#Crear una función de menú que enumere los modos en la calculadora
def menu():
  mode = input("""Ingresa un número para elegir un modo:
"1: Suma
"2: Resta
"3: Multiplicación
"4: División
"5: Potencias
              "6: Salir""").strip()
  return mode
  
#Función de suma
def add(number1, number2):
  answer = number1 + number2
  return answer

#Función de resta
def subtract(number1, number2):
  answer = number1 - number2
  return answer

#Función de multiplicación
def multiply(number1, number2):
  answer = number1 * number2
  return answer

#Función de división
def divide(number1, number2):
  answer = number1 / number2
  return answer

#Función de potencias
def powers(number1, number2):
  answer = number1 ** number2
  return answer
  
#Bucle del programa principal
while True:
  
  #Imprimir el menú y obtener la elección de modo del usuario
  mode = menu()
  
  #Comprobar que sea una opción válida
  if mode in ["1", "2", "3", "4", "5", "6"]:
    
    #Pedir números al usuario
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    
    #Hacer la operación matemática elegida con números, o salir del bucle si se elige la salida
    if mode == "1":
      solution = add(num1,num2)
      print("{} + {} = {}".format(num1, num2, solution))
    elif mode == "2":
      solution = subtract(num1,num2)
      print("{} - {} = {}".format(num1, num2, solution))
    elif mode == "3":
      solution = multiply(num1, num2)
      print("{} * {} = {}".format(num1, num2, solution))
    elif mode == "4":
      solution = divide(num1, num2)
      print("{} / {} = {}".format(num1, num2, solution))
    elif mode == "5":
      solution = powers(num1, num2)
      print("{} ^ {} = {}".format(num1, num2, solution))
    else:
      break
  #De lo contrario, decirle al usuario que esa no era una opción
  else:
    print("Oh, oh… esa no era una opción. ¡Inténtalo de nuevo!")
print("¡Adiós!")

*/*****************************************************************/
repaso funciones de listas
******************************************************************/
#Crear una lista
rides = ["Kamikaze", "Matterhorn", "Bumper Boats", "Freefall", "Aqualoop", "Ferris Wheel", "Gravitron"]

#Anexar un elemento
rides.append("Tea Cups")

#Insertar un elemento
rides.insert(0,"Carousel")

#Quitar un elemento
rides.remove("Matterhorn")

#Quitar un elemento con pop
rides.pop(2)

#Imprimir Carousel y Gravitron
print(rides[0])
print(rides[2])

#Imprimir un espacio
print("")

#Imprimir la lista con un bucle
for ride in rides:
  print(ride)
  
/************************************************************************/
# Imprimir el menú para que el usuario sepa cuáles son las opciones y obtener la opción que elija el usuario
def menu():
  
  mode = input("""Ingresa un número para elegir un modo:
  1: Agregar una tarea
  2: Ver una lista
  3: Salir
  """).strip()
  
  return mode

# Función que le permite al usuario agregar una tarea a su lista de pendientes
def add_task():
  new_task = input("Ingresa la tarea que deseas agregar:")
  todo_list.append(new_task)

# Función que muestra las tareas actuales de la lista de pendientes
def view_list():
  for task in todo_list:
    print("- {}".format(task))
    
/*****************************************************************************
# Imprimir el menú para que el usuario sepa cuáles son las opciones y obtener la opción que elija el usuario
def menu():
    
  mode = input("""Ingresa un número para elegir un modo:
  1: Agregar una tarea
  2: Ver la lista
  3: Salir
  """).strip()

  return mode

# Función que le permite al usuario agregar una tarea a su lista de pendientes
def add_tasks():
  new_task = input("Ingresa la tarea que deseas agregar: ")
  todo_list.append(new_task)

# Función que muestra las tareas actuales de la lista de pendientes
def view_list():
  for task in todo_list:
    print("- {}".format(task))

# Crear una lista vacía para almacenar las tareas
todo_list = []

# Ejecutar el programa principal en un bucle.
while True:
  chosen_option = menu()
  if chosen_option == '1':
    add_tasks()
  elif chosen_option == '2':
    print("Esta es tu lista de pendientes:")
    view_list()
  elif chosen_option == '3':
    break
  else:
    print("Esa no era una opción. Inténtalo de nuevo.")
    
/*********************************************************
# Imprimir el menú para que el usuario sepa cuáles son las opciones y obtener la opción que elija el usuario
def menu():
    
  mode = input("""Ingresa un número para elegir un modo:
  1: Agregar una tarea
  2: Ver la lista
  3: Salir
  """).strip()

  return mode

# Función que le permite al usuario agregar una tarea a su lista de pendientes
def add_tasks():
  while True:
    new_task = input("Ingresa la tarea que deseas agregar o escribe 'fin' para regresar al menú:").lower().strip()
    if new_task == 'fin':
      break
    else:
      todo_list.append(new_task)

# Función que muestra las tareas actuales de la lista de pendientes
def view_list():
  for task in todo_list:
    print("- {}".format(task))

# Crear una lista vacía para almacenar las tareas
todo_list = []

# Ejecutar el programa principal en un bucle.
while True:
  chosen_option = menu()

  if chosen_option == "1":
    add_tasks() 
  elif chosen_option == "2":
    print("Esta es tu lista de pendientes:")
    view_list()
  elif chosen_option == "3":
    break
  else:
    print("Esa no era una opción. Inténtalo de nuevo.")

/****************************************************************/
# Imprimir el menú para que el usuario sepa cuáles son las opciones y obtener la opción que elija el usuario
def menu():
    
  mode = input("""Ingresa un número para elegir un modo:
  1: Agregar una tarea
  2: Ver la lista
  3: Salir
  """).strip()

  return mode

# Función que le permite al usuario agregar una tarea a su lista de pendientes
def add_tasks():
  while True:
    new_task = input("Ingresa la tarea que deseas agregar o escribe 'fin' para regresar al menú:").lower().strip()
    if new_task == 'fin':
      break
    else:
      todo_list.append(new_task)

# Función que muestra las tareas actuales de la lista de pendientes
def view_list():
  if len(todo_list) > 0:
    for task in todo_list:
      print("- {}".format(task))
  else:
    print("¡Aún no tienes tareas!")

# Crear una lista vacía para almacenar las tareas
todo_list = []

# Ejecutar el programa principal en un bucle.
while True:
  chosen_option = menu()

  if chosen_option == "1":
    add_tasks() 
  elif chosen_option == "2":
    print("Esta es tu lista de pendientes:")
    view_list()
  elif chosen_option == "3":
    break
  else:
    print("Esa no era una opción. Inténtalo de nuevo.")
print("¡Adiós!")

/*******************/
Recuerdo try : except
******************/
#Función para calcular el descuento y el monto del impuesto
def price_calculator(price, discount):
  discount_rate = discount / 100
  discount_amount = price * discount_rate
  price -= discount_amount
  return price

#Preguntar el precio al usuario
while True:
  try:
    original_price = float(input("¿Cuál es el costo total del pedido? "))
    break
  except ValueError:
    print("¡Por favor, ingresa un número válido!")

#Pedir un porcentaje de descuento y asegurarse de que esté entre 0 y 100
while True:
  try:
    discount = float(input("Ingresa el porcentaje de descuento: "))
    if discount >= 0 and discount <= 100:
      break
    else:
      print("Ingresa un número entre 0 y 100")
  except ValueError:
    print("¡Por favor, ingresa un número válido!")
  
#Calcular y generar el descuento
discounted_price = price_calculator(original_price, discount)

print("El precio después de un {:.1f} % de descuento es ${:.2f}".format(discount, discounted_price))


/**************************************************/
Repaso Funciones
******************************************************/
def my_function(number):
  #Código que hace cosas
  print("Esta sentencia print está dentro de la función")
  lucky_number = 7
  new_number = 7 + number
  
  print("Esta sentencia print también está dentro de la función")
  return new_number

#Llamar a la función
print(my_function(8))







'''
Lenguaje de programación - Python
- Alto nivel
- General
- Interpretado
'''

'''
Se compone principalmente de operadores y literales (objetos)
<Literales>     1, 'abc', 2.0, True 
<Operadores>    + / * % ** = ==
<literal>   <operador>  <literal>
    1           +           2
'''
#print(1 + 2)
#1 3.0              #SyntaxError
#5 / 'Python'       #TypeError

# Statement o enunciado.
print("Hello World!")
# Escribir una cadena de caracteres.
print("Python Rocks!")
# Podemos "Sumar" dos cadenas de caracteres.
print("Python" + "Rocks!")
# Podemos sumar numeros enteros.

'''Tenemos diferentes tipos de variables'''

my_int = 1          #Integer
my_float = 1.0      #Float
my_bool = False     #Boolean
my_none = None      #NoneType

'''Variables'''

# Las variables son nombres que se vinculan cn un valor en memoria y el cual lo vinculamos
# a traves del operador asignacion "="

a = 2
#id(a)
b = 3
#id(b)
c = (a * b) / 2

# Sin embargo, para un programador esto no significa nada y mucho menos si es alguien que
# no esta familiarizado con la programación. Así.

base = 2
altura = 4
area = (base * altura) / 2

# Esto tiene mucho mas sentido para el programador que lee el programa.

'''Importante'''

# Podemos sobreescribir la direccion donde apunta esta variable por medio de la re-asignacion

my_var = 'Hello World!'
print(my_var)
#id(my_var)
my_var = 3
print(my_var)
#id(my_var)

# Las variables pueden contener mayusculas, minusculas, numeros (sin comenzar con uno)
# y el simbolo "_"

'''Importante'''

# No pueden llamarse como las palabras reservadas!
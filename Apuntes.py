#Tipos de datos
                                     ejemplos:

string = ""                          variable = "contenido, variable"
                                     print(variable)
-----------------------------------------------------------------------
int = 0                              variable = 30
-----------------------------------------------------------------------
list = ["a", "b"]                    numeros = ["1", "2", "3"]
-------------------------------------------------------------------------------------
tupla = ()                           numeros_letras = (true, 45, 1.75, "Juan Pérez")
---------------------------------------------------------------------------------------
float = 1.5                          decimales = 1.5


#Bucles-----------------------------------------------------------------------------------------------

edad = 20

if edad >= 18:
    print("Eres mayor de edad.")


# == igual      != distinto
# #if inicia division
# < mayor q     > menor q
# <= mayor o igual q
# >= menor o igual q
# in    dentro de
# not in     no dentro de
#elif otra division dentro del if
# else lo demas
------------------------------------------
puntaje = 85

if puntaje >= 90:
    print("Obtienes una A.")
elif puntaje >= 80:
    print("Obtienes una B.")
elif puntaje >= 70:
    print("Obtienes una C.")
else:
    print("Tienes que mejorar.")
--------------------------------------------

texto = ["hola","mundo","maravilloso"]
for palabra in texto:       # palabra es una nueva variable dentro de texto
    print(palabra)          #sirve para recorrer strings/listas
-------------------------------------------------------------------------
contador = 1

i = 0                       #contador
while i != 3:                   #mientras que no sea igual, ejecuta el codigo
    print("se esta cargando")   #contador necesario
    i = i + 1                   # contador es (i = 0) y dentro (i = i+1)
------------------------------------------------------------------------------------

# .funcion()

lista_vacia.append(variable)        # .append()     añade variable al final de lista_vacia
                                    # se suele poner dentro de un for
--------------------------------------------------------------------------------------------

variable = variable.lower()     #caombierte la variable a letras minusculas (siempre tiene que ser un string)

variable = variable.upper()     #caombierte la variable a letras mayusculas (siempre tiene que ser un string)

variable = variable.capitalize()    #caombierte la primera letra de variable a mayuscula (siempre tiene que ser un string)

variable = variable.sttrip()    #Elimina los espacios del principio y del final

variable = variable.replace()  #Remplaza todos los espacios por nada
--------------------------------------------------------------------------------------------------------------


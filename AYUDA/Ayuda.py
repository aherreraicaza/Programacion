# Tipos de datos

string = ""             #str
integer = 0             #int
lista = ["a", "b"]      #list / lst
floaty = 4.2            #float
diccionario = {1: "lunes", 2: "martes", 4:"jueves"}     #dict
tupla = (10,20,30,"hola","adios")       #tumpl

#bucles

if variable1 == variable2:      # == igual      != distinto         #if inicia division
    print("son iguales")        # < mayor q     > menor q
elif variable1 != variables2:   # <= mayor o igual q                #elif otra division dentro del if
    print("son distintas")      # >= menor o igual q
else:                           # in    dentro de                   #else lo demas
    print("todo lo demas")      # not in     no dentro de



texto = ["hola","mundo","maravilloso"]
for palabra in texto:       # in dentro de testo
    print(palabra)


i = 0
while i != 3:                   #mientras que no sea igual, ejecuta el codigo
    print("se esta cargando")   #contador necesario
    i = i + 1                   # contador es (i = 0) y dentro (i = i+1)


# .funcion()

lista_vacia.append(variable)        # .append()     añade variable al final de lista_vacia
                                    # se suele poner dentro de un for



variable = variable.lower()     #caombierte la variable a letras minusculas (siempre tiene que ser un string)

variable = variable.upper()     #caombierte la variable a letras mayusculas (siempre tiene que ser un string)

variable = variable.capitalize()    #caombierte la primera letra de variable a mayuscula (siempre tiene que ser un string)
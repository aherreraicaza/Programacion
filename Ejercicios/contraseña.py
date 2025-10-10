import random

longitud = int(input("Pon un numero del 6 al 12: "))

num = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()[]{}|@#~¬'

longitud_num = len(num)

guardar_contraseña = ''

if longitud >= 6 and longitud <=12:
    while longitud != 0:
        caracter = num[random.randint(0, longitud_num)]
        guardar_contraseña = guardar_contraseña + caracter
        longitud = longitud - 1

    print(guardar_contraseña)

else:
    print('error')
def nombres(tupla):
    for i in tupla:
        if i[1] == 'H':
            print(f'Hola don {i[0]}')
        elif i[1] == 'M':
            print(f'Hola dona {i[0]}')

nombres((("Ana", "M"), ("Luis", "H"), ("María", "M"), ("Carlos", "H")))
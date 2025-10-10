def es_bisiesto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))


fecha = input("Pon una fecha en formato dd/mm/aaaa: ").strip()

if len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/":
    dia, mes, ano = fecha.split("/")

    if dia.isdigit() and mes.isdigit() and ano.isdigit():
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        dias31 = [1, 3, 5, 7, 8, 10, 12]
        dias30 = [4, 6, 9, 11]

        if mes < 1 or mes > 12:
            print("[!] Mes inválido!")
        elif mes == 2:
            if (es_bisiesto(ano) and dia <= 29) or (not es_bisiesto(ano) and dia <= 28):
                print("[+] Fecha válida!")
            else:
                print("[!] Día inválido!")
        elif mes in dias31 and dia <= 31:
            print("[+] Fecha válida!")
        elif mes in dias30 and dia <= 30:
            print("[+] Fecha válida!")
        else:
            print("[!] Día inválido!")
    else:
        print("[!] Caracteres inválidos!")
else:
    print("[!] Formato inválido!")

dia = input("ingrese dia de la semana ")
dia = int(dia)

while(dia<=7 or dia>=1):
    if dia == 1:
        print("Dia laboral")
        break
    elif dia == 2:
        print("Dia laboral")
        break
    elif dia == 3:
        print("Dia laboral")
        break
    elif dia == 4:
        print("Dia laboral")
        break
    elif dia == 5:
        print("Dia laboral")
        break
    elif dia == 6:
        print("Dia no laboral")
        break
    elif dia == 7:
        print("Dia no laboral")
        break
    else:
        print("Ingrese un numero correcto")
        dia = input("ingrese dia de la semana ")
        dia = int(dia)

contraseña = "Hola"
i = 0 
intento = "aloH"

while(intento != contraseña):
    intento = input("Ingrese la contraseña ")
    i+=1
    if (intento == contraseña):
        print("Acceso correcto")
        break
    elif (i >= 3):
        print("Se bloqueo el acceso")
        break
num = input("ingrese un numero: ")
num = int(num)
cont = 0
for i in range (1, num+1):
    if(num % i == 0):
        cont +=1
        
if (cont ==2):
    print("es numero primo")   
else:
    print("el numero ingresado no es primo")     
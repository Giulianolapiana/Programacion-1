#Metodo:
def elminar_espacios(cadena):
    resultado=cadena.replace(" ","")#usamos la funcion replace para reemplazar los " " por "" en la cadena y 
    #y guardamos el resultante en la variable local de eliminar_espacios llamada resultado
    return resultado
#Guardamos la frase en la variable cadena
cadena=input("Ingrese una cadena:")
print(f"La cadena sin espacios es:{elminar_espacios(cadena)}")
#Llamamos a eliminar_espacios() y pasamos como argumento cadena para eliminar caracteres espacios.


"""23- Crea un programa donde se pida el ingreso de una cadena y por medio de
recursión mostrar la cadena de forma inversa.
Ejemplo: Ingreso “computadora de escritorio”
Invertir cadena “oirotircse ed arodatupmoc”
"""
def pal_recursiva(pal):
    if len(pal) == 0:
        return pal
    else:
        return pal[-1] + pal_recursiva(pal[:-1])


palabra = input("Ingrese una palabra/cadena: ")
pal_invertida = pal_recursiva(palabra)
print(f"La cadena invertida es: {pal_invertida}")
"""
Reto #1
¿Es un anagrama?
Dificultad: Media

Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
Un anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagramas.
"""
import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: ./Challenge01.py palabra1 palabra2")
    else:
        palabra1 = sys.argv[1]
        palabra2 = sys.argv[2]
        if son_anagramas(palabra1, palabra2):
            print(f"{palabra1} y {palabra2} son anagramas.")
        else:
            print(f"{palabra1} y {palabra2} no son anagramas.")

def son_anagramas(cadena1, cadena2):
    #Pasamos las cadenas ambas a minúsculas
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()
    
    #Comprobamos que no sean exactamente la misma palabra.
    if (cadena1==cadena2):
        return False
    
    #Las pasamos a cadenas para ordenarlas.
    lista1 = list(cadena1)
    lista2 = list(cadena2)

    #Las ordenamos
    lista1.sort()
    lista2.sort()
    
    #Y comprobamos si son iguales
    if (lista1==lista2):
        return True
    else:
        return False

if __name__ == '__main__':
    main()

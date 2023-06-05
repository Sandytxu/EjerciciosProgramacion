"""
Reto #2
LA SUCESIÓN DE FIBONACCI
Dificultad: Difícil

Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
La serie de Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def main():

    n0 = 0
    n1 = 1
    fib = 0
    contador=1
    while(contador<=50):
        print(f"Numero {contador}: {n0}")
        fib = n0+n1
        n0=n1
        n1=fib
        contador+=1

if __name__ == '__main__':
    main()

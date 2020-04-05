import random
import math

def varianza(X):
    mu = media(X)
    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2
    
    return acumulador / len(X)

def media(X):
    return sum(X) / len(X)

def desviacion_estandar(X):
    return math.sqrt(varianza(X))

if __name__ == "__main__":
    X = [random.randint(9,12) for i in range(11)]
    muu = lambda X: sum(X) / len(X)
    Var = varianza(X)
    sigmaa = lambda X: math.sqrt(varianza(X))
    #sqrt significa que es una raiz cuadrada

    print(f'Arrego de X = {X}')
    print(f'Media = {muu(X)}')
    print(f'Varianza = {Var}')
    print(f'Desviacion Estandar = {sigmaa(X)}')

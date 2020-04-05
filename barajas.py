import random
import collections

PALOS = ['espada', 'corazon', 'rombo','trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7','8', '9', 'jota', 'reina', 'rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    return mano

def flush(manos, intentos):
    colores = 0
    for mano in manos:
        color = []
        for carta in mano:
            color.append(carta[1])

        counter = dict(collections.Counter(color))
        for valor in counter.values():
            if valor == 5:
                colores += 1
                break
    probabilidad_par = (colores / intentos)*100
    print(f'La probabilidad de tener una flush en una mano de 5 bajarajas es {probabilidad_par}')

def main(tamano_mano, intentos):
    baraja = crear_baraja()
    manos = []

    for _ in range(intentos):
        mano = obtener_mano(baraja, tamano_mano)
        manos.append(mano)
    flush(manos, intentos)
    pares = 0
    for man in manos:
        valore = []
        for carta in man:
            valore.append(carta[1])

        conter = dict(collections.Counter(valore))

        for val in conter.values():
            if val == tamano_mano:
                pares += 1
                break
    probabilidad_par = (pares / intentos)*100
    print(f'La probabilidad de tener una flush en una mano de {tamano_mano} bajarajas es {probabilidad_par}')
        

if __name__ == "__main__":
    tamano_mano = int(input('Cuantas barjas sera la mano?: '))
    intentos = int(input('Cuantos intentos para la simulacion?: '))
    main(tamano_mano, intentos)
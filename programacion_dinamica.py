import sys

def fibonacci_rescursivo(n):
    if n == 1 or n == 0:
        print('un paso')
        return 1 
    
    return fibonacci_rescursivo(n-1) + fibonacci_rescursivo(n-2)
    print('un paso')

def fibonacci_dinamico(n, memo = {}):
    if n == 1 or n == 0:
        print('un paso')
        return 1 
    
    try:
        return memo[n]
        print('un paso')
    except KeyError:
        resultado = fibonacci_dinamico(n -1, memo) + fibonacci_dinamico(n-2, memo)
        memo[n] = resultado
        print(f'memo: [{n}] = {resultado}')
        print('un paso')
        return resultado

if __name__ == "__main__":
    sys.setrecursionlimit(10003)
    n = int(input('Escoje un numero: '))
    res = fibonacci_dinamico(n)
    print(res)
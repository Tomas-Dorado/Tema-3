from Iterativo import determinante_iterativo
from Recursivo import determinante_recursivo


if __name__ == "__main__":
    matriz = [
        [5, 3, 1],
        [4, 11, 6],
        [7, 8, 9]
    ]
    print("Matriz:")
    for fila in matriz:
        print(fila)
    print("Determinante (recursivo):", determinante_recursivo(matriz))
    print("Determinante (iterativo):", determinante_iterativo(matriz))
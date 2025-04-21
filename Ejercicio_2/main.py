from Iterativo import determinante_iterativo
from Recursivo import determinante_recursivo


if __name__ == "__main__":
    matriz = [
        [2, 3, 1],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Determinante (recursivo):", determinante_recursivo(matriz))
    print("Determinante (iterativo):", determinante_iterativo(matriz))
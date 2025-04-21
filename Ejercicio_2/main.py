from Iterativo import determinante_iterativo

# Método recursivo para calcular el determinante de una matriz
def determinante_recursivo(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    determinante = 0
    for i in range(len(matriz)):
        submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
        determinante += ((-1) ** i) * matriz[0][i] * determinante_recursivo(submatriz)
    return determinante



# Ejemplo de uso
if __name__ == "__main__":
    matriz = [
        [2, 3, 1],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Determinante (recursivo):", determinante_recursivo(matriz))
    print("Determinante (iterativo):", determinante_iterativo(matriz))
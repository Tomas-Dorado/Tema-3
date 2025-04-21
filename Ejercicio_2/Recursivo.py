def determinante_recursivo(matriz):
    '''
    Calcula el determinante de una matriz cuadrada utilizando un método recursivo.'''
    
    if len(matriz) == 1:
        return matriz[0][0]
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    determinante = 0
    for i in range(len(matriz)):
        submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
        determinante += ((-1) ** i) * matriz[0][i] * determinante_recursivo(submatriz)
    return determinante
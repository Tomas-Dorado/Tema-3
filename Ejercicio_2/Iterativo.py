def determinante_iterativo(matriz):
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("Este método solo funciona para matrices 3x3.")
    
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    
    return (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)
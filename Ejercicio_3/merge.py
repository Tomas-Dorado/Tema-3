def mergesort(lista, clave, descendente=False):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio], clave, descendente)
    derecha = mergesort(lista[medio:], clave, descendente)
    return merge(izquierda, derecha, clave, descendente)

def merge(izquierda, derecha, clave, descendente):
    resultado = []
    while izquierda and derecha:
        if (izquierda[0][clave] > derecha[0][clave] if descendente else izquierda[0][clave] < derecha[0][clave]):
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    resultado.extend(izquierda if izquierda else derecha)
    return resultado
from Polinomio import PolinomioMagico


def Laznador():
    p1 = PolinomioMagico({3: 4, 2: 3, 0: 2})  # 4x^3 + 3x^2 + 2
    p2 = PolinomioMagico({2:4, 1: 1, 0: 1})        # x + 1

    print("Polinomio 1:", p1)
    print("Polinomio 2:", p2)

    # Resta
    resta = p1.restar(p2)
    print("Resta:", resta)

    # División
    cociente, residuo = p1.dividir(p2)
    print("Cociente:", cociente)
    print("Residuo:", residuo)

    # Eliminar término
    p1.eliminar_termino(2)
    print("Polinomio 1 después de eliminar x^2:", p1)

    # Verificar término
    existe = p1.existe_termino(3)
    print("¿Existe el término x^3 en Polinomio 1?", existe)
    
Laznador()
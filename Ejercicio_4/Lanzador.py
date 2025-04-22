from Polinomio import PolinomioMagico


def lanzador():
    p1 = PolinomioMagico({3: 4, 2: 3, 0: 2})  # 4x^3 + 3x^2 + 2
    dicc= {}
    while True:
        exponente = int(input("Ingrese el exponente del término a agregar (o -1 para salir): "))
        if exponente == -1:
            break
        else: 
            numero = int(input("Ingrese el coeficiente del término a agregar : "))
            dicc[exponente] = numero
    p2 = PolinomioMagico(dicc) 

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
    n= int(input("Ingrese el exponente del término a eliminar en el polinomio 1: "))
    p1.eliminar_termino(n)
    print("Polinomio 1 después de eliminar x^2:", p1)

    # Verificar término
    existe = p1.existe_termino(2)
    print("¿Existe el término x^3 en Polinomio 1?", existe)
    
lanzador()
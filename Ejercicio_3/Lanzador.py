from merge import mergesort

def lanzador():
    naves = [
        {"nombre": "Cometa Veloz", "longitud": 120, "tripulantes": 10, "pasajeros": 50},
        {"nombre": "Titán del Cosmos", "longitud": 200, "tripulantes": 15, "pasajeros": 100},
        {"nombre": "GX-1 Explorer", "longitud": 90, "tripulantes": 5, "pasajeros": 6},
        {"nombre": "GX-2 Voyager", "longitud": 110, "tripulantes": 8, "pasajeros": 10},
        {"nombre": "Cometa Veloz", "longitud": 150, "tripulantes": 12, "pasajeros": 80},
        {"nombre": "Nebulosa Andrómeda", "longitud": 180, "tripulantes": 20, "pasajeros": 120},
        {"nombre": "Aurora Cósmica", "longitud": 130, "tripulantes": 7, "pasajeros": 40},
        {"nombre": "Nebulosa Andrómeda", "longitud": 200, "tripulantes": 30, "pasajeros": 60},
    ]
    
    # Ordenar la lista de naves por nombre ascendente y longitud descendente
    naves_ordenadas = mergesort(naves, "longitud", descendente=True)
    naves_ordenadas = mergesort(naves_ordenadas, "nombre")

    # Mostrar información de "Cometa Veloz" y "Titán del Cosmos"
    info_cometa_titan = [nave for nave in naves if nave["nombre"] in ["Cometa Veloz", "Titán del Cosmos"]]

    # Determinar las cinco naves con mayor cantidad de pasajeros
    top_5_pasajeros = mergesort(naves, "pasajeros", descendente=True)[:5]

    # Determinar la nave que requiere la mayor cantidad de tripulación
    nave_mayor_tripulacion = max(naves, key=lambda x: x["tripulantes"])

    # Mostrar todas las naves cuyo nombre comience con "GX"
    naves_gx = [nave for nave in naves if nave["nombre"].startswith("GX")]

    # Listar todas las naves que pueden llevar seis o más pasajeros
    naves_seis_pasajeros = [nave for nave in naves if nave["pasajeros"] >= 6]

    # Mostrar información de la nave más pequeña y la más grande
    nave_mas_pequena = min(naves, key=lambda x: x["longitud"])
    nave_mas_grande = max(naves, key=lambda x: x["longitud"])
    
    print("Naves ordenadas por nombre ascendente y longitud descendente:")
    for nave in naves_ordenadas:
        print(nave)

    print("\nInformación de 'Cometa Veloz' y 'Titán del Cosmos':")
    for nave in info_cometa_titan:
        print(nave)

    print("\nLas cinco naves con mayor cantidad de pasajeros:")
    for nave in top_5_pasajeros:
        print(nave)

    print("\nLa nave que requiere la mayor cantidad de tripulación:")
    print(nave_mayor_tripulacion)

    print("\nNaves cuyo nombre comienza con 'GX':")
    for nave in naves_gx:
        print(nave)

    print("\nNaves que pueden llevar seis o más pasajeros:")
    for nave in naves_seis_pasajeros:
        print(nave)

    print("\nLa nave más pequeña:")
    print(nave_mas_pequena)

    print("\nLa nave más grande:")
    print(nave_mas_grande)

lanzador()

import os
import subprocess
from menu import menu

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            subprocess.run(["python", os.path.join("Ejercicio_1", "main.py")])
        elif opcion == 2:
            subprocess.run(["python", os.path.join("Ej2", "main.py")])
        elif opcion == 3:
            print("Ejercicio 3 no implementado.")
        elif opcion == 4:
            print("Ejercicio 4 no implementado.")
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

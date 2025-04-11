from Game import HanoiGame

def main():
    # Pedir al usuario el número de discos
    num_disks = int(input("Introduce el número de discos: "))

    # Ejecutar el juego
    game = HanoiGame(num_disks)
    game.run()

if __name__ == "__main__":
    main()
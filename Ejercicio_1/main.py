import pygame
import time

# Configuración de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
FPS = 60

# Clase Nodo para representar cada piedra
class Nodo:
    def __init__(self, size):
        self.size = size
        self.next = None

# Clase Torre para representar cada columna
class Torre:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stack = None
        self.height = 0

    def push(self, size):
        new_node = Nodo(size)
        new_node.next = self.stack
        self.stack = new_node
        self.height += 1

    def pop(self):
        if self.stack is None:
            return None
        size = self.stack.size
        self.stack = self.stack.next
        self.height -= 1
        return size

    def draw(self, screen):
        # Dibuja la torre
        pygame.draw.rect(screen, BLACK, (self.x - 10, self.y - 200, 20, 400))
        # Dibuja las piedras
        current = self.stack
        offset = 0
        while current:
            width = current.size * 10
            pygame.draw.rect(screen, BLUE, (self.x - width // 2, self.y + 200 - offset - 20, width, 20))
            current = current.next
            offset += 20

# Clase Hanoi para manejar la lógica del juego
class Hanoi:
    def __init__(self, num_piedras):
        self.num_piedras = num_piedras
        self.torres = [Torre(200, HEIGHT // 2), Torre(400, HEIGHT // 2), Torre(600, HEIGHT // 2)]
        for size in range(num_piedras, 0, -1):
            self.torres[0].push(size)
        self.moves = []

    def solve(self, n, source, target, auxiliary):
        if n == 1:
            self.moves.append((source, target))
            return
        self.solve(n - 1, source, auxiliary, target)
        self.moves.append((source, target))
        self.solve(n - 1, auxiliary, target, source)

    def execute_moves(self, screen):
        for move in self.moves:
            source, target = move
            size = self.torres[source].pop()
            self.torres[target].push(size)
            self.draw(screen)
            pygame.display.flip()
            time.sleep(0.5)

    def draw(self, screen):
        screen.fill(WHITE)
        for torre in self.torres:
            torre.draw(screen)

# Inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Torre de Hanói")
clock = pygame.time.Clock()

# Configuración inicial
num_piedras = 5
hanoi = Hanoi(num_piedras)
hanoi.solve(num_piedras, 0, 2, 1)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hanoi.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

    # Ejecutar los movimientos una vez
    hanoi.execute_moves(screen)
    running = False

pygame.quit()
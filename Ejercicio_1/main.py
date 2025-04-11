import pygame
import sys
import time

# Clase para representar un disco


# Clase para representar una torre
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.disks = []

    def add_disk(self, disk):
        self.disks.append(disk)

    def remove_disk(self):
        return self.disks.pop() if self.disks else None

    def draw(self, screen):
        # Dibuja la torre
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 5, self.y - 200, 10, 200))
        # Dibuja los discos
        for i, disk in enumerate(reversed(self.disks)):
            disk_x = self.x - disk.width // 2
            disk_y = self.y - 20 * (i + 1)
            pygame.draw.rect(screen, disk.color, (disk_x, disk_y, disk.width, 20))

# Clase principal para resolver y visualizar el problema
class HanoiGame:
    def __init__(self, num_disks):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Torres de Hanói")
        self.clock = pygame.time.Clock()
        self.num_disks = num_disks
        self.towers = [
            Tower(200, 300),
            Tower(400, 300),
            Tower(600, 300)
        ]
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]
        self.init_disks()

    def init_disks(self):
        for i in range(self.num_disks, 0, -1):
            width = i * 20
            color = self.colors[i % len(self.colors)]
            self.towers[0].add_disk(Disk(width, color))

    def draw(self):
        self.screen.fill((255, 255, 255))
        for tower in self.towers:
            tower.draw(self.screen)
        pygame.display.flip()

    def move_disk(self, source, target):
        disk = self.towers[source].remove_disk()
        self.towers[target].add_disk(disk)
        self.draw()
        time.sleep(0.5)

    def solve_hanoi(self, n, source, target, auxiliary):
        if n == 1:
            self.move_disk(source, target)
            return
        self.solve_hanoi(n - 1, source, auxiliary, target)
        self.move_disk(source, target)
        self.solve_hanoi(n - 1, auxiliary, target, source)

    def run(self):
        self.draw()
        time.sleep(1)
        self.solve_hanoi(self.num_disks, 0, 2, 1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

# Número de discos
num_disks = 4

# Ejecutar el juego
game = HanoiGame(num_disks)
game.run()
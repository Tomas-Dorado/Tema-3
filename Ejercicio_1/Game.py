import pygame
import sys
import time
from Torre import Torre
from Nodo import Disco  


# Clase principal para resolver y visualizar el problema
class HanoiGame:
    
    def __init__(self, num_disks):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Torres de Hanói")
        self.clock = pygame.time.Clock()
        self.num_disks = num_disks
        
        self.towers = [
            Torre(200, 300),
            Torre(400, 300),
            Torre(600, 300)
        ]
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]
        self.init_disks()
        self.move_count = 0  # Contador de movimientos

    def init_disks(self):
        for i in range(self.num_disks, 0, -1):
            width = i * 20
            color = self.colors[i % len(self.colors)]
            self.towers[0].add_disk(Disco(width, color))
            self.draw()
    def draw(self):
        self.screen.fill((255, 255, 255))
        for tower in self.towers:
            tower.draw(self.screen)
        self.display_move_count()  # Mostrar el contador de movimientos
        pygame.display.flip()
        
        
    def display_move_count(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Movimientos: {self.move_count}", True, (0, 0, 0))
        self.screen.blit(text, (10, 10))

    def move_disk(self, source, target):
        disk = self.towers[source].remove_disk()
        self.towers[target].add_disk(disk)
        self.move_count += 1  # Incrementar el contador de movimientos
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
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
        sys.exit()
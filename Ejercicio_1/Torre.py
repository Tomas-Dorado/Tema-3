import pygame

class Torre:
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
            
    def __str__(self):
        return f"Torre(x={self.x}, y={self.y}, disks={self.disks})"
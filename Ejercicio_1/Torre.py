import pygame

class Torre:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.disks = []

    def add_disk(self, disk):
        if self.disks and self.disks[-1].width < disk.width:
            raise ValueError("No se puede colocar un disco más grande sobre uno más pequeño.")
        self.disks.append(disk)

    def remove_disk(self):
        if not self.disks:
            raise ValueError("No hay discos para remover.")
        return self.disks.pop()

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 5, self.y - 150, 10, 150))
        for i, disk in enumerate(self.disks):  # Iterate normally to reverse the order
            disk_x = self.x - disk.width // 2
            disk_y = self.y - 20 * (i + 1)
            pygame.draw.rect(screen, disk.color, (disk_x, disk_y, disk.width, 20))
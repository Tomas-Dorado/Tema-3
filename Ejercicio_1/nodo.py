#la clase Disco es el nodo de nuestro programa.

class Disco:
    def __init__(self, width, color):
        self.width = width
        self.color = color
        
    def __str__(self):
        return f"Disco(width={self.width}, color={self.color})"
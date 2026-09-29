import pygame

class vhs:
    p = pygame.Vector2(0, 0)
    graphic = pygame.image.load("Images/vhs.png")
    rect = pygame.Rect(0, 0, 16, 16)
    points = 1

    def __init__(self, p):
        self.p = p
        self.rect = pygame.Rect(p.x, p.y, 16, 16)

    def draw(self):
        return self.graphic
    
    def collect(self, hud):
        hud.score += self.points
        

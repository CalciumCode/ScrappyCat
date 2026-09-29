import pygame

class hud:
    screen = pygame.display
    hfont = None
    score = 0
    icon = pygame.image.load("Images/hud-s.png")

    def __init__(self, screen):
        self.screen = screen 
        self.hfont = pygame.font.Font("pixel_operator/PixelOperator-Bold.ttf", 36)


    def draw(self, b):
        1
        text_surface = self.hfont.render("Film: {}/{}".format(self.score, 23), True, (0, 0, 0))
        self.screen.blit(text_surface, (5, 0))
        self.screen.blit(self.icon,(3, b[1] - self.icon.get_height() - 5))
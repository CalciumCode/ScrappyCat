import pygame

class camera:
    p = pygame.Vector2()
    tp = pygame.Vector2()
    w = 0
    h = 0

    def __init__(self, pos, targpos, w, h):
        self.p = pos
        self.tp = targpos
        self.w = w
        self.h = h
    
    def update(self, tpos):
        self.p = tpos.xy - pygame.Vector2(.5 * self.w, .5*self.h)

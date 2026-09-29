import player
import vhs
import pygame

platforms = []
scratchposts = []
vhss = []
plr = None

def generatelevel():
    plr = player.player(pygame.Vector2(0, 0))
    platforms = [
        pygame.Rect(-600, -500, 400, 1250),     
        pygame.Rect(-200, 550, 2000, 200),    
        pygame.Rect(100, 400, 250, 20),  
        pygame.Rect(450, 300, 150, 20),    
        pygame.Rect(1000, 300, 500, 250),    
        pygame.Rect(1500, 225, 250, 250),    
        pygame.Rect(1750, 250, 500, 250),    
        pygame.Rect(1850, 150, 250, 20),    
        pygame.Rect(2200, 150, 250, 500),    
        pygame.Rect(2450, 300, 300, 250),    
        pygame.Rect(2750, -350, 150, 250),    
        pygame.Rect(2550, -500, 50, 50),    
        pygame.Rect(2900, -100, 1000, 250),    
        pygame.Rect(3900, -900, 500, 1500),    
        pygame.Rect(3050, -400, 50, 50),    
        pygame.Rect(3200, -500, 50, 50),    
        pygame.Rect(3400, -600, 50, 50),    
        pygame.Rect(3700, -500, 50, 50),    
        pygame.Rect(3800, -800, 50, 100),    
        pygame.Rect(4400, -1400, 500, 3000),
        pygame.Rect(3500, -1400, 850, 200),
        pygame.Rect(4000, -1500, 250, 20),  
        pygame.Rect(4500, -1600, 250, 20),  
        pygame.Rect(4200, -1900, 250, 20),  
        pygame.Rect(4650, -2000, 250, 20),  
    ]
    scratchposts = [
        pygame.Rect(450, 320, 150, 230),
        pygame.Rect(2750, -100, 150, 600),
        pygame.Rect(2550, -450, 50, 350), 
        pygame.Rect(2850, -350, 50, 350), 
        pygame.Rect(3900, -750, 50, 350), 
        pygame.Rect(4400, -1400, 50, 500),
        pygame.Rect(4430, -1900, 20, 150),
    ]
    vhss = [
        vhs.vhs(pygame.Vector2(150, 520)),
        vhs.vhs(pygame.Vector2(200, 520)),
        vhs.vhs(pygame.Vector2(250, 520)),
        vhs.vhs(pygame.Vector2(200, 370)),
        vhs.vhs(pygame.Vector2(250, 370)),
        vhs.vhs(pygame.Vector2(300, 370)),
        vhs.vhs(pygame.Vector2(475, 270)),
        vhs.vhs(pygame.Vector2(525, 270)),
        vhs.vhs(pygame.Vector2(575, 270)),
        vhs.vhs(pygame.Vector2(1900, 120)),
        vhs.vhs(pygame.Vector2(1950, 120)),
        vhs.vhs(pygame.Vector2(2000, 120)),
        vhs.vhs(pygame.Vector2(2562, -530)),
        vhs.vhs(pygame.Vector2(3062, -430)),
        vhs.vhs(pygame.Vector2(3212, -530)),
        vhs.vhs(pygame.Vector2(3412, -630)),
        vhs.vhs(pygame.Vector2(3712, -530)),
        vhs.vhs(pygame.Vector2(3812, -830)),
        vhs.vhs(pygame.Vector2(4600, -1630)),
        vhs.vhs(pygame.Vector2(4650, -1630)),
        vhs.vhs(pygame.Vector2(4300, -1930)),
        vhs.vhs(pygame.Vector2(4350, -1930)),
        vhs.vhs(pygame.Vector2(4775, -2030)),
        ]
    return (plr, platforms, vhss, scratchposts)



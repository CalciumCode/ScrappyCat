import pygame

class player:
    h = 10
    spd = 6
    jh = 3
    plyr_rect = pygame.Rect(380, 100, 32, 48) 
    grnd_rect = pygame.Rect(380, 100, 32, 48) 
    wall_rect = pygame.Rect(380, 100, 32, 32) 
    ceil_rect = pygame.Rect(380, 100, 32, 48) 
    p = pygame.Vector2(0, 0)
    hv = pygame.Vector2(0, 0)
    vv = pygame.Vector2(0, 0)
    g = pygame.Vector2(0, .8)
    jf = pygame.Vector2(0, -15)
    df = pygame.Vector2(12, -7)

    jumping = False
    grounded = False
    climbing = False
    facingRight = True

    acceleration = .2
    friction = .4
    maxspeed = 6
    maxfall = 18
    climbspeed = 2

    dashes = 1
    sc = 48
    sp = {
        "IDLE": pygame.image.load("Images/s-idle00.png"),
        "WALK0": pygame.image.load("Images/s-walk00.png"),
        "WALK1": pygame.image.load("Images/s-walk01.png"),
        "WALK2": pygame.image.load("Images/s-walk02.png"),
        "WALK3": pygame.image.load("Images/s-walk03.png"),        
        "CLIMB0": pygame.image.load("Images/s-climb00.png"),
        "CLIMB1": pygame.image.load("Images/s-climb01.png"),
        "CLIMB2": pygame.image.load("Images/s-climb02.png"),
        "JUMP": pygame.image.load("Images/s-jump00.png"),
        "AIR": pygame.image.load("Images/s-jump01.png"),
        "FALL": pygame.image.load("Images/s-jump02.png"),
    }
    graphic = sp["IDLE"]

    def __init__(self, p):
        self.p = p

    def update(self):
        self.animation()
        if self.grounded or self.climbing: 
            self.jumping = False
            self.dashes = 1      
        elif self.vv.y < self.maxfall:
            self.vv += self.g        
        self.plyr_rect.center = self.p
        self.grnd_rect.center = self.p + (pygame.Vector2(0, 20))
        self.ceil_rect.center = self.p +- (pygame.Vector2(0, 20))
        if self.facingRight:
            self.wall_rect.center = self.p + (pygame.Vector2(16, 0))
        else:
            self.wall_rect.center = self.p - (pygame.Vector2(16, 0))

    def movestep(self):
        self.p += self.hv + self.vv

    def jump(self):
        if self.grounded or self.climbing:
            self.vv += self.jf
            self.jumping = True
            self.grounded = False
            self.climbing = False
        elif self.dashes > 0 and not self.jumping:
            self.dive();
    
    jc = -3
    def jumpCancel(self):
        if self.jumping and self.vv.y < self.jc:
            self.vv = pygame.Vector2(0, self.jc)
        self.jumping = False
    
    def dive(self):
        self.vv = pygame.Vector2(0, self.df.y)
        if self.facingRight:
            self.hv += pygame.Vector2(self.df.x, 0)
        if not self.facingRight:
            self.hv += pygame.Vector2(-self.df.x, 0)
        self.dashes -= 1
    
    def accelerate(self, dir):
        if not dir * self.hv.x >= 0:
            self.decelerate()
            return

        if self.hv.magnitude() < self.maxspeed:
            self.hv += dir * pygame.math.Vector2(1, 0) * self.acceleration
        if self.hv.magnitude() > self.maxspeed:
            self.decelerate()

    def decelerate(self):
        self.hv = pygame.Vector2.move_towards(self.hv, pygame.math.Vector2(0,0), self.friction)

    def climb(self, dir):
        self.jumping = False
        if self.facingRight:
            self.vv = dir * pygame.math.Vector2(0, -1) * self.climbspeed
        if not self.facingRight:
            self.vv = -dir * pygame.math.Vector2(0, -1) * self.climbspeed

    def draw(self):
        if self.facingRight:
            return pygame.transform.scale(self.graphic, (self.sc, self.sc))
        else:
            return pygame.transform.scale(pygame.transform.flip(self.graphic, True, False), (self.sc, self.sc))
        ##pygame.draw.rect(screen, (255,0,0), self.player_rect)
        ##pygame.draw.rect(screen, (0,255,0), self.ground_rect)
    
    animclock = 0
    def animation(self):
        spd = self.hv.magnitude()
        if spd > 0.1:
            self.facingRight = self.hv.x > 0

        if self.climbing:
            if self.vv.y < 0:
                self.animclock += .1
                if self.animclock < 1:
                    self.graphic = self.sp["CLIMB0"]
                elif self.animclock < 2:
                    self.graphic = self.sp["CLIMB1"]
                elif self.animclock < 3:
                    self.graphic = self.sp["CLIMB2"]
                else:
                    self.animclock = 0
            else:
                self.graphic = self.sp["CLIMB0"]
            return
        
        if self.grounded:
            if spd < .3:
                self.graphic = self.sp["IDLE"]
                self.animclock = 0
            else:
                self.animclock += .2
                if self.animclock < 1:
                    self.graphic = self.sp["WALK0"]
                elif self.animclock < 2:
                    self.graphic = self.sp["WALK1"]
                elif self.animclock < 3:
                    self.graphic = self.sp["WALK2"]
                elif self.animclock < 4:
                    self.graphic = self.sp["WALK3"]
                else:
                    self.animclock = 0
        else:
            if self.vv.y < -2:
                self.graphic = self.sp["JUMP"]
            elif self.vv.y < 2:
                 self.graphic = self.sp["AIR"]
            else :
                 self.graphic = self.sp["FALL"]
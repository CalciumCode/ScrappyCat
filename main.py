import pygame
import lvl
import camera
import sys
import hud
import asyncio

async def main():
    pygame.init()

    WIDTH, HEIGHT = 640, 360
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Scrappy Cat")
    clock = pygame.time.Clock()

    # Colors
    BACKGROUND = (149, 157, 178)
    Floor = (84, 97, 117)
    Scratch = (255, 223, 0)   

    h = hud.hud(screen)
    o = lvl.generatelevel()
    plr = o[0]
    platforms = o[1]
    vhss = o[2]
    scratchposts = o[3]
    cam = camera.camera(pygame.Vector2(.5 * WIDTH, .5 * HEIGHT), plr.p, WIDTH, HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if plr.climbing:
                plr.climb(1)
            else:
                plr.accelerate(1)
        elif keys[pygame.K_LEFT]:
            if plr.climbing:
                plr.climb(-1)
            else:
                plr.accelerate(-1)
        elif plr.climbing:
            plr.climb(0)

        if not keys[pygame .K_LEFT] and not keys[pygame.K_RIGHT]:
            plr.decelerate()

        if keys[pygame.K_SPACE]:
            plr.jump()
        else:
            plr.jumpCancel()
   
        plr.update()    
        c = False
        for sc in scratchposts:
            if plr.wall_rect.colliderect(sc):
                c = True
                if plr.hv.x > 0:  
                    plr.hv = pygame.Vector2()
                    plr.p = pygame.Vector2(sc.left - (.5 * plr.plyr_rect.width), plr.p.y)
                    plr.climbing = True
                if plr.hv.x < 0:  
                    plr.hv = pygame.Vector2()
                    plr.p = pygame.Vector2(sc.right + (.5 * plr.plyr_rect.width), plr.p.y)
                    plr.climbing = True
        if not c:
            plr.climbing = False
        g = False
        for p in platforms:
            if plr.wall_rect.colliderect(p):
                if plr.hv.x > 0:  
                    plr.hv = pygame.Vector2()
                    plr.p = pygame.Vector2(p.left - (.5 * plr.plyr_rect.width), plr.p.y)
                if plr.hv.x < 0:  
                    plr.hv = pygame.Vector2()
                    plr.p = pygame.Vector2(p.right + (.5 * plr.plyr_rect.width), plr.p.y)
            if plr.grnd_rect.colliderect(p):
                g = True
                if plr.vv.y > 0:  
                    plr.vv = pygame.Vector2()
                    plr.p = pygame.Vector2(plr.p.x, p.top - (.5 * plr.plyr_rect.height))
                    plr.grounded = True
            if plr.ceil_rect.colliderect(p):
                if plr.vv.y < 0:  
                    plr.vv = pygame.Vector2()
                    plr.p = pygame.Vector2(plr.p.x, p.bottom + (.5 * plr.plyr_rect.height))
        if not g:
            plr.grounded = False
        plr.movestep()
        for v in vhss[:]:
            if plr.plyr_rect.colliderect(v):
                v.collect(h)
                vhss.remove(v)

        screen.fill(BACKGROUND)
        cam.update(plr.p)
        for p in platforms:
            pygame.draw.rect(screen, Floor, p.move(-cam.p))
        for s in scratchposts:
            pygame.draw.rect(screen, Scratch, s.move(-cam.p))
        for v in vhss:
            screen.blit(v.draw(),  v.p - cam.p)
        hsc = .5 * plr.sc
        screen.blit(plr.draw(), (plr.p - (hsc, hsc))- cam.p)
        h.draw((WIDTH, HEIGHT))
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)
    pygame.quit()
    sys.exit()
asyncio.run(main())
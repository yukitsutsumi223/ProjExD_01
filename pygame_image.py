import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True, False), bg_img]
    tmr = 0
    cnt = 0
    i = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        
       
        x = tmr%3200
        tmr += 1
        if tmr % 20 == 1:    
            cnt += 1
            kk_t = cnt % 2
        screen.blit(bg_imgs[0], [-x, 0])
        screen.blit(bg_imgs[1], [1600-x, 0])
        screen.blit(bg_imgs[2], [3200-x, 0])
        screen.blit(kk_imgs[kk_t], [300, 200])
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
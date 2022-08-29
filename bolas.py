from random import randint
import pygame as pg

class Bola:
    def __init__(self, x, y, w=25, h=25, color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

        self.vx = 0
        self.vy = 0

    def velocidad(self, vx, vy):
        self.vx = vx
        self.vy = vy

#Se indica en qué tamaño de pantalla se mueve y se define el rebote
    def mover(self, xmax, ymax):
        self.x += self.vx
        self.y += self.vy

        if self.x >= xmax or self.x <= 0 - self.w:
            self.vx *= -1
        
        if self.y >= ymax or self.y <= 0 - self.h:
            self.vy *= -1
    

pg.init()

pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("Bolitas rebotando")

bola = Bola(400, 300, color=(255,255,255))
bola.velocidad(1, 1)
bola2 = Bola(400, 300, 35, 35, color=(0, 255, 0))
bola2.velocidad(randint(-10, 10), randint(-10, 10))
bola3 = Bola(randint(300, 800), randint(200, 600), 15, 15, color=(255, 0, 0))
bola3.velocidad(randint(1, 2), randint(2, 3))


game_over = False
while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
        
#Color del fondo de pantalla y las bolas se mueven dentro de la pantalla    
    pantalla_principal.fill((0, 125, 255))
    bola.mover(800, 600)
    bola2.mover(800, 600)
    bola3.mover(800, 600)

#Imprime las bolas en la pantalla y su movimiento    
    pg.draw.rect(pantalla_principal, bola.color, (bola.x, bola.y, bola.w, bola.h))
    pg.draw.rect(pantalla_principal, bola2.color, (bola2.x, bola2.y, bola2.w, bola2.h))
    pg.draw.rect(pantalla_principal, bola3.color, (bola3.x, bola3.y, bola3.w, bola3.h))
    pg.display.flip()


pg.quit()
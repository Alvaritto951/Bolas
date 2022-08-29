import pygame as pg
import random

cantidad = random.randint(2,50)


class Cuadrao:
    def __init__(self, w=25, h=25, color = (255, 255, 255)):
        self.x = random.randint(0,800-h)
        self.y = random.randint(0,600-w)
        self.w = w
        self.h = h
        self.color = color

        self.vx = 1
        self.vy = 1

    def velocidad(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def mover(self, xmax, ymax):
        self.x += self.vx
        self.y += self.vy

        if self.x >= xmax or self.x <= 0 - self.w:
            self.vx *= -1
        
        if self.y >= ymax or self.y <= 0 - self.h:
            self.vy *= -1 
    
    def dibujar(self, donde):
        pg.draw.rect(donde, self.color, (self.x, self.y, self.w, self.h))

pg.init()

pantalla_principal = pg.display.set_mode((800, 600))

pg.display.set_caption("Bolitas rebotando")

cuadraos=[]
cuadrao_velocidad=[]

                                            # creador lista de objetos
for i in range(cantidad):
    lado = random.randint(5, 50)
    cuadrao = Cuadrao(h= lado,w = lado, color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    cuadrao.velocidad(random.randint(-5, 5), random.randint(-5, 5))
    cuadraos.append(cuadrao)

game_over = False
while not game_over:
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0, 0, 255))


                                             #Imprime los orectangulos en pantalla y movimiento()
    for j in range(random.randint(1, 10)):
        cuadraos[j].dibujar(pantalla_principal)
        cuadraos[j].mover(800, 600)

    #Mejor hacerlo de esta manera, ya que es lo que más se utiliza en Python
    for cuadrao in cuadraos:
        cuadrao.dibujar(pantalla_principal)
        cuadrao.mover(800, 600)

    pg.display.flip()
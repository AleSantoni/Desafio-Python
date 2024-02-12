import pygame
import random
import math
from pygame import mixer
import io


#inicializa pygame
pygame.init()

""" Creamos el tamaño de la pantalla del juego """
pantalla=pygame.display.set_mode((1000,800))

# Titulo e icono de la ventana
pygame.display.set_caption("Invacion Espacial")
icono=pygame.image.load("ovni.png")
fondo=pygame.image.load("fondo.jpg")
pygame.display.set_icon(icono)


# agregar musica
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)




# variable jugador
img_jugador=pygame.image.load("astronave.png")
img_jugador=pygame.transform.scale(img_jugador,(64,64))
jugador_x=468
jugador_y=650
# variable que va a manejar el movimiento del jugador
jugador_x_cambio=0

#variable enemigo


img_enemigo=[]

enemigo_x=[]
enemigo_y=[]
# variable que va a manejar el movimiento del jugador
enemigo_x_cambio=[]
enemigo_y_cambio=[]
cantidad_enemigos=8

for i in range(cantidad_enemigos):
    enemigo=pygame.image.load("enemigo.png")
    enemigo=pygame.transform.scale(enemigo,(64,64))


    img_enemigo.append(enemigo)



    enemigo_x.append(random.randint(0,936))
    enemigo_y.append(random.randint(50,200))
    # variable que va a manejar el movimiento del jugador
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

# variable bala
bala=[]
img_bala=pygame.image.load("bala.png")

bala_x=0
bala_y=650
bala_x_cambio=0
bala_y_cambio=0.8
bala_visible=False

def fuente_bytes(fuente):
    # abre el archivo tif en modo lectura binaria
    with open (fuente, "rb") as f:
        # lee el contenido del archivo
        ttf_bytes = f.read()
        #crea un objeto bytes io con el contenido del archivo
    return io.BytesIO(ttf_bytes)

# variable para puntaje
puntaje=0
fuente_como_bytes= fuente_bytes("Transcorner.ttf")
fuente=pygame.font.Font(fuente_como_bytes("Transcorner.ttf"),32)
texto_x=10
texto_y=10

# Texto final del juego
fuente_final=pygame.font.Font(fuente_como_bytes,40)


def texto_final():
    mi_fuente_final=fuente_final.render("GAME OVER",True,(255,255,255))
    pantalla.blit(mi_fuente_final,(300,300))







def mostrar_puntaje(x,y):
    texto=fuente.render(f"Puntaje: {puntaje}",True,(255,255,255))
    pantalla.blit(texto,(x,y))



#funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible=True
    pantalla.blit(img_bala,(x+16,y+10))# ponemos la bala en pantalla

#funcion enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y))

# funcion detectar colisiones
def hay_colision(x1,y1,x2,y2):
    distancia=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
    if distancia<27:# 27 es el tamaño de la nave
        return True
    else:
        return False

#loop while para la ventana que se quede abierta hasta que el evento Quit se ejecute

se_ejecuta=True
while se_ejecuta:
    # vamos a cargar una imagen de fondo
    pantalla.blit(fondo,(0,0))


    for evento in pygame.event.get():
        # evento cerrar programa
        if evento.type==pygame.QUIT:
            se_ejecuta=False
        #evento presionar flechas
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_LEFT:
                jugador_x_cambio=-0.5
            if evento.key==pygame.K_RIGHT:
                jugador_x_cambio=0.5
            if evento.key==pygame.K_SPACE:
                sonido_bala=mixer.Sound("disparo.mp3").play()
                if not bala_visible:
                    bala_x=jugador_x

                bala_x=jugador_x
                disparar_bala(bala_x,bala_y)

        #evento soltar flechas
        if evento.type==pygame.KEYUP:
            if (evento.key==pygame.K_LEFT or evento.key==pygame.K_RIGHT  ):
                jugador_x_cambio=0

    #modificar la posicion del  jugador
    jugador_x+=jugador_x_cambio


    # limitar el movimiento del jugador
    if jugador_x<=0:
        jugador_x=0
    elif jugador_x>=936:

        jugador_x=936

    # movimiento bala
    if bala_y<=-64:
        bala_y=650
        bala_visible=False

    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y-=bala_y_cambio


    # modificar la posicion del  enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e]> 600:
            # Necesito sacar los enemigos de la pantalla
            for j in range(cantidad_enemigos):
                enemigo_y[j]=2000
            texto_final()
            break

        enemigo_x[e]+= enemigo_x_cambio[e]

        # limitar el movimiento del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 936:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]


         # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision=mixer.Sound("Golpe.mp3").play().set_volume(0.3)

            bala_y = 650
            bala_visible = False
            puntaje += 1

            enemigo_x[e] = random.randint(0, 936)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e],e)

    jugador(jugador_x,jugador_y)

    # mustro el puntaje
    mostrar_puntaje(texto_x,texto_y)

    #actualizar
    pygame.display.update()



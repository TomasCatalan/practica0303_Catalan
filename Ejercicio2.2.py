import pygame

pygame.init()
ventana = pygame.display.set_mode((1080,720))
pygame.display.set_caption("ejercicio 2.2")

# Crea el objeto pelota
ball = pygame.image.load("OBAMNA.png")

# Establece imagen de fondo
fondo = pygame.image.load("IraqBackground.png")
ventana.blit(fondo, (0,0))

# Transforma el tamaño del objeto ball
ball = pygame.transform.scale(ball, (100, 140))

# indica la velocidad de la pelota
speedball = [5,5]

# Pongo la pelota en el origen de coordenadas
ballrect = ball.get_rect()

# Lugar de inicio de la bola
ballrect.move_ip(0,0)

# Transforma el tamaño de la imagen de fondo
fondo = pygame.transform.scale(fondo, (1080, 720))

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Muevo la pelota
    ballrect = ballrect.move(speedball)
    
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speedball[0] = -speedball[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speedball[1] = -speedball[1]
    
    #establece el fondo como una imagen, fill evita trazado de la bola
    ventana.fill((0, 0, 0))
    ventana.blit(fondo, (0,0))

    # Dibujo la pelota
    ventana.blit(ball, ballrect)

    pygame.display.flip()
    pygame.time.Clock().tick(120)

pygame.quit()

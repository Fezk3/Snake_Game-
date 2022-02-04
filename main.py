import pygame
import time
import random

# inicia pygame
pygame.init()

# colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)

ancho, alto = 600, 400

display_juego = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake Game")

reloj = pygame.time.Clock()

snake_tam = 10
snake_vel = 15

fuente_mensaje = pygame.font.SysFont('Arial', 20)
fuente_puntaje = pygame.font.SysFont('Arial', 15)

# logica


def puntaje_actual(puntaje):
    texto = fuente_puntaje.render(f'Score: {str(puntaje)}', True, verde)
    display_juego.blit(texto, [0, 0])


def dibuja_snake(snake_tam, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(display_juego, blanco, [pixel[0], pixel[1], snake_tam, snake_tam])


def run_game():

    game_over = False
    game_close = False

    # posi inicial

    x = ancho / 2
    y = alto / 2

    x_vel = 0
    y_vel = 0

    snake_pixels = []
    snake_largo = 1

    # spawn de comida en posiciones random
    comida_x = round(random.randrange(0, ancho - snake_tam) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - snake_tam) / 10.0) * 10.0

    # loop del juego

    while not game_over:

        while game_close:
            display_juego.fill(negro)
            game_over_message = fuente_mensaje.render("Game Over!", True, rojo)
            display_juego.blit(game_over_message, [ancho/3, alto/3])
            puntaje_actual(snake_tam - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_vel = -snake_tam
                    y_vel = 0
                if event.key == pygame.K_RIGHT:
                    x_vel = snake_tam
                    y_vel = 0
                if event.key == pygame.K_UP:
                    x_vel = 0
                    y_vel = -snake_tam
                if event.key == pygame.K_DOWN:
                    x_vel = 0
                    y_vel = snake_tam

        if x >= ancho or x < 0 or y >= alto or y < 0:
            game_close = True

        x += x_vel
        y += y_vel

        # ventana del juego

        display_juego.fill(negro)
        pygame.draw.rect(display_juego, verde, [comida_x, comida_y, snake_tam, snake_tam])
        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_largo:
            del snake_pixels[0]

        # snake choca con sigo misma

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        dibuja_snake(snake_tam, snake_pixels)
        puntaje_actual(snake_largo - 1)
        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ancho - snake_tam) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - snake_tam) / 10.0) * 10.0
            snake_largo += 1

        reloj.tick(snake_vel)

    pygame.quit()
    quit()


run_game()

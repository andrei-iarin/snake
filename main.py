import pygame
import random

pygame.init()
screen_square = 720
pixel_width = 50
screen = pygame.display.set_mode([screen_square] * 2)
clock = pygame.time.Clock()
running = True

def generate_strating_position():
    position_range = (pixel_width // 2, screen_square - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]
def reset():
    target.center = generate_strating_position()
    snake_pixel.center = generate_strating_position()
    return [snake_pixel.copy()]
def isOutOfBounds():
    return snake_pixel.bottom > screen_square or snake_pixel.top < 0 or snake_pixel.left < 0 or snake_pixel.right > screen_square

snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_strating_position()
snake = [snake_pixel.copy()]
snake_diretion = (0, 0)
snake_lenght = 1

target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
target.center = generate_strating_position()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_diretion = (0, -pixel_width)
            if event.key == pygame.K_s:
                snake_diretion = (0, pixel_width)
            if event.key == pygame.K_a:
                snake_diretion = [-pixel_width, 0]
            if event.key == pygame.K_d:
                snake_diretion = [pixel_width, 0]

    screen.fill('black')
    
    if isOutOfBounds():
        snake = reset()
        snake_lenght = 1

    if snake_pixel.center == target.center:
        target.center = generate_strating_position()
        snake_lenght += 1
        snake.append(snake_pixel.copy())

    keys = pygame.key.get_pressed()
   

    for snake_part in snake:
        pygame.draw.rect(screen, 'green', snake_part)
    
    pygame.draw.rect(screen, 'red', target)
    
    snake_pixel.move_ip(snake_diretion)
    snake.append(snake_pixel.copy())
    snake = snake[-snake_lenght:]

    font = pygame.font.Font('freesansbold.ttf', 23)
    text = font.render('score: ' + str(snake_lenght), True, 'white')
    textRect = text.get_rect()
    textRect.center = (50, 20)
    screen.blit(text, textRect)
    pygame.display.flip()
    clock.tick(5)
pygame.quit()

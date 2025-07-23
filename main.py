import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catcher")

# Game variables
score = 0
font = pygame.font.SysFont(None, 55)

# Player
player_width = 100
player_height = 20
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 10

# Falling object
object_width = 30
object_height = 30
object_x = random.randint(0, SCREEN_WIDTH - object_width)
object_y = -object_height
object_speed = 5

# Game loop
running = True
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))

def draw_object(x, y):
    pygame.draw.rect(screen, RED, (x, y, object_width, object_height))

def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            player_x = event.pos[0] - (player_width // 2)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Boundaries for player
    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - player_width:
        player_x = SCREEN_WIDTH - player_width

    # Object falling
    object_y += object_speed
    if object_y > SCREEN_HEIGHT:
        object_y = -object_height
        object_x = random.randint(0, SCREEN_WIDTH - object_width)

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    object_rect = pygame.Rect(object_x, object_y, object_width, object_height)

    if player_rect.colliderect(object_rect):
        score += 1
        object_y = -object_height
        object_x = random.randint(0, SCREEN_WIDTH - object_width)

    # Drawing
    draw_player(player_x, player_y)
    draw_object(object_x, object_y)
    show_score()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

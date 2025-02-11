import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rolling Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball settings
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

BALL_BOUNCE_TO_X_AXIS_EVENT = pygame.USEREVENT + 1
BALL_BOUNCE_TO_Y_AXIS_EVENT = pygame.USEREVENT + 2

BOUNCE_BACK_TIME_IN_MS = 500

ball_bounce_to_x_axis_time = float('inf')
ball_bounce_to_y_axis_time = float('inf')


# Clock for controlling FPS
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)  # Clear screen
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hit_x_axis = 0 < pygame.time.get_ticks() - ball_bounce_to_y_axis_time < BOUNCE_BACK_TIME_IN_MS
    hit_y_axis = 0 < pygame.time.get_ticks() - ball_bounce_to_x_axis_time < BOUNCE_BACK_TIME_IN_MS
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not hit_x_axis:
        ball_x -= ball_speed_x
        ball_bounce_to_y_axis_time = float('inf')

    if keys[pygame.K_RIGHT] and not hit_x_axis:
        ball_x += ball_speed_x
        ball_bounce_to_y_axis_time = float('inf')

    if keys[pygame.K_UP] and not hit_y_axis:
        ball_y -= ball_speed_y
        ball_bounce_to_x_axis_time = float('inf')

    if keys[pygame.K_DOWN] and not hit_y_axis:
        ball_y += ball_speed_y
        ball_bounce_to_x_axis_time = float('inf')

    # Bounce ball off walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius > WIDTH:
        # pygame.time.set_timer(BALL_BOUNCE_TO_Y_AXIS_EVENT, 2000, loops=1)
        ball_bounce_to_y_axis_time = pygame.time.get_ticks()
        hit_x_axis = True
        x_dir = ball_x - ball_radius <= 0
        
    if ball_y - ball_radius <= 0 or ball_y + ball_radius > HEIGHT:
        # pygame.time.set_timer(BALL_BOUNCE_TO_X_AXIS_EVENT, 2000, loops=1)
        ball_bounce_to_x_axis_time = pygame.time.get_ticks()
        hit_y_axis = True
        y_dir = ball_y - ball_radius <= 0

    if hit_x_axis:
        ball_x = ball_x - ball_speed_x if not x_dir else ball_x + ball_speed_x

    if hit_y_axis:
        ball_y = ball_y - ball_speed_y if not y_dir else ball_y + ball_speed_y

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    # Refresh screen
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(60)

pygame.quit()

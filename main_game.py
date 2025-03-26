import pygame
import random
import subprocess

# Initialize Pygame and Sound
pygame.init()
pygame.mixer.init()  # Initialize the sound mixer

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BALL_RADIUS = 15
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7
BALL_SPEED = 5
BORDER_WIDTH = 5
FONT = pygame.font.Font(None, 50)

# Load Sounds
hit_sound = pygame.mixer.Sound("Data/data0.yds")  # Sound when ball hits a paddle
wall_sound = pygame.mixer.Sound("Data/data0.yds")  # Sound when ball hits top/bottom
score_sound = pygame.mixer.Sound("Data/data1.yds")  # Sound when a player scores

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Score Game")
icon = pygame.image.load("Data/icon.ico")
pygame.display.set_icon(icon)  # Set icon

# Paddles positions
paddle1_x, paddle1_y = 50, HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_x, paddle2_y = WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2

# Ball position
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

# Score
score1, score2 = 0, 0

running = True
clock = pygame.time.Clock()


def reset_ball():
    """ Resets the ball to a random Y position and plays score sound. """
    global ball_x, ball_y, ball_dx, ball_dy
    pygame.mixer.Sound.play(score_sound)  # Play goal sound
    ball_x = WIDTH // 2
    ball_y = random.randint(HEIGHT // 3, HEIGHT * 2 // 3)
    ball_dx = BALL_SPEED * random.choice([-1, 1])
    ball_dy = BALL_SPEED * random.choice([-1, 1])


while running:
    screen.fill(BLACK)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move paddle 1 (Left player: W/S keys)
    if keys[pygame.K_w] and paddle1_y > BORDER_WIDTH:
        paddle1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT - BORDER_WIDTH:
        paddle1_y += PADDLE_SPEED

    # Move paddle 2 (Right player: UP/DOWN keys)
    if keys[pygame.K_UP] and paddle2_y > BORDER_WIDTH:
        paddle2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT - BORDER_WIDTH:
        paddle2_y += PADDLE_SPEED

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top/bottom walls
    if ball_y - BALL_RADIUS <= BORDER_WIDTH or ball_y + BALL_RADIUS >= HEIGHT - BORDER_WIDTH:
        ball_dy *= -1
        pygame.mixer.Sound.play(wall_sound)  # Play wall bounce sound

    # Ball collision with paddles
    if (paddle1_x < ball_x - BALL_RADIUS < paddle1_x + PADDLE_WIDTH and paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT):
        ball_dx *= -1
        pygame.mixer.Sound.play(hit_sound)  # Play paddle hit sound

    if (paddle2_x < ball_x + BALL_RADIUS < paddle2_x + PADDLE_WIDTH and paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT):
        ball_dx *= -1
        pygame.mixer.Sound.play(hit_sound)  # Play paddle hit sound

    # Check for scoring
    if ball_x - BALL_RADIUS <= 0:  # Left player missed
        score2 += 1
        reset_ball()
    if ball_x + BALL_RADIUS >= WIDTH:  # Right player missed
        score1 += 1
        reset_ball()

    # Draw border
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT), BORDER_WIDTH)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    # Draw score
    score_text = FONT.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 30, 20))

    # Show "Back to Menu" when game ends
    if score1 == 5 or score2 == 5:
        screen.fill(BLACK)
        win_text = FONT.render(f"Player {'1' if score1 == 5 else '2'} Wins!", True, WHITE)
        screen.blit(win_text, (WIDTH // 2 - 120, HEIGHT // 2 - 50))
        back_text = FONT.render("Press ESC to return", True, WHITE)
        screen.blit(back_text, (WIDTH // 2 - 150, HEIGHT // 2 + 20))

        pygame.display.flip()

        # Wait for ESC key to return
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.quit()  # Instantly close the game window
                        pygame.quit()  # Shut down pygame
                        subprocess.run(["python", "main.py"])  # Open main.py
                        exit()  # Ensure the script stops running

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()

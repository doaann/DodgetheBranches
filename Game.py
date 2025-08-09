import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timberman Clone")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
GREEN = (34, 139, 34)
RED = (255, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

tree_width = int(WIDTH * 0.1)
tree_x = WIDTH // 2 - tree_width // 2

branch_length = int(WIDTH * 0.22)
branch_height = 110
branch_thickness = 25

player_width = int(WIDTH * 0.08)
player_height = 55
player_side = "left"

score = 0
game_over = False

branches = []

for _ in range(8):
    r = random.random()
    if r < 0.35:
        branches.append("left")
    elif r < 0.7:
        branches.append("right")
    else:
        branches.append("none")

def draw_tree():
    pygame.draw.rect(win, BROWN, (tree_x, 0, tree_width, HEIGHT))
    for i, side in enumerate(branches):
        y = HEIGHT - (i + 1) * branch_height
        if side == "left":
            pygame.draw.rect(win, GREEN, (tree_x - branch_length, y + branch_height//3, branch_length, branch_thickness))
        elif side == "right":
            pygame.draw.rect(win, GREEN, (tree_x + tree_width, y + branch_height//3, branch_length, branch_thickness))

def draw_player():
    y = HEIGHT - player_height - 10
    x = tree_x - player_width if player_side == "left" else tree_x + tree_width
    pygame.draw.rect(win, RED, (x, y, player_width, player_height))

def move_player(side):
    global player_side, score, game_over
    if game_over:
        return
    player_side = side
    removed_branch = branches.pop(0)
    if removed_branch == player_side:
        game_over = True
    else:
        score += 1
        r = random.random()
        if r < 0.35:
            branches.append("left")
        elif r < 0.7:
            branches.append("right")
        else:
            branches.append("none")

def draw_score():
    text = font.render(f"Score: {score}", True, BLACK)
    win.blit(text, (10, 50))

def draw_game_over():
    lines = [
        "GAME OVER!",
        "Press Left or Right to restart",
        "Press Q to quit"
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, RED)
        win.blit(text, (20, HEIGHT // 3 + i * 60))

def reset_game():
    global score, game_over, player_side, branches
    score = 0
    game_over = False
    player_side = "left"
    branches.clear()
    for _ in range(8):
        r = random.random()
        if r < 0.35:
            branches.append("left")
        elif r < 0.7:
            branches.append("right")
        else:
            branches.append("none")

def main():
    global game_over
    running = True

    while running:
        clock.tick(30)
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_LEFT:
                        move_player("left")
                    elif event.key == pygame.K_RIGHT:
                        move_player("right")
                else:
                    if event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        reset_game()

        draw_tree()
        draw_player()
        draw_score()

        if game_over:
            draw_game_over()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

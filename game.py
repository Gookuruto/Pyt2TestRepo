import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Kolory
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Tworzenie okna gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kółko i Krzyżyk")
screen.fill(BG_COLOR)

# Plansza
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Rysowanie linii na planszy
def draw_lines():
    # Pionowe linie
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Poziome linie
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Rysowanie znaków (kółko lub krzyżyk)
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'o':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'x':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

# Rysowanie planszy
def draw_board():
    draw_lines()
    draw_figures()

# Sprawdzenie zwycięstwa
def check_win(mark):
    # Sprawdzenie poziomo
    for row in range(BOARD_ROWS):
        if all(board[row][col] == mark for col in range(BOARD_COLS)):
            return True
    # Sprawdzenie pionowo
    for col in range(BOARD_COLS):
        if all(board[row][col] == mark for row in range(BOARD_ROWS)):
            return True
    # Sprawdzenie po skosie
    if all(board[i][i] == mark for i in range(BOARD_ROWS)) or all(board[i][BOARD_COLS - i - 1] == mark for i in range(BOARD_ROWS)):
        return True
    return False

# Sprawdzenie remisu
def check_draw():
    return all(board[row][col] != '' for row in range(BOARD_ROWS) for col in range(BOARD_COLS))

# Resetowanie gry
def reset_game():
    screen.fill(BG_COLOR)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = ''
    draw_board()

# Główna pętla gry
turn = 'x'
game_over = False
draw_board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = turn
                if check_win(turn):
                    print(f"{turn} wins!")
                    game_over = True
                elif check_draw():
                    print("It's a draw!")
                    game_over = True
                else:
                    turn = 'o' if turn == 'x' else 'x'
                draw_board()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
                turn = 'x'
                game_over = False
        if game_over:
            reset_game()
            game_over = False
            turn = 'x'

    pygame.display.update()

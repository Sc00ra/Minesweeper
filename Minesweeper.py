import pygame
import numpy as np
import random 


pygame.init()
width = 0
height = 0
num_bombs = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT = pygame.font.Font(None, 30)

def generate_board(height,width):
    return np.empty((height,width),dtype=str)

def generate_bombs(num_bombs):
    if num_bombs >= width * height:
        return ""
    board = generate_board(height,width)
    while num_bombs > 0:
        position_x = random.randint(0,width-1)
        position_y = random.randint(0,height-1)
        if board[position_y][position_x] != "X":
            board[position_y][position_x] = "X"
            num_bombs -= 1
    return board

def count_mines():
    board = generate_bombs(num_bombs)
    if isinstance(board,str):
        return "Hold up, that's a lot of bombs"
    count = 0
    for i in range(height):
        for j in range(width):
            if board[i][j] != "X":
                if i + 1 < height and board[i+1][j] == "X":
                    count += 1
                if i - 1 >= 0 and board[i-1][j] == "X":
                    count += 1
                if j + 1 < width and board[i][j+1] == "X":
                    count += 1 
                if j - 1 >= 0 and board[i][j-1] == "X":
                    count += 1 
                if i + 1 < height and j + 1 < width and board[i+1][j+1] == "X":
                    count += 1
                if i - 1 >= 0 and j - 1 >= 0 and board[i-1][j-1] == "X":
                    count += 1                
                if i - 1 >= 0 and j + 1 < width and board[i-1][j+1] == "X":
                    count += 1
                if i + 1 < height and j - 1 >= 0 and board[i+1][j-1] == "X":
                    count += 1
                board[i][j] = f"{count}"
                count = 0
            
    return board  

def get_input():
    global width,height,num_bombs
    screen = pygame.display.set_mode((500,250))
    clock = pygame.time.Clock()
    running = True
    input_activate = 0 
    input_fields = ["Height","Width","Number of bombs"]
    input_values = ["","",""]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_activate == 0:
                        width = int(input_values[0])
                    elif input_activate == 1:
                        height = int(input_values[1])
                    elif input_activate == 2:
                        num_bombs = int(input_values[2])
                        running = False
                    input_activate = (input_activate + 1) % 3
                elif event.key == pygame.K_BACKSPACE:
                    input_values[input_activate] = input_values[input_activate][:-1]
                else:
                    input_values[input_activate] += event.unicode
        screen.fill(WHITE)
        
        screen.blit(FONT.render("Enter a number and then click enter",True,GRAY),(50,25))

        for i, field in enumerate(input_fields):
            color = BLACK if i == input_activate else GRAY
            text_surface = FONT.render(field + " " + input_values[i],True,color)
            screen.blit(text_surface,(50,75 + 50*i))

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()



get_input()
print(count_mines())
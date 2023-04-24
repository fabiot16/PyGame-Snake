
import pygame
import time
import random

pygame.init()

# Colors 
background = (140,164,142)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
gold = (255,215,0)

# Relevant positions
x_limit = 800
y_limit = 600

# Block size

snake_block = 10

# Window config
dis = pygame.display.set_mode((x_limit,y_limit))
pygame.display.update()
pygame.display.set_caption("Snake")

# Timming config
clock = pygame.time.Clock()
snake_speed = 20

# Font
font_style = pygame.font.SysFont(None, 50)

# Message display
def endGameMessage():
    global score
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [50,100])
    mesg = font_style.render("Weak", True, red)
    dis.blit(mesg, [50, 150])
    
    mesg = font_style.render("Q-Quit   R-Repeat", True, red)
    dis.blit(mesg, [50, 300])

# Print score
def printScore(score):
    value = font_style.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0,0])

# Game loop

def gameLoop():
    global score
    score = 0
    x1 = 400
    y1 = 300
    body = []
    head = [[400,300]]
    game_over = False
    game_close = False
    direction = pygame.K_RIGHT
    snake_speed = 0

    # Menu
    wall_option = -1
    while wall_option < 0:
        dis.fill(black)
        value = font_style.render("Walls Menu:", True, white)
        dis.blit(value, [0,0])
        value = font_style.render("Without walls - Press N (Baby mode)", True, white)
        dis.blit(value, [0,50])
        value = font_style.render("With walls - Press Y (Grownup mode)", True, white)
        dis.blit(value, [0,100])
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        wall_option = 1
                        multiplier = 3
                    if event.key == pygame.K_n:
                        wall_option = 0
                        multiplier = 1
    
    while snake_speed == 0:
        dis.fill(black)
        value = font_style.render("Speed Menu:", True, white)
        dis.blit(value, [0,0])
        value = font_style.render("10 - Press 0 (Yawn mode)", True, white)
        dis.blit(value, [0,50])
        value = font_style.render("15 - Press 1 (Meh mode)", True, white)
        dis.blit(value, [0,100])
        value = font_style.render("20 - Press 2 (Ok mode)", True, white)
        dis.blit(value, [0,150])
        value = font_style.render("25 - Press 3 (Hmmm mode)", True, white)
        dis.blit(value, [0,200])
        value = font_style.render("30 - Press 4 (Getting serious mode)", True, white)
        dis.blit(value, [0,250])
        value = font_style.render("35 - Press 5 (Testosterone fueled machine mode)", True, white)
        dis.blit(value, [0,300])
        value = font_style.render("40 - Press 6 (Good luck mode)", True, white)
        dis.blit(value, [0,350])
        value = font_style.render("50 - Press 7 (Just don't)", True, white)
        dis.blit(value, [0,400])
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        snake_speed = 10
                        multiplier *= 1
                    if event.key == pygame.K_1:
                        snake_speed = 15
                        multiplier *= 1.5
                    if event.key == pygame.K_2:
                        snake_speed = 20
                        multiplier *= 2
                    if event.key == pygame.K_3:
                        snake_speed = 25
                        multiplier *= 2.5
                    if event.key == pygame.K_4:
                        snake_speed = 30
                        multiplier *= 3.5
                    if event.key == pygame.K_5:
                        snake_speed = 35
                        multiplier *= 4.5
                    if event.key == pygame.K_6:
                        snake_speed = 40
                        multiplier *= 6
                    if event.key == pygame.K_7:
                        snake_speed = 50
                        multiplier *= 10


    food_x = round(random.randrange(0, x_limit - snake_block) / 10) * 10
    food_y = round(random.randrange(0, y_limit - snake_block) / 10) * 10
    dis.fill(background)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    pygame.draw.rect(dis, gold, [food_x, food_y, snake_block, snake_block])
    pygame.display.update()

    while not game_over:
        while game_close == True:
            dis.fill(black)
            endGameMessage()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_over = False
                        game_close = False
                        score = 0
                        body = [[400,300]]
                        x1 = 400
                        y1 = 300

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != pygame.K_RIGHT:
                    direction = pygame.K_LEFT
                elif event.key == pygame.K_RIGHT and direction != pygame.K_LEFT:
                    direction = pygame.K_RIGHT
                elif event.key == pygame.K_UP and direction != pygame.K_DOWN:
                    direction = pygame.K_UP
                elif event.key == pygame.K_DOWN and direction != pygame.K_UP:
                    direction = pygame.K_DOWN
        
        if direction == pygame.K_LEFT:
            x1 -= 10
        elif direction == pygame.K_RIGHT:
            x1 += 10
        elif direction == pygame.K_UP:
            y1 -= 10
        elif direction == pygame.K_DOWN:
            y1 += 10
        new_position = [x1, y1]


        if new_position == [food_x, food_y]:
            food_x = round(random.randrange(0, x_limit - snake_block) / 10) * 10
            food_y = round(random.randrange(0, y_limit - snake_block) / 10) * 10
            body.append([food_x, food_y])
            score += snake_speed * multiplier
            score *= 1.1
            score = round(score)
            print("Ca bo")
            print(score)
        elif new_position != head:
            body.append(head)
            body.pop(0)
            head = new_position
            
        if (wall_option == 1 and (x1 < 0 or x1 >= 800 or y1 < 0 or y1 >= 600)) or new_position in body:
            game_close = True
        elif wall_option == 0:
            if x1 == 800:
                x1 = 0
            if x1 < 0:
                x1 == 800
            if y1 == 600:
                y1 = 0
            if y1 < 0:
                y1 = 600
        
        dis.fill(background)
        pygame.draw.rect(dis, black, [head[0], head[1], snake_block, snake_block])
        for pos in body:
            pygame.draw.rect(dis, black, [pos[0], pos[1], snake_block, snake_block])

        pygame.draw.rect(dis, gold, [food_x, food_y, snake_block, snake_block])
        printScore(score)
        pygame.display.update()

        clock.tick(snake_speed)
    # End game
    time.sleep(2)
    pygame.quit()
    quit()
gameLoop()
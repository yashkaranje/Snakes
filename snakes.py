import pygame
import time
import random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
dis_width = 600
dis_height = 400
snake_block = 10
snake_speed = 15

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def getFood():
    foodx = random.randrange(0, dis_width - snake_block)
    foody = random.randrange(0, dis_height- snake_block)
    return (foodx,foody)

def drawText(iptext):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(iptext, True, white)

    textRect = text.get_rect()
    textRect.center = (dis_width//2, dis_height//2)

    dis.blit(text, textRect)

def gameLoop():
    game_over = False
    x1 = dis_width // 2
    y1 = dis_height // 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    score = 0
    food = getFood()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(black)
        pygame.draw.rect(dis, green, [food[0], food[1], snake_block, snake_block])
        
        one_block = (x1,y1)
        snake_List.append(one_block)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == one_block:
                game_over = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        if x1 in list(range(int(food[0]), int(food[0]+snake_block)))  and y1 in list(range(int(food[1]), int(food[1]+snake_block))):
            score+=1
            while(True):
            	food = getFood()
            	for spos in snake_List:
            		if food == spos:
            			continue
            	break	

            Length_of_snake += 1

        clock.tick(snake_speed)

    dis.fill(black)
    drawText("Score : " + str(score))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()


gameLoop()
import pygame
import pygame_menu
import os
import random
import time

pygame.init()

MENU = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Racing game")
run = True
difficulty = 1

frameRate = pygame.time.Clock()

def set_difficulty(case, value):
    
    global difficulty
    difficulty = value
    print (difficulty)
    # Do the job here !
    pass
def genFrame(GAME, game_over):
    if game_over != True:
        pygame.draw.rect(GAME, (54, 54, 54), pygame.Rect(240, 0, 800, 720))
        pygame.draw.rect(GAME, (20, 110, 20), pygame.Rect(0, 0, 240, 720))
        pygame.draw.rect(GAME, (20, 110, 20), pygame.Rect(1040, 0, 240, 720))
        pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(625, 0, 10, 720))
        pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(645, 0, 10, 720))

def pause_menu(GAME, game_over, score):
    caption = 'Pause'
    menu=pygame_menu.Menu(caption, 690, 360,
    theme=pygame_menu.themes.THEME_SOLARIZED)
    if game_over:
        caption = 'Game over'
        dashboard = "Score " + str(score)
        menu.add.label(dashboard,
                    align=pygame_menu.locals.ALIGN_CENTER,
                    font_name = "arialblack",
                    font_color="red")


    menu.add.button('Restart', start_the_game,
                    align=pygame_menu.locals.ALIGN_CENTER,
                    font_name = "arialblack")
    menu.add.button('Back', open_menu,
                    align=pygame_menu.locals.ALIGN_CENTER,
                    font_name = "arialblack")
    
    menu.mainloop(GAME)

def start_the_game():
    game_over = False
    car = pygame.image.load("Assets\\car.png").convert()
    car = pygame.transform.scale(car, (64, 128))
    box = pygame.image.load("Assets\\box.png").convert()
    box = pygame.transform.scale(box, (64, 64))
    X = 608
    Y = -100
    box_x = random.uniform(350, 700)
    box_y = -100
    building_y = 0
    building_gap = random.uniform(100, 200)
    movement = 0
    run=True
    
    GAME = pygame.display.set_mode((1280, 720))
    line1 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(430, -100, 10, 64))
    line2 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(835, -100, 10, 64))
    leftColum = pygame.draw.rect(GAME, (168, 99, 71), pygame.Rect(0, building_y, 10, 64))
    rightColum = pygame.draw.rect(GAME, (168, 99, 71), pygame.Rect(1000, building_y + building_gap, 10, 64))
    score = 0
    left_color = random.uniform(100, 200)
    right_color = random.uniform(100, 200)

    while run:
        font = pygame.font.Font('freesansbold.ttf', 32)
        dashboard = "Score " + str(score)
        text = font.render(dashboard, True, (0, 128, 0), (0, 0, 0))
        textRect = text.get_rect()
        GAME.fill("Black")
        genFrame(GAME, game_over)
        line1 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(430, Y, 10, 64))
        line2 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(835, Y, 10, 64))
        leftColum = pygame.draw.rect(GAME, (168, 99, 71), pygame.Rect(0, building_y, 100, 700))
        rightColum = pygame.draw.rect(GAME, (168, 99, 71), pygame.Rect(1100, building_y + building_gap, 300, 600))
        pygame.draw.rect(GAME, (255, 255, 255), line1)
        pygame.draw.rect(GAME, (255, 255, 255), line2) 
        pygame.draw.rect(GAME, (left_color, 99, 71), leftColum)
        pygame.draw.rect(GAME, (right_color, 99, 71), rightColum)

        GAME.blit(car, (X, 570))
        GAME.blit(box, (box_x, box_y))
        GAME.blit(text, textRect)
        X+=1*movement
        Y+=1*difficulty
        box_y+=1*difficulty
        building_y+=1*difficulty
        
        if Y == 720:
            Y = -100
        if box_y > 720:
            box_y = random.uniform(-1000, -100)
            box_x = random.uniform(350, 700)
            score += 1
            font = pygame.font.Font('freesansbold.ttf', 32)
            dashboard = "Score " + str(score)
            text = font.render(dashboard, True, (0, 128, 0), (0, 0, 0))
            textRect = text.get_rect()
            GAME.blit(text, textRect)
            print("score ", score)
        if building_y > 820:
            building_y = -1000
            building_gap = random.uniform(-200, 200)
            left_color = random.uniform(100, 200)
            right_color = random.uniform(100, 200)    
        pygame.display.update()
        if ((box_y > 506 and box_y < 700) and ((X-64 < box_x) and ((X + 64) > box_x))):
            car = pygame.transform.rotate(car, 45)
            game_over = True
            genFrame(GAME, game_over)
            time.sleep(1)
            time.sleep(1)
            pause_menu(GAME, game_over, score)
            # run = False
            
        for event in pygame.event.get():
            
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    pause_menu(GAME, game_over, score)
                if (event.key == pygame.K_RIGHT):
                    movement = 0.5
                if (event.key == pygame.K_LEFT):
                    movement = -0.5
            if(event.type == pygame.KEYUP):
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
                    movement = 0

            pygame.display.flip()
            frameRate.tick(128)
    pass

def open_menu(MENU):
    run = False
    menu = pygame_menu.Menu('Welcome', 1280, 720,
                    theme=pygame_menu.themes.THEME_SOLARIZED)

    menu.add.text_input('Name :', default='KNU Forever!!!',
                    font_name = "arialblack")
    menu.add.selector('Difficulty :', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty, 
                    font_name = "arialblack")
    menu.add.button('Play', start_the_game,
                    font_name = "arialblack")
    menu.add.button('Quit', pygame_menu.events.EXIT,
                    font_name = "arialblack",
                    font_color="red")
    menu.mainloop(MENU)

open_menu(MENU)

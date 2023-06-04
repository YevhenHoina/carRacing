import pygame
import pygame_menu
import os
pygame.init()

MENU = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Racing game")
run = True
car = pygame.image.load("Assets\\car.png").convert()
car = pygame.transform.scale(car, (64, 128))

frameRate = pygame.time.Clock()

def set_difficulty(value, difficulty):
    # Do the job here !
    pass
def genFrame(GAME):
    pygame.draw.rect(GAME, (54, 54, 54), pygame.Rect(240, 0, 800, 720))
    pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(625, 0, 10, 720))
    pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(645, 0, 10, 720))
    
def start_the_game():
    X = 608
    Y = -100

    movement = 0
    run=True
    
    GAME = pygame.display.set_mode((1280, 720))
    line1 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(430, -100, 10, 64))
    line2 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(835, -100, 10, 64))
    line3 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(430, -475, 10, 64))
    line4 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(835, -475, 10, 64))
    
    while run:
        GAME.fill("Black")
        print("game is running!")
        genFrame(GAME)
        line1 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(430, Y, 10, 64))
        line2 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(835, Y, 10, 64))
        pygame.draw.rect(GAME, (255, 255, 255), line1)
        pygame.draw.rect(GAME, (255, 255, 255), line2)
        GAME.blit(car, (X, 570))
        X+=1*movement
        Y+=1
        if Y == 720:
            Y = -100
        pygame.display.update()

        for event in pygame.event.get():
            
            
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    menu=pygame_menu.Menu('Pause', 690, 360,
                    theme=pygame_menu.themes.THEME_SOLARIZED)
                    menu.add.button('Resume', start_the_game,
                                    align=pygame_menu.locals.ALIGN_CENTER,
                                    font_name = "arialblack")
                    menu.add.button('Back', open_menu,
                                    align=pygame_menu.locals.ALIGN_CENTER,
                                    font_name = "arialblack")
                    menu.mainloop(GAME)
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

def open_menu():
    run = False
    menu = pygame_menu.Menu('Welcome', 1280, 720,
                    theme=pygame_menu.themes.THEME_SOLARIZED)

    menu.add.text_input('Name :', default='KNU Forever!!!',
                    font_name = "arialblack")
    menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty, 
                    font_name = "arialblack")
    menu.add.button('Play', start_the_game,
                    font_name = "arialblack")
    menu.add.button('Quit', pygame_menu.events.EXIT,
                    font_name = "arialblack",
                    font_color="red")

    menu.mainloop(MENU)

open_menu()

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

def start_the_game():
    X = 608
    Y = 0
    run=True
    GAME = pygame.display.set_mode((1280, 720))
    pygame.draw.rect(GAME, (54, 54, 54), pygame.Rect(240, 0, 800, 720))
    pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(625, 0, 10, 720))
    pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(645, 0, 10, 720))
    pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(430, 0, 10, 64))
    pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(835, 0, 10, 64))
    line1 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(430, 0, 10, 64))
    line2 = pygame.draw.rect(GAME, (255, 255, 255), pygame.Rect(835, 0, 10, 64))

    while run:
        print("game is running!")
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

            Y+=1
            GAME.blit(car, (X, 570))
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

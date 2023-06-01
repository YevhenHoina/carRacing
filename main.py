import pygame
import pygame_menu
import os
pygame.init()

MENU = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Racing game")
run = True

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    while run:
        GAME = pygame.display.set_mode((1280, 720))
        print("game is running!")
    pass



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
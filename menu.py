import pygame
from pygame.locals import *
from helpers import *


def menu():
    import game

    def easyGame():
        game.game(EASY_MODE)

    def mediumGame():
        game.game(MEDIUM_MODE)

    def hardGame():
        game.game(HARD_MODE)

    pygame.display.quit()
    pygame.init()
    window = pygame.display.set_mode((900, 600))

    image = pygame.image.load('back.png').convert()
    title = pygame.font.SysFont('comicsansms', 100).render(
        'Chienese Checkers', True, (5, 8, 119))
    titleRect = title.get_rect()
    titleRect.center = (460, 120)

    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.blit(pygame.transform.scale(image, (900, 600)), (0, 0))
        window.blit(title, titleRect)

        button(window, "Easy", 225, 300, 100, 30, DARK_COLOR,
               LIGHT_COLOR, easyGame)

        button(window, "Medium", 400, 300, 100, 30, DARK_COLOR,
               LIGHT_COLOR, mediumGame)

        button(window, "Hard", 575, 300, 100, 30, DARK_COLOR,
               LIGHT_COLOR, hardGame)

        pygame.display.flip()

    pygame.quit()
    
if __name__ == '__main__':
    menu()
import pygame

LIGHT_COLOR = (202, 203, 213)
DARK_COLOR = (2, 6, 145)
EASY_MODE = 'EASY'
MEDIUM_MODE = 'MEDIUM'
HARD_MODE = 'HARD'

difficulty_settings = {
    EASY_MODE: {
        "title": "CHINESE-CHECKERS (Easy Mode)",
        "depth": 1,
    },

    MEDIUM_MODE: {
        "title": "CHINESE-CHECKERS (Medium Mode)",
        "depth": 2,
    },

    HARD_MODE: {
        "title": "CHINESE-CHECKERS (Hard Mode)",
        "depth": 3,
    }
}


def button(window, msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(window, ic, (x, y, w, h))

    pygame.draw.rect(window, ic, (x - 6, y - 6, w + 12, h + 12), 6, 20)
    font = pygame.font.SysFont("comicsansms", 20)
    textsurface = font.render(msg, True, "white")
    textRect = textsurface.get_rect()
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    window.blit(textsurface, textRect)


def message(text, windowWidth, windowHeight, text_size, col_color, window):
    t = pygame.font.SysFont(None, text_size).render(text, True, col_color)
    window.blit(t, (windowWidth, windowHeight))

# import pygame
# from pygame.locals import *

# LIGHT_COLOR = (202, 203, 213)
# DARK_COLOR = (2, 6, 145)
# EASY_MODE = 'EASY'
# MEDIUM_MODE = 'MEDIUM'
# HARD_MODE = 'HARD'

# def button(window, msg, x, y, w, h, ic, ac, action=None):
#     mouse = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     if x + w > mouse[0] > x and y + h > mouse[1] > y:
#         pygame.draw.rect(window, ac, (x, y, w, h))

#         if click[0] == 1 and action != None:
#             action()
#     else:
#         pygame.draw.rect(window, ic, (x, y, w, h))

#     pygame.draw.rect(window, ic, (x-6, y-6, w+12, h+12), 6, 20)
#     font = pygame.font.SysFont("comicsansms", 20)
#     textsurface = font.render(msg, True, "white")
#     textRect = textsurface.get_rect()
#     textRect.center = ((x + (w / 2)), (y + (h / 2)))
#     window.blit(textsurface, textRect)

# def message(text, windowWidth, windowHeight, text_size, col_color, window):
#     t = pygame.font.SysFont(None, text_size).render(text, True, col_color)
#     window.blit(t, (windowWidth, windowHeight))

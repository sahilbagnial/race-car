from .settings import *
from .colors import *


#   Returns objects of text
def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


#   Display Message ( text )
def display_msg(msg, size, color, text_x, text_y):
    font = pygame.font.SysFont("comicsansms", size)
    text_surf, text_rect = text_objects(msg, font, color)
    text_rect.center = (text_x, text_y)
    surface.blit(text_surf, text_rect)
    pygame.display.update()


#   Display Buttons
def button(msg, x, y, w, h, ic, ac, font_size, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(surface, ac, (x, y, w, h))

        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(surface, ic, (x, y, w, h))

    small_text = pygame.font.SysFont("comicsansms", font_size)
    text_surf, text_rect = text_objects(msg, small_text, black)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    surface.blit(text_surf, text_rect)


#   Draw Blocks
def block(block_x_list, block_y, block_w, block_h, color):
    for block_x in block_x_list:
        pygame.draw.rect(surface, color, (block_x, block_y, block_w, block_h))


#   Encrypt
def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])


# Getting High Score ( if exists )
def get_high_score():
    try:
        file_handler = open('sts.m41k')
        encrypted_score = file_handler.read()
        if encrypted_score == '':
            high_score = None
        else:
            decrypted = str_xor(encrypted_score, "YeahDudeWhatever#231231^*^&(**&)(")
            high_score = str(decrypted)
        file_handler.close()
    except:
        high_score = None

    return high_score
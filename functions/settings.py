import pygame

pygame.init()

crash_sound = pygame.mixer.Sound("assets/sounds/crash.wav")
window_width = 800
window_height = 600
surface = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Race Car by S^#!L")
car_obj = pygame.image.load("assets/img/racecar.png")
pygame.display.set_icon(car_obj)

import pygame
import random
import sys
import os
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
pygame.init()
info = pygame.display.Info()
WIDTH_WIN, HEIGHT_WIN = info.current_w * 100 // 125, info.current_h * 100 // 125
print(info.current_w, info.current_h)
print(WIDTH_WIN, HEIGHT_WIN)

screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
pygame.mouse.set_visible(False)

FPS = 60
clock = pygame.time.Clock()
rur = True
while rur:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            rur = False
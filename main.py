import os
import json
import random

import pygame

import config
import utils
from Shiro import engine


pygame.init()
pygame.display.set_caption(config.DISPLAY_CAPTION)

screen = pygame.display.set_mode(config.SCREEN_SIZE)
clock = pygame.time.Clock()

pygame.mixer.init()
song_finished = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(song_finished)
song_index = 0
pygame.mixer.music.load(config.SONG_FILES[song_index])
pygame.mixer.music.play(0)

background_image = engine.utils.load_image(config.BACKGROUND_IMAGE_FILE,
                                           size=config.SCREEN_SIZE)

cars = pygame.sprite.Group()
roads = utils.load_roads_from_file(path=config.ROADS_FILE)
spawners = utils.load_spawners_from_file(path=config.SPAWNERS_FILE,
                                         roads=roads,
                                         cars_sprite_group=cars)

debug = engine.debug.Debug(screen=screen, 
                           clock=clock, 
                           cars=cars, 
                           roads=roads,
                           mouse=True)

run = True

while run:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_LCTRL] and keys[pygame.K_d]:
                debug_mode = debug.debug
                debug.debug = not debug_mode

            elif keys[pygame.K_LCTRL] and keys[pygame.K_s]:
                song_index += 1
                if song_index >= len(config.SONG_FILES):
                    song_index = 0
                pygame.mixer.music.load(config.SONG_FILES[song_index])
                pygame.mixer.music.play(0)

            elif keys[pygame.K_LCTRL] and keys[pygame.K_p]:
                pygame.mixer.music.pause()

            elif keys[pygame.K_LCTRL] and keys[pygame.K_u]:
                pygame.mixer.music.unpause()

        elif event.type == song_finished:
            song_index += 1
            if song_index >= len(config.SONG_FILES):
                song_index = 0
            pygame.mixer.music.load(config.SONG_FILES[song_index])
            pygame.mixer.music.play(0)
            
    
    screen.blit(background_image, (0, 0))
    debug.update()
    cars.update(roads, screen)
    cars.draw(screen)
    for i in spawners:
        i.update()
    
    pygame.display.flip()
    clock.tick(config.FPS)

pygame.mixer.quit()
pygame.quit()

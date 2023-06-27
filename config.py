import os
from Shiro import engine


DISPLAY_CAPTION = 'Модель движения на круговой автомобильной развязке'
SCREEN_SIZE = 650, 650
FPS = 30

_current_folder = os.getcwd()
_data_folder = os.path.join(_current_folder, 'data')
ROADS_FILE = os.path.join(_data_folder, 'roads.json')
SPAWNERS_FILE = os.path.join(_data_folder, 'spawners.json')

_engine_images_folder = engine.config.images_folder
BACKGROUND_IMAGE_FILE = os.path.join(_engine_images_folder, 'background-ring-road.png')
CARS_IMAGE_FILE = os.path.join(_engine_images_folder, 'cars.png')

_engine_sounds_folder = engine.config.sounds_foler
SONG_FILES = [os.path.join(_engine_sounds_folder, i) for i in os.listdir(_engine_sounds_folder)]

SPAWNERS_DELAY_RANGE = 6, 15
CAR_SPPED_RANGE = 1, 2
CAR_SIZE = 18, 32

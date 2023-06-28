import os
from Shiro import engine


DISPLAY_CAPTION: str = 'Модель движения на круговой автомобильной развязке'
SCREEN_SIZE: tuple[int, int] = 650, 650
FPS: int = 30

_current_folder: str = os.getcwd()
_data_folder: str = os.path.join(_current_folder, 'data')
ROADS_FILE: str = os.path.join(_data_folder, 'roads.json')
SPAWNERS_FILE: str = os.path.join(_data_folder, 'spawners.json')

_engine_images_folder: str = engine.config.images_folder
BACKGROUND_IMAGE_FILE: str = os.path.join(_engine_images_folder, 'background-ring-road.png')
CARS_IMAGE_FILE: str = os.path.join(_engine_images_folder, 'cars.png')

_engine_sounds_folder: str = engine.config.sounds_foler
SONG_FILES: list[str] = [os.path.join(_engine_sounds_folder, i)
                         for i in os.listdir(_engine_sounds_folder)]

SPAWNERS_DELAY_RANGE: tuple[int, int] = 6, 15
CAR_SPPED_RANGE: tuple[int, int] = 1, 2
CAR_SIZE: tuple[int, int] = 19, 33

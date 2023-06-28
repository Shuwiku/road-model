import os
from Shiro.engine.utils.load_image import load_image


_cur_folder: str = os.getcwd()
_main_folder: str = os.path.join(_cur_folder, 'Shiro')
_engine_folder: str = os.path.join(_main_folder, 'engine')

images_folder: str = os.path.join(_engine_folder, 'images')
sounds_foler: str = os.path.join(_engine_folder, 'sounds')

engine_icon: str = os.path.join(images_folder, 'engine-icon.jpg')

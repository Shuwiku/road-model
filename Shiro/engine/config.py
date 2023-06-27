import os
from Shiro.engine.utils.load_image import load_image


_cur_folder = os.getcwd()
_main_folder = os.path.join(_cur_folder, 'Shiro')
_engine_folder = os.path.join(_main_folder, 'engine')

images_folder = os.path.join(_engine_folder, 'images')
sounds_foler = os.path.join(_engine_folder, 'sounds')

engine_icon = os.path.join(images_folder, 'engine-icon.jpg')

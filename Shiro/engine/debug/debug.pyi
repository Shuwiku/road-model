import pygame

from Shiro.engine.objects import road


class Debug:
    """Этот класс предназначен для 'дебага' игры.
    На деле он скорее просто выводит доступную информацию на экран."""

    def __init__(self,
                 screen: pygame.display,
                 car_sprites: pygame.sprite.Group = None,
                 clock: pygame.time.Clock = None,
                 debug: bool = False,
                 mouse_pos: bool = False,
                 roads_list: list[road.Road] = None,
                 sound_index: int = 0,
                 sounds_list: list[str] = None,
                 _font_distance: int = 16,
                 _font_file: str = None,
                 _font_size: int = 24,
                 _text_antialias: bool = True,
                 _text_backgrond_color: tuple[int, int, int] = (0, 0, 0),
                 _text_color: tuple[int, int, int] = (255, 0, 0)):
        """Инициализация нового объекта класса."""

    @property
    def screen(self):
        """Свойство класса.
        Возвращает экран, на который выводятся данные."""

    @screen.setter
    def screen(self,
               _screen: pygame.display):
        """Установщик свойства класса.
        Устанавливает экран, на который выводятся данные."""

    @property
    def car_sprites(self):
        """Свойство класса.
        Возвращает группу спрайтов автомобилей."""

    @car_sprites.setter
    def car_sprites(self,
                    _car_sprites: pygame.sprite.Group):
        """Установщик войства класса.
        Устанавливает группу спрайтов автомобилей."""

    @property
    def clock(self):
        """Свойство класса.
        Возвращает объект pygame.time.Clock"""

    @clock.setter
    def clock(self,
              _clock: pygame.time.Clock):
        """Установщик войства класса.
        Устанавливает объект pygame.time.Clock"""

    @property
    def debug(self):
        """Свойство класса.
        Возвращает, выводится ли информация на экран."""

    @debug.setter
    def debug(self,
              _debug: bool):
        """Установщик свойства класса.
        Устанавливает, выводится ли информация на экран."""

    @property
    def mouse_pos(self):
        """Свойство класса.
        Возвращает, выводятся ли координаты мыши на экран."""

    @mouse_pos.setter
    def mouse_pos(self,
                  _mouse_pos: bool):
        """Установщик свойства класса.
        Устанавливает, выводятся ли координаты мыши на экран."""

    @property
    def roads_list(self):
        """Свойство класса.
        Возвращает список дорог."""

    @roads_list.setter
    def roads_list(self,
                   _roads_list: list[road.Road]):
        """Установщик свойства класса.
        Устанавливает список дорог."""

    @property
    def sound_index(self):
        """Свойство класса.
        Возвращает индекс текущего звука в списке всех звуков."""

    @sound_index.setter
    def sound_index(self,
                    _sound_index: int):
        """Установщик свойства класса.
        Устанавливает индекс текущего звука в списке всех звуков."""

    @property
    def sounds_list(self):
        """Свойство класса.
        Возвращает список всех звуков."""

    @sounds_list.setter
    def sounds_list(self,
                    _sounds_list: list[str]):
        """Установщик свойства класса.
        Устанавливает список всех звуков."""

    def update(self):
        """Обновление экземпляра класса.
        Заставляет его выводить на экран все имеющиеся у него сведения."""

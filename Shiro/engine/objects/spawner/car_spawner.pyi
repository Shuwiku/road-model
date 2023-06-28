import pygame

from Shiro.engine.objects.road import Road


class CarSpawner:
    """Спавнер автомобилей.
    Создаёт автомобиль на дороге, к которой сам привязан.
    Имеет задержку перед созданием."""

    def __init__(self,
                 car_image_path: str,
                 car_size: list[int, int],
                 car_speed_range: list[int, int],
                 cars_sprite_group: pygame.sprite.Group,
                 delay: int,
                 road: Road):
        """Инициализация объекта класса"""

    def update(self):
        """Обновление объекта.
        Проверяет, пора ли создавать новый автомобиль, и,
        в случае, если время пришло, создаёт его."""

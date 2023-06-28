import pygame

from Shiro.engine.objects import road


class Car(pygame.sprite.Sprite):
    """Класс машины (автомобиля). Авто движется по дороге,
    а если конкретнее, то по её точкам."""

    def __init__(self,
                 car_image: pygame.Surface,
                 car_road: road.Road,
                 car_speed: int,
                 sprite_group: pygame.sprite.Group):
        """Инициализация нового объекта класса."""

    def update(self, 
               roads_list: list[road.Road],
               screen: pygame.display) -> None:
        """Обновление объекта класса. 
        Должно вызываться с помощью группы спрайтов."""


class CarVector(pygame.sprite.Sprite):
    """Вектор направления движения автомобиля.
    Это костыль, поэтому по нему не будет никакой документации."""

    def __init__(self,
                 width,
                 height,
                 start_pos,
                 end_pos):
        """Инициализация костыля."""

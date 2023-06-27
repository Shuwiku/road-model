import pygame

from Shiro.engine.objects import road


class Car(pygame.sprite.Sprite):
    """Класс машины (автомобиля). Авто движется по дороге,
    а если конкретнее, то по её точкам."""

    def __init__(self,
                 sprite_group: pygame.sprite.Group,
                 car_speed: int,
                 car_road: road.Road,
                 car_image: pygame.Surface):
        """Инициализация нового объекта класса."""

    def update(self, 
               roads_list: list[road.Road]) -> None:
        """Обновление объекта класса. 
        Должно вызываться с помощью группы спрайтов."""

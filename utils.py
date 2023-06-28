import json
import random

import pygame.sprite

import config
from Shiro import engine


def load_roads_from_file(path: str,
                         encoding: str = None):
    """Загрузить дороги из файла.
    Я не хотел пихать эту громоздкую хрень в основное тело программы,
    поэтому вынес сюда."""
    roads = []
    with open(path, mode='r', encoding=encoding) as f:
        data = json.load(f)
    for i in data.values():
        road_id = i.get('road-id')
        road_points = i.get('road-points')
        next_roads = i.get('next-roads')
        obj = engine.objects.road.Road(road_id=road_id, 
                                       road_points=road_points, 
                                       next_roads=next_roads)
        roads.append(obj)
    return roads


def load_spawners_from_file(cars_sprite_group: pygame.sprite.Group,
                            path: str,
                            roads: list[engine.objects.road.Road],
                            encoding: str = None):
    """Загрузить спавнеры из файла.
    Я не хотел пихать эту громоздкую хрень в основное тело программы,
    поэтому вынес сюда."""
    spawners = []
    with open(path, mode='r', encoding=encoding) as f:
        data = json.load(f)
    for i in data.values():
        road_id = i.get('road-id')
        road = [j for j in roads if j.road_id == road_id][0]
        delay = random.randint(*config.SPAWNERS_DELAY_RANGE)
        obj = engine.objects.spawner.CarSpawner(delay=delay,
                                                road=road,
                                                cars_sprite_group=cars_sprite_group,
                                                car_size=config.CAR_SIZE,
                                                car_speed_range=config.CAR_SPPED_RANGE,
                                                car_image_path=config.CARS_IMAGE_FILE)
        spawners.append(obj)
    return spawners

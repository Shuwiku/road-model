import random
import time

from Shiro.engine.objects import vehicle
from Shiro.engine.utils.load_image import load_cars_image


class CarSpawner:

    def __init__(self, car_image_path, car_size,  car_speed_range,
                 cars_sprite_group, delay, road):
        self._car_image_path = car_image_path
        self._car_size = car_size
        self._car_speed_range = car_speed_range
        self._cars_sprite_group = cars_sprite_group
        self._delay = delay
        self._road = road

        self._last_time_spawn = time.time() + delay // 2

    def update(self):
        current_time = time.time()

        if current_time - self._last_time_spawn >= self._delay:
            self._spawn_random()
            self._last_time_spawn = current_time

    def _spawn_random(self):
        speed = random.randint(*self._car_speed_range)
        image = random.choice(load_cars_image(self._car_image_path, self._car_size))
        vehicle.Car(car_image=image,
                    car_road=self._road,
                    car_speed=speed,
                    sprite_group=self._cars_sprite_group)

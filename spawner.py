import time
import random
from car import Car
from load_image import load_cars_image


def create_random_car(sprite_group, car_road, size):
    speed = random.randint(2, 4)
    image = random.choice(load_cars_image('images/cars.png', size))
    car = Car(sprite_group, speed, car_road, image)
    print('car spawned')


class VehicleSpawner:
    POSSIBLE_TYPES = ['car']

    def __init__(self, road, vehicle_types, vehicle_sizes):
        self._vehicle_types = vehicle_types
        self._vehicle_sizes = vehicle_sizes
        self._road = road

    def spawn_random(self, sprite_group):
        vehicle_type = random.choice(self._vehicle_types)
        data = {
            'car': (create_random_car, self._vehicle_sizes.get('car'))
        }
        result = data.get(vehicle_type)
        if result is None:
            print('result is None')
            return
        result[0](sprite_group, self._road, result[1])


class VehicleSpawnersList:

    def __init__(self, spawn_delay):
        self._spawners = []
        self._spawn_delay = spawn_delay
        self._last_spawn = time.time() + spawn_delay // 2

    @property
    def spawners(self):
        return self._spawners
    
    @spawners.setter
    def spawners(self, spawners_list):
        self._spawners = spawners_list

    def update(self, vehicle_sprite_group):
        current_time = time.time()
        print(current_time - self._last_spawn)
        if current_time - self._last_spawn >= self._spawn_delay:
            print('delay!')
            spawner = random.choice(self._spawners)
            spawner.spawn_random(vehicle_sprite_group)
            self._last_spawn = current_time

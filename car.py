import math
import random
import pygame


class Car(pygame.sprite.Sprite):

    def __init__(self, sprite_group, speed, road, image):
        super().__init__(sprite_group)
        self.sprite_group = sprite_group
        self.image0 = image
        self.image = image
        self.rect = self.image0.get_rect()
        self.rect.center = road.road_points[0]
        self._speed = speed
        self._road = road
        self._index_next_road_point = 1
        self._to_x, self._to_y = self._road.road_points[self._index_next_road_point]
        self._direction = pygame.math.Vector2((self._to_x, self._to_y)) - pygame.math.Vector2(self.rect.center)

    def update(self, screen, roads_list):
        self._triggers(roads_list)
        self._rotate()
        self._move()

    def _triggers(self, roads_list):
        x_range = range(self._to_x - self._speed, self._to_x + self._speed)
        y_range = range(self._to_y - self._speed, self._to_y + self._speed)
        x, y = self.rect.center
        if (x, y) == (self._to_x, self._to_y) or \
            (x in x_range and y in y_range):
            self._index_next_road_point += 1
        if self._index_next_road_point >= len(self._road.road_points):
            next_roads_id = self._road.next_roads
            if not bool(next_roads_id):
                self.kill()
                return
            self._road = roads_list.roads.get(random.choice(next_roads_id))
            self._index_next_road_point = 0
            self._to_x, self._to_y = self._road.road_points[0]
        else:
            self._to_x, self._to_y = self._road.road_points[self._index_next_road_point]
        self._direction = pygame.math.Vector2((self._to_x, self._to_y)) - pygame.math.Vector2(self.rect.center)


    # def _move(self):
    #     x0, y0 = self.rect.center
    #     x1, y1 = 0, 0
    #     if x0 != self._to_x:
    #         x1 = self._speed * (1 if x0 < self._to_x else -1)
    #     if y0 != self._to_y:
    #         y1 = self._speed * (1 if y0 < self._to_y else -1)
    #     self.rect.center = x0 + x1, y0 + y1

    def _move(self):
        pos = self._direction.normalize() * self._speed
        x, y = pygame.math.Vector2(self.rect.center)
        x += pos.x
        y += pos.y
        self.rect.center = round(x), round(y)

    def _rotate(self):
        x, y = self.rect.center
        ax, ay = self._to_x - x, self._to_y - y
        angle = math.degrees(-math.atan2(ay, ax)) - 90
        self.image = pygame.transform.rotate(self.image0, angle)
        self.rect = self.image.get_rect()
        self.rect.center = x, y


class CarsList:

    def __init__(self):
        self._cars = []

    @property
    def cars(self):
        return self._cars
    
    @cars.setter
    def cars(self, cars_list):
        self._cars = cars_list

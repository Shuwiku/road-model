import math
import random

import pygame


class Car(pygame.sprite.Sprite):

    def __init__(self, car_image, car_road, car_speed, sprite_group):
        super().__init__(sprite_group)

        self.image = car_image
        self._image0 = car_image
        self._road = car_road
        self._speed = car_speed
        self._speed0 = car_speed
        self._sprite_group = sprite_group

        self.rect = car_image.get_rect()
        self.rect.center = car_road.road_points[0]

        _vec_1 = pygame.math.Vector2(self.rect.center)
        _vec_2 = pygame.math.Vector2(car_road.road_points[1])
        self._direction = _vec_2 - _vec_1
        self._frozen_time = 0
        self._frozen_time_max = 180
        self._next_road_point_index = 1
        self._next_x, self._next_y = car_road.road_points[1]
        self._speed_step = 0.05
        self._vector: pygame.math.Vector2
        self._vector_lenght = 60
        _vec_3 = self._direction.normalize() * self._vector_lenght
        self._vector = pygame.math.Vector2(_vec_1 + _vec_3)

    def update(self, roads_list, screen):
        self._triggers(roads_list=roads_list)
        self._move(screen=screen)

    def _collide(self, screen):
        width, height = screen.get_size()
        vector = CarVector(width=width,
                           height=height,
                           start_pos=self.rect.center,
                           end_pos=self._vector)

        for i in self._sprite_group:

            if pygame.sprite.collide_mask(i, vector) and i.rect.center != self.rect.center:
                return True

        return False

    def _move(self, screen):
        pos = self._direction.normalize() * self._speed
        x0, y0 = pygame.math.Vector2(self.rect.center)
        x1, y1 = round(x0 + pos.x), round(y0 + pos.y)
        self.rect.center = x1, y1

        if self._collide(screen):
            self.rect.center = x0, y0
            self._frozen_time += 1

            if self._speed - self._speed_step >= 0:
                self._speed -= self._speed_step

        else:
            self._frozen_time = 0

            if self._speed + self._speed_step <= self._speed0:
                self._speed += self._speed_step

            else:
                self._speed = self._speed0

    def _rotate(self):
        x, y = self.rect.center
        ax, ay = self._next_x - x, self._next_y - y
        angle = math.degrees(-math.atan2(ay, ax)) - 90
        self.image = pygame.transform.rotate(self._image0, angle)
        self.rect = self.image.get_rect()
        self.rect.center = x, y

    def _triggers(self, roads_list):
        range_x = range(round(self._next_x - self._speed), 
                        round(self._next_x + self._speed))
        range_y = range(round(self._next_y - self._speed),
                        round(self._next_y + self._speed))
        x, y = self.rect.center

        if (x, y) == (self._next_x, self._next_y) or \
            (x in range_x and y in range_y):
            self._next_road_point_index += 1

        if self._next_road_point_index >= len(self._road.road_points):
            road_ids = self._road.next_roads

            if not bool(road_ids):
                self.kill()
                return

            road_id = random.choice(road_ids)
            self._road = None

            for i in roads_list:
                if i.road_id == road_id:
                    self._road = i
                    break

            self._next_road_point_index = 0
            self._next_x, self._next_y = self._road.road_points[0]
            self._rotate()

        else:
            pos = self._road.road_points[self._next_road_point_index]
            self._next_x, self._next_y = pos
            self._rotate()

        if self._frozen_time >= self._frozen_time_max:
            self.kill()

        _vec_1 = pygame.math.Vector2(self.rect.center)
        _vec_2 = pygame.math.Vector2((self._next_x, self._next_y))
        self._direction = _vec_2 - _vec_1
        _vec_3 = self._direction.normalize() * self._vector_lenght
        self._vector = pygame.math.Vector2(_vec_1 + _vec_3)


class CarVector(pygame.sprite.Sprite):

    def __init__(self, width, height, start_pos, end_pos):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = width // 2, height // 2

        pygame.draw.line(self.image, (100, 100, 200), start_pos, end_pos, 2)
        self.mask = pygame.mask.from_surface(self.image)

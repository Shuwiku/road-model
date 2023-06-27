import math
import random

import pygame


class Car(pygame.sprite.Sprite):

    def __init__(self, sprite_group, car_speed, car_road, car_image):
        super().__init__(sprite_group)

        self.rect = car_image.get_rect()
        self.rect.center = car_road.road_points[0]
        self.image = car_image
        # self.mask = pygame.mask.from_surface(car_image)

        self._sprite_group = sprite_group
        self._speed = car_speed
        self._road = car_road
        self._image0 = car_image
        self._next_road_point_index = 1
        self._next_x, self._next_y = car_road.road_points[1]
        dir_vec_1 = pygame.math.Vector2(car_road.road_points[1])
        dir_vec_2 = pygame.math.Vector2(self.rect.center)
        self._direction = dir_vec_1 - dir_vec_2
        self._vector_lenght = 60
        self._sleep_time = 0
        vec = self._direction.normalize() * self._vector_lenght
        self._vector = pygame.math.Vector2(dir_vec_2.x + vec.x, dir_vec_2.y + vec.y)

    def update(self, roads_list, screen):
        self._triggers(roads_list, screen)
        self._rotate()
        self._move(screen)
        if self._sleep_time >= 240:
            self.kill()

    def _is_collide(self, screen):
        a = CarVector(650 // 2, 650 // 2, self.rect.center, self._vector)
        for i in self._sprite_group:
            if pygame.sprite.collide_mask(i, a) and i.rect.center != self.rect.center:
                self._sleep_time += 1
                return True
        self._sleep_time = 0
        return False

    def _move(self, screen):
        pos = self._direction.normalize() * self._speed
        x0, y0 = pygame.math.Vector2(self.rect.center)
        x1, y1 = round(x0 + pos.x), round(y0 + pos.y)
        self.rect.center = x1, y1
        if self._is_collide(screen):
            self.rect.center = x0, y0

    def _rotate(self):
        x, y = self.rect.center
        ax, ay = self._next_x - x, self._next_y - y
        angle = math.degrees(-math.atan2(ay, ax)) - 90
        self.image = pygame.transform.rotate(self._image0, angle)
        self.rect = self.image.get_rect()
        self.rect.center = x, y

    def _triggers(self, roads_list, screen):
        range_x = range(self._next_x - self._speed, 
                        self._next_x + self._speed)
        range_y = range(self._next_y - self._speed,
                        self._next_y + self._speed)
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

        else:
            pos = self._road.road_points[self._next_road_point_index]
            self._next_x, self._next_y = pos

        dir_vec_1 = pygame.math.Vector2((self._next_x, self._next_y))
        dir_vec_2 = pygame.math.Vector2(self.rect.center)
        self._direction = dir_vec_1 - dir_vec_2

        vec = self._direction.normalize() * self._vector_lenght
        self._vector = pygame.math.Vector2(dir_vec_2.x + vec.x, dir_vec_2.y + vec.y)

        # vec = self._direction.normalize() * 50
        # vec = pygame.math.Vector2(dir_vec_2.x + vec.x, dir_vec_2.y + vec.y)
        # pygame.draw.line(screen, (0, 0, 255), dir_vec_2, vec, width=2)


class CarVector(pygame.sprite.Sprite):

    def __init__(self, x, y, s, e):
        super().__init__()
        self.image = pygame.Surface((650, 650))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = 650 // 2, 650 // 2
        pygame.draw.line(self.image, (100, 100, 200), s, e, 2)
        self.mask = pygame.mask.from_surface(self.image)

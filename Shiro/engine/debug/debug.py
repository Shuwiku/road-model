import pygame


class Debug:
    
    def __init__(self, screen, debug=False, cars=None, roads=None, music=None,
                 clock=None, mouse=False):
        self._screen = screen
        self._debug = debug
        self._cars = cars
        self._roads = roads
        self._music = music
        self._clock = clock
        self._mouse = mouse

        self._font_size = 24
        self._font_distance = 16
        self._font = pygame.font.Font(None, self._font_size)
        self._text_color = (225, 0, 0)
        self._text_antialias = True
        self._text_backgrond_color = (0, 0, 0)

    @property
    def screen(self):
        return self._screen
    
    @screen.setter
    def screen(self, _screen):
        self._screen = _screen

    @property
    def debug(self):
        return self._debug
    
    @debug.setter
    def debug(self, _debug):
        self._debug = _debug

    def update(self):
        if not self._debug:
            return
        x, y = 0, 0
        self._mode(x, y)
        y += self._font_distance
        if self._clock is not None:
            self._fps(x, y)
            y += self._font_distance
        if self._roads is not None:
            self._road_lines(x, y)
            y += self._font_distance
        if self._cars is not None:
            self._total_cars(x, y)
            y += self._font_distance
            self._car_hitboxes(x, y)
            y += self._font_distance
            self._car_vectors(x, y)
            y += self._font_distance
        if self._mouse:
            self._mouse_pos(x, y)
            y += self._font_distance

    def _mode(self, x, y):
        self.__blit('debug mode', x, y)

    def _fps(self, x, y):
        current_fps = self._clock.get_fps()
        self.__blit(f'fps: {current_fps:.2f}', x, y)

    def _total_cars(self, x, y):
        self.__blit(f'total cars: {len(self._cars)}', x, y)

    def _car_hitboxes(self, x, y):
        self.__blit('car hitboxes', x, y)
        for i in self._cars:
            pygame.draw.rect(self._screen, (255, 0, 0), i.rect, 2)

    def _car_vectors(self, x, y):
        self.__blit('car vectors', x, y)
        for i in self._cars:
            pygame.draw.line(self._screen, (255, 0, 125), i.rect.center, i._vector, 2)

    def _road_lines(self, x, y):
        self.__blit('road lines', x, y)
        for i in self._roads:
            road_id = i.road_id  # road id
            # font = pygame.font.Font(None, 20)
            points = i.road_points
            # pos = points[0]
            # text = font.render(road_id, 1, (255, 0, 0))
            # self._screen.blit(text, pos)
            for j in range(len(points) - 1):  # road points
                pygame.draw.line(self._screen, (0, 0, 255), points[j], points[j + 1], 3)
            next = i.next_roads  # next roads
            if next is None:
                continue
            for j in next:
                point = None
                for k in self._roads:
                    if k.road_id == j:
                        point = k.road_points[0]
                pygame.draw.line(self._screen, (0, 255, 0), points[-1], point, 3)
            self.__blit(road_id, *points[0])

    def _mouse_pos(self, x, y):
        pos = pygame.mouse.get_pos()
        self.__blit(f'mouse: {pos}', x, y)

    def __blit(self, text, x, y):
        text = self._font.render(text, self._text_antialias,
                                 self._text_color, self._text_backgrond_color)
        self._screen.blit(text, (x, y))

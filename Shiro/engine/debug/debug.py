import os

import pygame


class Debug:

    def __init__(self, screen, car_sprites=None, clock=None, debug=False,
                 mouse_pos=False, roads_list=None, sound_index=0, sounds_list=None,
                 _font_distance=16, _font_file=None, _font_size=24,  _text_antialias=True, 
                 _text_backgrond_color=(0, 0, 0), _text_color=(255, 0, 0)):
        self._screen = screen
        self._car_sprites = car_sprites
        self._clock = clock
        self._debug = debug
        self._mouse_pos = mouse_pos
        self._roads_list = roads_list
        self._sound_index = sound_index
        self._sounds_list = sounds_list

        self._font_distance = _font_distance
        self._font_file = _font_file
        self._font_size = _font_size
        self._text_antialias = _text_antialias
        self._text_backgrond_color = _text_backgrond_color
        self._text_color = _text_color

        self._font = pygame.font.Font(_font_file, self._font_size)

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, _screen):
        self._screen = _screen

    @property
    def car_sprites(self):
        return self._car_sprites

    @car_sprites.setter
    def car_sprites(self, _car_sprites):
        self._car_sprites = _car_sprites

    @property
    def clock(self):
        return self._clock

    @clock.setter
    def clock(self, _clock):
        self._clock = _clock

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, _debug):
        self._debug = _debug

    @property
    def mouse_pos(self):
        return self._mouse_pos

    @mouse_pos.setter
    def mouse_pos(self, _mouse_pos):
        self._mouse_pos = _mouse_pos

    @property
    def roads_list(self):
        return self._roads_list

    @roads_list.setter
    def roads_list(self, _roads_list):
        self._roads_list = _roads_list

    @property
    def sound_index(self):
        return self._sound_index

    @sound_index.setter
    def sound_index(self, _sound_index):
        self._sound_index = _sound_index

    @property
    def sounds_list(self):
        return self._sounds_list

    @sounds_list.setter
    def sounds_list(self, _sounds_list):
        self._sounds_list = _sounds_list

    def update(self):

        if not self._debug:
            return

        x, y = 0, 0
        self._display_debug_mode(x, y)
        y += self._font_distance
        
        if self.clock is not None:
            self._display_fps(x, y)
            y += self._font_distance

        if self._mouse_pos:
            self._display_mouse_pos(x, y)
            y += self._font_distance

        if self._roads_list is not None:
            self._draw_road_lines(x, y)
            y += self._font_distance

        if self._car_sprites is not None:
            self._display_total_cars(x, y)
            y += self._font_distance
            self._draw_car_hitboxes(x, y)
            y += self._font_distance
            self._draw_car_vectors(x, y)
            y += self._font_distance

        if self._sounds_list is not None:
            x, y = 0, self._screen.get_width() - self._font_distance
            self._display_sound_name(x, y)

    def _display_debug_mode(self, x, y):
        text = 'debug mode'
        self.__blit_text(text, x, y)

    def _display_fps(self, x, y):
        fps = self._clock.get_fps()
        text = f'fps: {fps:.2f}'
        self.__blit_text(text, x, y)

    def _display_mouse_pos(self, x, y):
        pos = pygame.mouse.get_pos()
        text = f'mouse: {pos}'
        self.__blit_text(text, x, y)

    def _display_total_cars(self, x, y):
        text = f'total cars: {len(self._car_sprites)}'
        self.__blit_text(text, x, y)

    def _display_sound_name(self, x, y):
        sound_file = self._sounds_list[self._sound_index]
        sound_name = os.path.basename(sound_file)
        text = f'[{self._sound_index + 1} / {len(self._sounds_list)}] {sound_name}'
        self.__blit_text(text, x, y)

    def _draw_road_lines(self, x, y):
        text = 'draw road lines'
        self.__blit_text(text, x, y)

        for i in self._roads_list:  # road points
            points = i.road_points

            for j in range(len(points) - 1):
                pygame.draw.line(self._screen, (0, 0, 255), points[j], points[j + 1], 3)

            next_roads = i.next_roads  # next roads

            if next_roads is None:
                continue

            for j in next_roads:
                point = None

                for k in self._roads_list:

                    if k.road_id == j:
                        point = k.road_points[0]
                        break

                pygame.draw.line(self._screen, (0, 255, 0), points[-1], point, 3)

            road_id = i.road_id  # road id
            self.__blit_text(road_id, *points[0])

    def _draw_car_hitboxes(self, x, y):
        text = 'draw car hitboxes'
        self.__blit_text(text, x, y)

        for i in self._car_sprites:
            pygame.draw.rect(self._screen, (255, 0, 0), i.rect, 2)

    def _draw_car_vectors(self, x, y):
        text = 'draw car vectors'
        self.__blit_text(text, x, y)

        for i in self._car_sprites:
            pygame.draw.line(self._screen, (255, 0, 125), i.rect.center, i._vector, 2)

    def __blit_text(self, text, x, y):
        text = self._font.render(text, self._text_antialias,
                                 self._text_color, self._text_backgrond_color)
        self._screen.blit(text, (x, y))

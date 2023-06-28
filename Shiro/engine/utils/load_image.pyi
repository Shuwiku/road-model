def load_image(path: str,
               colorkey: int | list[int, int] = None,
               size: list[int, int] = None):
    """Функция загрузки изображения в формат pygame.Surface"""


def load_cars_image(car_size: list[int, int],
                    path: str,
                    colorkey: int | list[int, int] = None,
                    count_x: int = 3,
                    count_y: int = 4):
    """Функция загрузки изображений автомобилей.
    В теории оно должно нормально кропать и грузить любые пачки
    изображений, но на практике не проверено."""

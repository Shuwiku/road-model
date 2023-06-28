import pygame


def load_image(path, colorkey=None, size=None):
    image = pygame.image.load(path)

    if size is not None:
        image = pygame.transform.scale(image, size)

    if colorkey is None:
        image = image.convert_alpha()

    else:
        image = image.convert()

        if colorkey == -1:
            colorkey = image.get_at((0, 0))

        image.set_colorkey(colorkey)

    return image


def load_cars_image(path, car_size, colorkey=None, count_x=3, count_y=4):
    full_image = load_image(path, colorkey)
    x0, y0 = full_image.get_size()
    x, y = 0, 0
    x_step, y_step = x0 // count_x, y0 // count_y
    ret = []

    for _ in range(count_y):

        for __ in range(count_x):

            image = pygame.Surface((x_step, y_step))
            crop = (x, y, x + x_step, y + y_step)
            image.blit(full_image, (0, 0), crop)
            image = pygame.transform.scale(image, car_size).convert()
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
            ret.append(image)
            x += x_step

        x = 0
        y += y_step

    return ret

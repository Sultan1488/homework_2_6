import math

pi = math.pi  # Число Пи. Примерно, равное 3.141592653589793


def calculate_sphere_volume(r):
    if type(r) == str:
        raise ValueError
    else:
        if r < 0:
            return 'Радиус сферы не может быть отрицательным'
        else:
            return 4 / 3 * pi * r ** 3

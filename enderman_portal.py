from dataclasses import dataclass
from math import tan, radians


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Coordinates:
    point: Point
    angle: float

    def __init__(self, x, y, angle):
        self.point = Point(x, y)
        self.angle = angle + 90  # change slope of the straight ordinate to abscissa


def find_portal(first_throw: Coordinates, second_throw: Coordinates) -> Point:
    # y = kx + b
    k1 = tan(radians(first_throw.angle))
    k2 = tan(radians(second_throw.angle))
    b1 = first_throw.point.y - k1 * first_throw.point.x
    b2 = second_throw.point.y - k2 * second_throw.point.x
    x = (b2 - b1) / (k1 - k2)
    y = k2 * x + b2
    return Point(x=x, y=y)

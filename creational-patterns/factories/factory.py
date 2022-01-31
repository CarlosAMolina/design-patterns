from enum import Enum
import math


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class PointBad:
    # Cartesian coordinates
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

    # Polar coordinates
    # Redeclaration for new coordinate type won't work 
    # def __init__(self, rho, theta):

    # Steps to add a new system violate the Open-Closed principle:
    # 1. Augment CoordinateSystem
    # 2. Change init method
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = a * cos(b)

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


class PointWithFactoryMethod:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod
    def new_cartesian_point(x, y):
        return PointWithFactoryMethod(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return PointWithFactoryMethod(rho * math.sin(theta), rho * math.cos(theta))


if __name__ == '__main__':
    p1 = PointBad(2, 3, CoordinateSystem.CARTESIAN)
    p2 = PointWithFactoryMethod.new_cartesian_point(1, 2)
    p3 = PointWithFactoryMethod.new_polar_point(5, 6)
    print(p1, p2, p3)

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


# Factory method

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

# Factory

class Point:

    def __init__(self, x=0, y=0):
        """
        We can set default values to the arguments and the 
        factory won't need to know how to use de init method.
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # The PointFactory can be a inner class of Point an use:
    # factory = PointFactory()


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        # Init a Point without worry about how to use the init method.
        p = Point()
        p.x = x
        p.y = y
        return p

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.sin(theta), rho * math.cos(theta))


if __name__ == '__main__':
    p1 = PointBad(2, 3, CoordinateSystem.CARTESIAN)
    p2 = PointWithFactoryMethod.new_cartesian_point(1, 2)
    p3 = PointWithFactoryMethod.new_polar_point(5, 6)
    p4 = PointFactory.new_cartesian_point(7, 8)
    p5 = PointFactory.new_polar_point(9, 10)
    print(p1, p2, p3, p4, p5)

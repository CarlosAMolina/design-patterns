from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ""


class Circle(Shape):
    def __init__(self, radius=0.0):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"A circle of radius {self.radius}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"A square with side {self.side}"


class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception("Cannot apply ColoredDecorator twice")
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f"{self.shape} has {self.transparency * 100.0}% transparency"


if __name__ == "__main__":
    circle = Circle(2)
    print(circle)

    red_circle = ColoredShape(circle, "red")  # Decorate the circle instance.
    print(red_circle)

    # ColoredShape doesn't have resize()
    # red_circle.resize(3)

    red_half_transparent_square = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_square)

    # nothing prevents double application
    print("The next line is going to raise an Exception")
    mixed = ColoredShape(ColoredShape(Circle(3), "red"), "blue")
    # If double application is not catched, we will have this result:
    # A circle of radius 3 has the color red has the color blue
    print(mixed)

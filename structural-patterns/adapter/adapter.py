# External library

class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x


def draw_point(p):
    print(".", end="")


# Our library

class Line:
    def __init__(self, start: Point, end: Point):
        self.end = end
        self.start = start


class Rectangle(list):
    """Represented as a list of lines."""

    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter(list):
    def __init__(self, line):
        super().__init__()
        print(
            f"\nGenerating points for line "
            f"[{line.start.x},{line.start.y}]→"
            f"[{line.end.x},{line.end.y}]"
        )


        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        if self._is_vertical_line(right, left):
            for y in range(top, bottom):
                self.append(Point(left, y))
        if self._is_horizontal_line(line):
            for x in range(left, right):
                self.append(Point(x, top))

    def _is_vertical_line(self, right: int, left: int) -> bool:
        return right - left == 0

    def _is_horizontal_line(self, line: Line) -> bool:
        return line.end.y - line.start.y == 0


class LineToPointAdapterCache:
    cache = {}

    def __init__(self, line):
        self.hash = hash(line)
        if self.hash in self.cache:
            return

        print(
            f"\nGenerating points for line "
            f"[{line.start.x},{line.start.y}]→"
            f"[{line.end.x},{line.end.y}]"
        )


        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        points = []

        if self._is_vertical_line(right, left):
            for y in range(top, bottom):
                points.append(Point(left, y))
        if self._is_horizontal_line(line):
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.hash] = points

    def _is_vertical_line(self, right: int, left: int) -> bool:
        return right - left == 0

    def _is_horizontal_line(self, line: Line) -> bool:
        return line.end.y - line.start.y == 0

    def __iter__(self):
        return iter(self.cache[self.hash])


def draw(rectangles):
    for index, rectangle in enumerate(rectangles, 1):
        print(f"\nRectangle {index}")
        for line in rectangle:
            adapter = LineToPointAdapter(line)
            for point in adapter:
                draw_point(point)

def draw_cache(rectangles):
    for index, rectangle in enumerate(rectangles, 1):
        print(f"\nRectangle {index}")
        for line in rectangle:
            adapter = LineToPointAdapterCache(line)
            for point in adapter:
                draw_point(point)




if __name__ == "__main__":
    rectangles = [Rectangle(1, 1, 10, 10), Rectangle(3, 3, 6, 6)]
    print("# Execution no caching")
    print("\n## Execution no caching. 1")
    draw(rectangles)
    print("\n## Execution no caching. 2")
    # All lines are generated again
    draw(rectangles)
    print("\n# Execution caching")
    print("\n## Execution caching. 1")
    draw_cache(rectangles)
    print("\n## Execution caching. 2")
    # All lines were generated previously, now the cache is used.
    draw_cache(rectangles)





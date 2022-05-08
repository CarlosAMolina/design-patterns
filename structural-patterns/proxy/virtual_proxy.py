class Bitmap:
    """The image is loaded despite it's used or not."""
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")


class LazyBitmap:
    """Avoid load the image if no draw."""
    def __init__(self, filename):
        self.filename = filename
        self.bitmap = None

    def draw(self):
        # Only loads the image in the first invocation.
        if not self.bitmap:
            self.bitmap = Bitmap(self.filename)
        self.bitmap.draw()


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")


if __name__ == "__main__":
    bmp = Bitmap("facepalm.jpg")
    draw_image(bmp)


    print()
    bmp = LazyBitmap("facepalm.jpg")
    draw_image(bmp)
    draw_image(bmp) # The image is not loaded twice.


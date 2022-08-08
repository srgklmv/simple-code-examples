class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = "".join(["*" * self.width + "\n" for _ in range(self.height)])
        return picture

    def get_amount_inside(self, shape):
        if shape.width > self.width:
            return 0
        vertical_fits = self.height // shape.height
        if self.width // shape.width >= 1:
            vertical_fits *= self.width // shape.width
        return vertical_fits


class Square(Rectangle):

    def __init__(self, side):
        self.width, self.height = side, side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width, self.height = side, side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

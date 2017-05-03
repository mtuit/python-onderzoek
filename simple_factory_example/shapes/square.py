from shapes.shape import Shape


class Square(Shape):

    def __init__(self, width=0):
        self.width = width

    def calculate_surface(self):
        return self.width * self.width

    def set_width(self, width):
        self.width = width

    def draw(self):
        print("Square")

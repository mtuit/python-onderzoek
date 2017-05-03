import math
from shapes.shape import Shape


class Circle(Shape):

    def __init__(self, diameter=0):
        self._diameter = diameter

    def calculate_surface(self):
        return math.pi * (self._diameter ** 2)

    def set_diameter(self, diameter):
        self._diameter = diameter

    def draw(self):
        print("Circle")

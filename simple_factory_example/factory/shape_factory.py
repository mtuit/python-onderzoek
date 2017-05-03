from shapes.circle import Circle
from shapes.square import Square


class ShapeFactory(object):

    @staticmethod
    def create_shape(type):
        if type == "Circle":
            return Circle()
        if type == "Square":
            return Square()
        else:
            raise TypeError("Shape {} is not known!".format(type))

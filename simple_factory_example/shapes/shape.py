import abc


class Shape(object):

    @abc.abstractmethod
    def calculate_surface(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass

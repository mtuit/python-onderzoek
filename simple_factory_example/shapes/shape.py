import abc


class Shape(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def calculate_surface(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass

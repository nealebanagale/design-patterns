#!/urs/bin/env/python3
from interfaces.shape_interface import Circle, Square


class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()
        if type == 'square':
            return Square()

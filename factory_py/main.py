#!/usr/bin/env/python3
from shape_factory import ShapeFactory


def main():
    factory = ShapeFactory()
    square = factory.getShape('square')
    square.draw()
    circle = factory.getShape('circle')
    circle.draw()



if __name__ == '__main__':
    main()

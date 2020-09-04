from model.abstract_factory import LargeRedSquareFactory, SmallBlueCircleFactory


def main():
    for factory in (SmallBlueCircleFactory(), LargeRedSquareFactory()):
        size = factory.set_size()
        size.size()
        color = factory.set_color()
        color.color()



if __name__ == '__main__':
    main()


# resources:
# https://refactoring.guru/design-patterns/abstract-factory/python/example#example-0
# https://sourcemaking.com/design_patterns/abstract_factory

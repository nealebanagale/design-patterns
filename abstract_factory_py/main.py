from furniture_factory import VictorianFurnitureFactory, ModernFurnitureFactory


def main():
    for factory in (VictorianFurnitureFactory(), ModernFurnitureFactory()):
        chair = factory.create_chair()
        coffe_table = factory.create_coffe_table()
        sofa = factory.create_sofa()

        chair.sitOn()
        coffe_table.putOn()
        sofa.sitOn()


if __name__ == '__main__':
    main()


# resources:
# https://refactoring.guru/design-patterns/abstract-factory/python/example#example-0
# https://sourcemaking.com/design_patterns/abstract_factory

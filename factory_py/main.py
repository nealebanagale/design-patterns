#!/usr/bin/env/python3
from logistics_factory import RoadLogistics, SeaLogistics


def main():
    # truck
    road_logistics = RoadLogistics()
    road_logistics.plan_delivery()

    # ship
    sea_logistics = SeaLogistics()
    sea_logistics.plan_delivery()


if __name__ == '__main__':
    main()

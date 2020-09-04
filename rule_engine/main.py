#!/usr/bin/env python3
from validator import Validator
from rules.rule_1 import Rule1 as r1


def main():
    sample = dict(hungry=True, food="steak")
    rules = [
        r1(sample)
    ]
    validator = Validator()
    result = validator.validate(rules)
    print(result)


if __name__ == '__main__':
    main()

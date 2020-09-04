#!/usr/bin/env python3
from rule_interface import RuleInterface


class Rule1(RuleInterface):
    def __init__(self, obj):
        self._hungry = obj['hungry']
        self._food = obj['food']

    def isApplicable(self):
        if self._hungry:
            return True
        else:
            return False

    def executeRule(self):
        if self._food == 'chicken':
            return f"Let's eat {self._food}"
        else:
            return f"I don't like to eat {self._food}"

#!/usr/bin/env python3
from abc import ABC, abstractmethod


class RuleInterface(ABC):
    @abstractmethod
    def isApplicable(self):
        pass

    @abstractmethod
    def executeRule(self):
        pass

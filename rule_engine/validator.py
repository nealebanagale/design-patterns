#!/usr/bin/env python3
class Validator:
    def validate(self, rules):
        result = []
        for rule in rules:
            if (rule.isApplicable()):
                result.append(rule.executeRule())
        return result

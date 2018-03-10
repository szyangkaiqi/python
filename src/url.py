#!/usr/bin/python3

import requests
import json


class Person:
    def add(self,a,b):
        return a+b

print(Person().add(1,2))
print(Person.__doc__)
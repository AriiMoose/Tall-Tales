__author__ = 'Andrew'

#!/usr/bin/env python

from Engine.Entity import Entity
from Engine.Components.TextComponent import TextComponent

class TestEntity(Entity):


    def __init__(self):
        self.testText = TextComponent()
        self.add_components("text", self.testText)
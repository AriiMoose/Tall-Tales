__author__ = 'andrew'

from Engine.Entity import *
from Engine.Components.TextComponent import *
from Engine.Components.KnowledgeComponent import *

class Player(Entity):

    def __init__(self):
        self.textComp = TextComponent()
        self.knowledgeComp = KnowledgeComponent()

        self.add_components("text", [self.textComp])
        self.add_components("knowledge", [self.knowledgeComp])
__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

#!/usr/bin/env python
import abc
import pygame

class Scene:

    # Catches undefined abstract methods during object creation
    __metaclass__ = abc.ABCMeta

    sceneSystems = []
    sceneEntities = []
    gameView = 0

    def __init__(self, game, sceneName):
        """
        """

    def initialise(self, game):
        """ Adds an instance of the game engine to the scene's view

        Args:
            game: Reference to the instance of the game engine (Game.py)
        """

        try:
            self.gameView = game

        except ValueError:
            print "Could not add scene to game view"

    def add_systems(self, systems=[], *args):
        """ Adds systems to the scene

        Args:
            systems: List of systems to add to the scene
        """
        for x in systems:
            try:
                self.sceneSystems.append(systems[x])

            except ValueError:
                print "Could not add system" + x

    def add_entities(self, entities=[], *args):
        """ Adds entities to the scene

        Args:
            entities: List of entities to add to the scene
        """

        for x in entities:
            try:
                self.sceneEntities.append(entities[x])

            except ValueError:
                print "Could not add entity" + x

    @classmethod
    def update(cls):
        """ Propagates the update loop for each of its systems
            Calls checkTransition

        Args:
            None
        """

        for x in cls.sceneSystems:
            cls.sceneSystems.update()

        cls.events = pygame.event.get()

        # Checks for events occurring within the scene and responds to them
        for event in cls.events:
            print "checking events"
            if event.type == pygame.QUIT:
                print "QUIT event received"
                cls.gameView.running = False

        cls.check_transition()

    @classmethod
    def check_transition(cls):
        """ Checks conditions for a scene transition
            Abstract method
            Conditions for transition must be defined by the developer

        Args:
            None
        """

    def draw(self):
        """

        :return:
        """
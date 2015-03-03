__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   This class defines a scene object. Scenes manage their own event loops and
            contain a list of systems and entities which belong to them

    Usage:  Subclass the scene to create a new scene
            In the subclass override the check_transition() method to define the parameters for transitioning between scenes
            Call the add_systems() and add_entities() methods to initialise the relative lists

"""

import abc
import pygame
from Engine.Systems.TextSystem import TextSystem

class Scene:

    # Catches undefined abstract methods during object creation
    __metaclass__ = abc.ABCMeta

    sceneSystems = []
    sceneEntities = []

    def __init__(self):
        """
        """

    def initialise(cls):
        """ Adds an instance of the game engine to the scene's view

        Args:
            game: Reference to the instance of the game engine (Game.py)
        """



    @classmethod
    def add_systems(cls, systems=[], *args):
        """ Adds systems to the scene

        Args:
            systems: List of systems to add to the scene
        """
        try:
            cls.sceneSystems = systems
        except ValueError:
            print "Could not add system"

    @classmethod
    def add_initial_entities(cls, entities=[], *args):
        """ Adds entities to the scene on scene initialisation

        Args:
            entities: List of entities to add to the scene
        """

        try:
            cls.sceneEntities = entities

        except ValueError:
            print "Could not add entity"

    @classmethod
    def add_entities(cls, *args):
        try:
            cls.sceneEntities = cls.sceneEntities.extend(args)

        except ValueError:
            print "Could not add entity"

    @classmethod
    def update(cls):
        """ Propagates the update loop for each of its systems
            Calls checkTransition

        Args:
            None
        """

        for x in cls.sceneSystems:
            x.update()

        cls.events = pygame.event.get()

        # Checks for events occurring within the scene and responds to them
        for event in cls.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
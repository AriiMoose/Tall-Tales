__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

#!/usr/bin/env python
import abc

class Scene:

    # Used to catch unimplemented abstract methods at instantiation
    __metaclass__ = abc.ABCMeta

    def __init__(self, game, sceneName):
        """ When a scene is created a dictionary reference to it is created in the game engine (Game.py)

        Args:
            game: Reference to the instance of the game engine (Game.py)
            sceneName: String to identify the scene
        """

        try:
            game.sceneList[sceneName] = {self}

        except ValueError:
            print "Could not add scene to game view"

    def initialise(self, game, sceneName):
        """

        """

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

    def update(self):
        """ Propagates the update loop for each of its systems
            Calls checkTransition

        Args:
            None
        """

        for x in self.sceneSystems:
            self.sceneSystems.update()

        self.check_transition()

    
    def check_transition(self):
        """ Checks conditions for a scene transition

        Args:
            None
        """

    def draw(self):
        """

        """
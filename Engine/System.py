__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   * Encapsulates game logic and updates its relevant entities
            * Multiple systems can manage different parts of the same entity
            * All systems contain a reference to the scene, and an array of entities with a priority value

    Usage:  * System class is to be subclassed in order to create specific systems
            * Events should be passed from the scene to the system
            * Scene can call check_entity() to distribute entities among systems
"""

class System(object):

    def __init__(self, system_type):
        self.entityList = {}    # Entities stored as dictionary. The key is the entity, the value is the priority
        self.priorityCounter = 0

    def check_entity(self, entity, ent_type):
        """ Used to check if an entity belongs to the system
            Does this by querying the entity for what components it has
            If the entity contains the matching type then it is added with a key that denotes it's priority
            By default, priority is assigned in the order the entities are checked

        Args:
            entity: An instance of the Entity class
        """
        if entity.does_contain(ent_type) is True:
            self.entityList[self.priorityCounter] = entity
            self.priorityCounter = self.priorityCounter + 1

        else:
            print "Check failed"

    def update(self):
        """ Contains all logic for the system
            Should loop through reach entity and update based on priority
        """

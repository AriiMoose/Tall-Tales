__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   * Entities encapsulate objects in the game world
            * They are aggregates of components which contain no logic
            * Their logic is managed by systems

    Usage:  * This class is to be instantiated for each new entity that is to be created
            * Components stored as arrays.
                Allows for multiple components of same type.
                Components indexed by their type
"""
#!/usr/bin/env python

from collections import defaultdict

class Entity:

    componentList = defaultdict(list)


    def __init__(self):
        pass

    def add_components(self, key, components=[]):
        """ Adds a component to the index.
            Creates an array at the components index if it does not already exist
            If the key exists the array is appended to the current array at that index

        Args:
            key: Key to be added
            components: Array of components to be added
        """
        try:
            self.componentList[key].append(components)
        except ValueError:
            print "Could not add components to entity" + self.__name__

    def remove_components(self, key, components):
        """ Removes the specified components at the given index

        Args:
            key: Index of the components
            components: Components to be removed
        """

        if key in self.componentList:
            for components in self.componentList:
                try:
                    del self.componentList[components]
                except ValueError:
                    print "Could not remove component"

        else:
            print "Key does not exist"

    def does_contain(self, key):
        """ Checks if the entity contains a tpye of component
            Component type is indicated by the key

        Args:
            key: Index in the componentList which indicates the type stored
        """
        print "Iterating over components..."
        for key in self.componentList:
            print "Checking keys..."
            if key in self.componentList:
                return True

            else:
                print "No key found"
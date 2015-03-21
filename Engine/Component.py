__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   A component is a list of related properties which contains no logic
            Each component is managed by a System

    Usage:  Subclass the component to create a new component
            This subclass can be further subclassed to provide special-case components

"""

class Component:

    type = ""

    def __init__(self):
       """

       """

    def get_type(self):
        """ Returns the component type. Defaults to class name

        Args:
            None
        """

        if type == "":
            return self.__name__
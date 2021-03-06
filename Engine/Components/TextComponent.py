__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   * Contains the attributes which are required for text processing
            * Managed and updated by the TextSystem

    Usage:  * Attributes within an entity's component should be set when intereacting with the relevant system
"""

from Engine.Component import Component

class TextComponent(Component):

    def __init__(self):
        self.type = "text"
        self.input_string = None
        self.output_string = None
        self.action = None
        self.action_target = None
        self.pos_tags = []
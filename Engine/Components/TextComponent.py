__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   * Contains the attributes which are required for text processing
            * Managed and updated by the TextSystem

    Usage:
"""
#!/usr/bin/env python
from Engine.Component import Component

class TextComponent(Component):

    def __init__(self):
        self.type = "text"
        self.input_string = ""
        self.output_string = ""
        self.pos_tags = []
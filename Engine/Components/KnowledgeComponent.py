__author__ = 'Andrew Tully'

__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   * Contains the attributes which are required for interacting with an expert system
            * Managed and updated by the KnowledgeSystem

    Usage:  * Attributes within an entity's component should be set when intereacting with the relevant system
"""
from Engine.Component import Component
class KnowledgeComponent(Component):

    def __init__(self):
        self.type = "knowledge"
        self.kfb_dict = {}
        self.krb_dict = {}
        self.kb = None
        self.current_rule = None
        self.eval_result = None
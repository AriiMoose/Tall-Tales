__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   * Subclass of System
            * Provides an interface for adding new facts and rules to a knowledge base

    Usage:

"""
from Engine.System import System
from pyke import knowledge_engine

class KnowledgeSystem(System):

    def __init__(self, loc):
        """ Instantiates a new instance of the knowledge engine

        Args:
            loc: The directory which the knowledge bases to be loaded are located
                A package or directory may be passed
        """
        self.engine = knowledge_engine.engine(loc)

    def create_kb(self):
        pass

    def add_kb(self, entity, kb_name, kb):
        """ Adds a knowledge base to an entity by appending it to the Knowledge Component

        Args:
            entity: The entity receiving the knowledge base
            kb_name: The key for the knowledge base being added
            kb: The knowledge base being added
        """
        if self.entityList.__contains__(entity):
            entity.KnowledgeComponent.kb_dict[kb_name] = kb

        else:
            print "Entity does not contain a Knowledge Component"

    def add_fact(self, kb, fact, actor, subject=""):
        """ Add new fact to during runtime

        Args:
            kb: The knowledge base receiving the new fact
            fact: The fact being added
            actor: The entity performing the action
            subject: The target of the action. Defaults to empty
        """

        # If there is no subject, do not add subject
        if subject is "":
            self.engine.assert_(kb, fact, actor)

        else:
            self.engine.assert_(kb, fact, (actor, subject))

    def add_rule(self):
        pass

    def update(self):

        # Update each entity based on it's priority
        for key in sorted(self.entityList):
            if(key.current_rule is not None):
                key.eval_result = self.evaluate(key.kb, key.current_rule)

    def evaluate(self, kb, rule, subject):
        """ Evaluates a rule or fact in the knowledge base

        Args:
            kb: Knowledge base to be checked
            rule: Rule/Fact to be checked
            actor: Entity performing the action. Defaults to the player
            subject: The target of the action
        """

        # Construct argument string for testing the rule
        self.arg_string = kb + "." + rule
        print(self.arg_string)
        print(subject)
        print(self.engine.prove_1_goal(self.arg_string + "(" + subject + ")"))

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
from pyke import knowledge_engine, krb_traceback

class KnowledgeSystem(System):

    def __init__(self, loc):
        """ Instantiates a new instance of the knowledge engine

        Args:
            loc: The directory which the knowledge bases to be loaded are located
                A package or directory may be passed
        """
        self.engine = knowledge_engine.engine(loc)
        self.currentKB = None

        self.type = "knowledge"
        super(KnowledgeSystem, self).__init__(type)

    def access_components(self):
        # Access the knowledge component of an entity

        for ents in self.entityList:
            if "knowledge" in self.entityList.get(ents).componentList:
                for comps in self.entityList.get(ents).componentList:
                    for rules in self.entityList.get(ents).componentList:
                        if rules.kb is not None and comps.current_rule is not None:
                            print("Evaluating...")
                            comps.eval_result = self.evaluate(comps.kb, comps.current_rule, comps.param)

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

    def evaluate(self, kb, rule, subject):
        """ Evaluates a rule or fact in the knowledge base

        Args:
            kb: Knowledge base to be checked
            rule: Rule/Fact to be checked
            actor: Entity performing the action. Defaults to the player
            subject: The target of the action
        """

        # To expand the subject arg, refer to:
        # http://stackoverflow.com/questions/6913084/how-to-split-list-and-pass-them-as-separate-parameter
        # Useful with FrameNet API

        # Construct argument string for testing the rule

        self.engine.reset()
        if kb is not None:
            self.arg_string = kb + "." + rule

            print("KB: " + kb)
            print("arg_string: " + self.arg_string)
            print("Subject: " + subject)
            print("Current KB: " + str(self.currentKB))
            print("New KB: " + (kb))


            try:
                self.engine.activate(kb)
                if self.engine.prove_1_goal(self.arg_string + "("")"):
                    return True

            except StandardError:
                krb_traceback.print_exc()
                return False
__author__ = 'andrew'

from Engine.Systems.KnowledgeSystem import KnowledgeSystem
from Engine.Scene import *
import Engine.InputBox


from DemoEntities.Chest import Chest
from DemoEntities.Door import Door
from DemoEntities.Key import Key
from DemoEntities.Player import Player


class IntroScene(Scene):

    @classmethod
    def initialise(cls):
        # Initialise scene systems
        cls.intro_textSystem = TextSystem()
        cls.intro_knowledgeSystem = KnowledgeSystem("./KBs/")

        # Initialise entities
        cls.player = Player()
        cls.intro_exit = Door()
        cls.intro_key = Key()
        cls.intro_chest = Chest()

        # Add systems to the scene
        cls.add_systems([cls.intro_knowledgeSystem, cls.intro_textSystem])

        # Add initial entities to the scene
        cls.add_initial_entities([cls.intro_exit, cls.intro_chest])

        # Scene-specific attributes
        cls.hasKey = False
        cls.user_reply = None

    def check_transition(cls):
        pass

    @classmethod
    def update(cls):
        Scene.update()
        for event in cls.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Take user input
                cls.player.textComp.input_string = Engine.InputBox.ask(cls.gameView.screen, "Input: ")

                # POS tag input
                cls.player.textComp.pos_tags = cls.intro_textSystem.get_pos(cls.player.textComp.input_string)

                # Interperate sentence
                cls.input_eval = cls.intro_textSystem.interperate(cls.player.textComp.pos_tags)
                cls.player.textComp.action = cls.input_eval[0]
                cls.player.textComp.action_target = cls.input_eval[1]

                cls.player.knowledgeComp.current_rule = cls.player.textComp.action
                cls.player.knowledgeComp.param = cls.player.knowledgeComp.action_target
                print(cls.player.knowledgeComp.eval_result)


    @classmethod
    def draw(self):
        pass
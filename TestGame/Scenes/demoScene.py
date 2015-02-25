from Engine.Scene import *
from Engine.Systems import TextSystem
from Engine.Systems import KnowledgeSystem
import Engine.InputBox

from TestGame.Entities.Chest import Chest
from TestGame.Entities.Door import Door
from TestGame.Entities.Key import Key
from TestGame.Entities.Player import Player

class DemoScene(Scene):

    @classmethod
    def initialise(cls):
        # Initialise Systems
        cls.demoScene_textSystem = TextSystem.TextSystem()
        cls.demoScene_knowledgeSystem = KnowledgeSystem.KnowledgeSystem('./TestGame/KB')

        # Initialise entities
        cls.demo_chest = Chest()
        cls.demo_door = Door()
        cls.demo_key = Key()
        cls.demo_player = Player()

        # Add systems to the scene
        cls.add_systems([cls.demoScene_knowledgeSystem, cls.demoScene_textSystem])

        # Add entities to the scene
        cls.add_initial_entities([cls.demo_chest, cls.demo_door, cls.demo_key, cls.demo_player])

    @classmethod
    def update(cls):
        Scene.update()

        for event in cls.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Take user input
                cls.demo_player.textComp.input_string = Engine.InputBox.ask(cls.gameView.screen, "Input: ")

                # POS tag input
                cls.demo_player.textComp.pos_tags = cls.demoScene_textSystem.get_pos(cls.demo_player.textComp.input_string)

                # Interperate sentence

                """
                - The player's Text Component stores the input string
                - This is passed to the scene's Text System to pos tag and evaluate
                - The player's Text Component stores the result, including the rule to be sent to the knowledge system
                    and the parameters for the rule
                - The Knowledge System then evaluates these values
                """

                cls.input_eval = cls.demoScene_textSystem.interperate(cls.demo_player.textComp.pos_tags)
                cls.demo_player.textComp.action = cls.input_eval[0]
                cls.demo_player.textComp.action_target = cls.input_eval[1]

                cls.demo_player.knowledgeComp.current_rule = cls.demo_player.textComp.action
                cls.demo_player.knowledgeComp.param = cls.demo_player.knowledgeComp.action_target
                print(cls.demo_player.knowledgeComp.eval_result)

    @classmethod
    def draw(self):
        pass
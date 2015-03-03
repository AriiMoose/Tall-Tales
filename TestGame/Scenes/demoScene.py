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

        print(cls.sceneEntities)

        # Check which entities belong to what systems
        for ents in DemoScene.sceneEntities:
            print(cls.demoScene_textSystem.priorityCounter)
            cls.demoScene_textSystem.check_entity(ents, "text")

        for ents in DemoScene.sceneEntities:
            print(ents)
            cls.demoScene_knowledgeSystem.check_entity(ents, "knowledge")

        print(cls.demoScene_textSystem.entityList)
        print(cls.demoScene_knowledgeSystem.entityList)

        # Scene-specific attributes
        cls.chest_open = False
        cls.has_key = False
        cls.door_open = False

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
                cls.demo_player.knowledgeComp.param = cls.demo_player.textComp.action_target
                cls.demo_player.knowledgeComp.eval_result = cls.demoScene_knowledgeSystem.evaluate(cls.demo_player.knowledgeComp.param,
                                                       cls.demo_player.knowledgeComp.current_rule,
                                                       cls.demo_player.knowledgeComp.param)

                print("Eval Results: " + str(cls.demo_player.knowledgeComp.eval_result))

                if cls.demo_player.knowledgeComp.eval_result:
                    cls.gameView.text = cls.gameView.font.render("You successfully " + cls.demo_player.textComp.input_string,
                                                            1,
                                                            (0, 0, 0))
                else:
                    cls.gameView.text = cls.gameView.font.render("You unsuccessfully " + cls.demo_player.textComp.input_string,
                                                                 1,
                                                                (0,0,0))
                cls.gameView.background.fill((250, 250, 250))
                cls.gameView.background.blit(cls.gameView.text, (50,100))
                cls.gameView.screen.blit(cls.gameView.background, (0, 0))
                pygame.display.flip()

        #print(cls.chest_open)

    @classmethod
    def draw(self):
        pass

    @classmethod
    def checkInput(cls):
        """ - Recursive function
            - Checks user input, if  that fails, check synonyms
            - If there is still no match, return false
        """
from Engine.Scene import *
from Engine.Systems import TextSystem
from Engine.Systems import KnowledgeSystem
from nltk.corpus import wordnet as wn
import Engine.InputBox
import re

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
        # Attribute flags
        cls.chest_open = False
        cls.has_key = False
        cls.key_present = False
        cls.key_eaten = False
        cls.door_open = False

        cls.intro_string = "You find yourself in a room with a door and a chest. Press Enter to input an action"
        cls.gameView.text = cls.gameView.font.render(cls.intro_string,
                                                            1,
                                                            (0, 0, 0))

    @classmethod
    def update(cls):
        Scene.update()

        for event in cls.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print(cls.chest_open)

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

                cls.input_eval = cls.demoScene_textSystem.interpret(cls.demo_player.textComp.pos_tags)

                print("Input eval: " + str(cls.input_eval))

                cls.demo_player.textComp.action = cls.input_eval[0]
                print("Player Action: " + str(cls.demo_player.textComp.action))

                cls.demo_player.textComp.action_target = cls.input_eval[1]

                cls.demo_player.knowledgeComp.current_rule = cls.demo_player.textComp.action
                cls.demo_player.knowledgeComp.param = cls.demo_player.textComp.action_target
                cls.demo_player.knowledgeComp.eval_result = cls.demoScene_knowledgeSystem.evaluate(cls.demo_player.knowledgeComp.param,
                                                       cls.demo_player.knowledgeComp.current_rule,
                                                       cls.demo_player.knowledgeComp.param)

                print("Eval Results: " + str(cls.demo_player.knowledgeComp.eval_result))

                # If the evaluation fails, print a default error message
                if not cls.demo_player.knowledgeComp.eval_result:
                    synsets = cls.demoScene_textSystem.checkInput(cls.demo_player.textComp.action)

                    for syn in synsets:
                        cls.demo_player.knowledgeComp.eval_result = cls.demoScene_knowledgeSystem.evaluate(cls.demo_player.knowledgeComp.param,
                                                                                                           syn,
                                                                                                           cls.demo_player.knowledgeComp.param)

                    if cls.demo_player.knowledgeComp.eval_result is False and cls.demo_player.textComp.action_target is not "":
                        cls.demo_player.textComp.output_string = ("You attempt to " +
                                                                    cls.demo_player.textComp.action + " the " +
                                                                    cls.demo_player.textComp.action_target +
                                                                    ". Nothing happens")

                    elif cls.demo_player.knowledgeComp.eval_result is False and cls.demo_player.textComp.action_target is "":
                        cls.demo_player.textComp.output_string = ("What do you want to " +
                                                                    cls.demo_player.textComp.action + "?")

                cls.gameView.text = cls.gameView.font.render(cls.demo_player.textComp.output_string,
                                                            1,
                                                            (0, 0, 0))


                """
                TODO:   - Basic animation
                """
                if cls.door_open is True:
                    # Draw open door
                    pass

                if cls.chest_open is True:
                    # Draw open chest
                    pass

                cls.gameView.background.blit(cls.background, (0,0))

                cls.gameView.background.blit(cls.gameView.text, (50,100))
                cls.gameView.screen.blit(cls.gameView.background, (0, 0))
                pygame.display.flip()

                print(cls.chest_open)

    @classmethod
    def draw(cls):
        cls.background = pygame.image.load('./TestGame/Backgrounds/scene.png')
        cls.gameView.background.blit(cls.background, (0, 0))
        cls.gameView.background.blit(cls.gameView.text, (50,100))
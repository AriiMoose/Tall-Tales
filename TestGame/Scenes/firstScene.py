__author__ = 'Andrew'

from Engine.Scene import *
import TestGame.Scenes.secondScene
from Engine.Systems.TextSystem import TextSystem
from Engine.Systems.KnowledgeSystem import KnowledgeSystem
from Engine.Components.TextComponent import TextComponent
from TestGame.Entities.TestEntity import TestEntity
import Engine.eztext
import Engine.InputBox

class SceneOne(Scene):

    @classmethod
    def initialise(cls):
        cls.testSystem = TextSystem()
        cls.knowledgeSys = KnowledgeSystem('./TestGame/KB/')
        cls.testEnt1 = TestEntity()
        cls.testEnt2 = TestEntity()

        cls.add_systems([cls.testSystem])
        print "Text System added"

        cls.add_initial_entities([cls.testEnt1])
        print "Sample Entity added"
        print "" + cls.testEnt1.componentList.__str__()

        for ents in cls.sceneEntities:
            cls.testSystem.check_entity(ents, cls.testSystem.type)

        print "System entity list " + cls.testSystem.entityList.__str__()

    @classmethod
    def check_transition(cls):

        for event in cls.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                print "KEYDOWN_LEFT event received"
                cls.gameView.set_active_scene(TestGame.Scenes.secondScene.SceneTwo)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                print "" + cls.sceneSystems.__str__()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                print "" + cls.sceneEntities.__str__()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                cls.add_entities(cls.testEnt2)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                cls.answer = Engine.InputBox.ask(cls.gameView.screen, "Input")
                print "Answer: " + cls.answer
                cls.test_pos = cls.testSystem.get_pos(cls.answer)
                cls.test_eval = cls.testSystem.interperate(cls.test_pos)
                print(cls.test_eval)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                cls.knowledgeSys.evaluate('test', cls.test_eval[0], cls.test_eval[1] )
        pygame.display.flip()

    @classmethod
    def draw(cls):
        # Fill Background
        cls.gameView.background = pygame.Surface(cls.gameView.screen.get_size())
        cls.gameView.background = cls.gameView.background.convert()
        cls.gameView.background.fill((250, 250, 250))

        # Display text
        cls.gameView.font = pygame.font.Font(None, 36)
        cls.gameView.text = cls.gameView.font.render("Scene One", 1, (10, 10, 10))
        cls.gameView.textpos = cls.gameView.text.get_rect()
        cls.gameView.textpos.centerx = cls.gameView.background.get_rect().centerx
        cls.gameView.background.blit(cls.gameView.text, cls.gameView.textpos)

        # Render (blit) everything to the screen
        cls.gameView.screen.blit(cls.gameView.background, (0, 0))
        pygame.display.flip()
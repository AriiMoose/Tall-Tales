__author__ = 'Andrew'

#!/usr/bin/env Python

from Engine.Scene import *
import TestGame.Scenes.secondScene

class SceneOne(Scene):

    @classmethod
    def check_transition(cls):

        for event in cls.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                print "KEYDOWN_LEFT event received"
                cls.gameView.set_active_scene(TestGame.Scenes.secondScene.SceneTwo)

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
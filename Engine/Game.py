__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

""" Desc:   This class defines a Game object which represents the game engine.
            The game engine handles the initialisation and updating on the game.

    Usage:  Create a new Game object, providing a name and screen dimensions.
            This creates a new instance of the game engine for running a game.
            Call the run function
            This loads a default canvas and begins running the main game loop until the game is closed.
"""

#!/usr/bin/env python
import pygame
import Scene
import sys
from TestGame.Scenes import firstScene

class Game:

    def __init__(self, game_name, screen_width, screen_height):

        """Initialises a default canvas and sets the game to be ready to run

        Args:
            game_name: Name of the game being created
            screen_width: Width of the game screen
            screen_height: Height of the game screen
            initialScene: The first scene to be activated in the game
        """

        pygame.init()
        self.sceneList = {}
        self.gameName = game_name
        self.initialised = True
        self.running = True
        self.isActive = False

        # Initialise Screen
        print "Initialising game screen..."
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(game_name)

        # Draw default background
        print "Drawing default canvas..."

         # Fill Background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        # Display text
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Hello world", 1, (10, 10, 10))
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.background.get_rect().centerx
        self.background.blit(self.text, self.textpos)

        # Render (blit) everything to the screen
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        # Set the base scene's game view to this instance of the game engine
        Scene.Scene.gameView = self

    def run(self):

        """ Runs the game. Calls update and draw methods

        Args:
            None
        """
        while self.running:
            self.update()

        if self.running == False:
            pygame.quit()
            sys.exit()

    def set_active_scene(self, scene):
        """ Set the active scene and notify the game that an active scene has been set

        Args:
            scene: The scene which is to be made active"""
        print "Setting active scene..."
        self.activeScene = scene
        self.isActive = True
        self.activeScene.draw()
        print "Scene changed"

    def update(self):
        """ Update the game each frame while the game is running
            Check the event queue
            If the game stops running unload the pygame modules & quit
            If an active scene has been set, update the active scene

        Args:
            None

        """

        if self.isActive:
            self.activeScene.update()

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
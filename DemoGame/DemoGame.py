__author__ = 'andrew'

from Engine.Game import Game
from DemoScenes import IntroScene

class DemoGame:

    game = Game("Demo Game", 500, 500)

    game.set_active_scene(IntroScene.IntroScene)
    game.run()
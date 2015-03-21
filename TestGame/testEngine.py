__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

from Engine.Game import Game
from Scenes import demoScene

class Test:
        game = Game('Test Game', 800, 600)

        game.set_active_scene(demoScene.DemoScene)
        print "Running game"
        game.run()

__author__ = 'Andrew Tully'
__copyright__ = 'Copyright 2015, Andrew Tully'
__credits__ = 'Andrew Tully'
__license__ = 'MIT'
__maintainer__ = 'Andrew Tully'
__email__ = 'ariimoose@gmail.com'
__status__ = 'Development'

#!/usr/bin/env python
from Engine.Game import Game
from Scenes import firstScene

class Test:
        game = Game('Test Game', 150, 50)

        game.set_active_scene(firstScene.SceneOne)
        print "Running game"
        game.run()

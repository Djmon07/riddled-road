import engine
import map

the_map = map.Map('startscene')
the_game = engine.Engine(the_map)
the_game.run()

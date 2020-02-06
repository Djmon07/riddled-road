import scene

class Engine(object):

    def __init__(self, scene):
        #class in map class
        self.scene = scene

    def run(self):
        #gets class from map
        current_scene = self.scene.opening_scene()
        final = self.scene.next_scene('finished')

        while current_scene != final:
            #checks for win/ loss condition
            next_scene_name = current_scene.enter()
            current_scene = self.scene.next_scene(next_scene_name)

        current_scene.enter()

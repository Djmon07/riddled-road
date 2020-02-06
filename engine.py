import scene

class Engine(object):

    def __init__(self, scene):
        self.scene = scene

    def run(self):
        current_scene = self.scene.opening_scene()
        final = self.scene.next_scene('finished')

        while current_scene != final:
            next_scene_name = current_scene.enter()
            current_scene = self.scene.next_scene(next_scene_name)

        current_scene.enter()

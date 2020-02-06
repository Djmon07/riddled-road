import scene

class Map(object):

    scene = {
        'startscene': scene.StartScene(),
        'road': scene.Road(),
        'barn': scene.Barn(),
        'path': scene.Path(),
        'bridge': scene.Bridge(),
        'death': scene.Death(),
        'finished': scene.Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        new_scene = Map.scene.get(scene_name)
        return new_scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

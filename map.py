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
    #scenes used in game

    def __init__(self, start_scene):
        #used to hold the scene
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        #used to hold the upcoming scene
        new_scene = Map.scene.get(scene_name)
        return new_scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

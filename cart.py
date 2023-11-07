from location import Location
from status import Status

# from ursina.prefabs.platformer_controller_2d import PlatformerController2d

from ursina import Entity, time, boxcast, raycast, Vec3, color, held_keys


class Cart(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        # start_location = Location
        # goal_location = Location
        # status = Status
        self.collider = "box"
        self.x = -4
        self.y = 0

    # self.path_plan = Path # This is where the path planning algorithm results should go

    # @wrapper

    def update(self):

        self.direction = Vec3(
            self.up * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
        ).normalized()
        # print(self.direction)

        hit_info = raycast(self.world_position, self.direction,
                           ignore=(self,), distance=1, debug=True)

        if not hit_info.hit:
            self.position += self.direction * 5 * time.dt

    def dropoff(self):
        pass

    def pickup(self):
        pass

    def drive(self):
        pass

    def calculate_path(self):
        pass

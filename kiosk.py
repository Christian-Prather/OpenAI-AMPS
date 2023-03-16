from location import Location
import random
from ursina import Entity, time, boxcast, raycast, Vec3, color


class Kiosk(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        self.location = Location(self.x, self.y)
        self.users_used = 0
        self.waiting_on_ride = False

        self.sim_ride_time = random.randint(10, 30)
        self.counter = 0
        self.collider = "box"

    def call_ride(self):
        if not self.waiting_on_ride:
            self.color = color.yellow

    def cancle_ride(self):
        pass

    def update(self):
        self.counter += 1 * time.dt
        if self.counter >= self.sim_ride_time:
            self.call_ride()
            self.counter = 0

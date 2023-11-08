from location import Location
import random
from ursina import Entity, time, boxcast, raycast, Vec3, color


def pick_random_walk():
    return random.randint(-1, 1)


class Person(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        print("Generating Person")
        self.collider = 'box'
        self.start_location = Location(
            random.randint(-4, 4), random.randint(-8, -2))
        self.current_location = self.start_location

        self.lifetime = random.randint(100, 1000)
        self.walk_time = 0
        self.walk_direction = pick_random_walk()
        self.horizontal = True
        self.walk_length = random.randint(50, 55)
        self.x = self.start_location.x
        self.y = self.start_location.y
        # self.origin = (-.5, .5)
        self.collider = "box"
        self.hit_something = False
        self.direction = Vec3(self.walk_direction, 0, 0).normalized()

    def update(self):
        '''
            The loop thread logic that will update position and decide if this object should be killed or moved
        '''
        hit_info = raycast(origin=self.world_position, direction=self.direction,
                           distance=0.25, ignore=(self,), debug=True)
        if hit_info.hit:
            self.color = color.red
            # print("Hit")
            self.walk_direction = -self.walk_direction
            if self.horizontal:
                self.x += self.walk_direction * time.dt
            else:
                self.y += self.walk_direction * time.dt
        else:
            self.color = color.pink
            if self.horizontal:
                self.direction = Vec3(self.walk_direction, 0, 0).normalized()
                if self.walk_time < self.walk_length:
                    self.x += self.walk_direction * time.dt

                    self.walk_time += 1
                else:
                    self.walk_direction = pick_random_walk()
                    self.walk_time = 0
                    self.horizontal = False
            else:
                self.direction = Vec3(0, self.walk_direction, 0).normalized()

                if self.walk_time < self.walk_length:
                    self.y += self.walk_direction * time.dt
                    self.walk_time += 1
                else:
                    self.walk_direction = pick_random_walk()
                    self.walk_time = 0
                    self.horizontal = True

    def update_position(self):
        '''
            Randomly generate a move to make and update position
        '''
        pass

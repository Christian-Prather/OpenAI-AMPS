from location import Location
import random
from ursina import Entity, time


def pick_random_walk():
    return random.randint(-1, 1)


class Person(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        print("Generating Person")
        self.start_location = Location(
            random.randint(0, 1), random.randint(0, 1))
        self.current_location = self.start_location

        self.lifetime = random.randint(0, 2000)
        self.walk_time = 0
        self.walk_direction = pick_random_walk()
        self.horizontal = True
        self.walk_length = random.randint(30, 55)
        self.x = self.start_location.x
        self.y = self.start_location.y

    def update(self):
        '''
            The loop thread logic that will update position and decide if this object should be killed or moved
        '''
        if self.horizontal:
            if self.walk_time < self.walk_length:
                self.x += self.walk_direction * time.dt
                self.walk_time += 1
            else:
                self.walk_direction = pick_random_walk()
                self.walk_time = 0
                self.horizontal = False
        else:
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

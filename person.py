from location import Location
import random
from ursina import Entity, time

def pick_random_walk():
    return random.randint(-1, 1)


class Person(Entity):
    print("Generating Person")
    start_location = Location(
        random.randint(0, 100), random.randint(0, 100))
    current_location = start_location
    lifetime = random.randint(0, 2000)
    walk_time = 0
    walk_direction = pick_random_walk()
    horizontal = True
    walk_length = random.randint(30, 55)

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

from location import Location
import random


class Person():
    def __init__(self):
        print("Generating Person")
        self.start_location = Location(
            random.randint(0, 100), random.randint(0, 100))
        self.current_location = self.start_location
        self.lifetime = random.randint(0, 2000)

    def update(self):
        '''
            The loop thread logic that will update position and decide if this object should be killed or moved
        '''
        pass

    def update_position(self):
        '''
            Randomly generate a move to make and update position
        '''
        pass

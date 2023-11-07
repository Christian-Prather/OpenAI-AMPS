from location import Location
from kiosk import Kiosk

class User:
    def __init__(self):
        print("Generating a user")
        self.waiting_time = 0
        self.destination = Location
        self.start_location = Location
        self.frustration = 0
        self.nearest_kiosk = Kiosk

    def update_personal_status(self):
        '''
            Update my frustration as Im waiting and see if I should cancel
        '''
        pass

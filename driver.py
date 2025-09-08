from constants import RATING

class Driver:
    def __init__(self, name, rating : RATING):
        self.name = name
        self.rating = rating
        self.avail = False
    
    def update_avail(self, avail):
        self.avail = avail
    
    def get_driver_name(self):
        return self.name
    
    def get_rating(self):
        return self.rating
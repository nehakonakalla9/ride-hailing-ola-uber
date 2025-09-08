from constants import RATING
class Rider:
    def __init__(self, name, rating : RATING):
        self.name = name
        self.rating = rating
    def get_rider_name(self):
        return self.name
    def get_rider_rating(self):
        return self.rating
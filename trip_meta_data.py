from constants import RATING
class TripMetaData:
    def __init__(self, src_loc, dst_loc, rider_rating : RATING):
        self.src_loc = src_loc
        self.dst_loc = dst_loc
        self.rider_rating = rider_rating
        self.driver_rating = RATING.UNASSIGNED
    
    def set_driver_rating(self, rating : RATING):
        self.driver_rating =  rating
    
    def get_driver_rating(self):
        return self.driver_rating

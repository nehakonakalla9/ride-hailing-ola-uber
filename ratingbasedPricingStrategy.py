from pricing_strategy import PricingStrategy
from trip_meta_data import TripMetaData
from constants import Util

class RatingBasedPricingStrategy(PricingStrategy):
    def calculate_price(self, trip_meta_data : TripMetaData):
        if Util.is_high_rating(trip_meta_data.rider_rating):
            price = 55.0
        else:
            price = 65.0
        print(f"Based on {Util.rating_to_string(trip_meta_data.rider_rating)} "
              f"rider rating, price of the trip is {price}")
        return price


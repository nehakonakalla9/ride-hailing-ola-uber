from pricing_strategy import PricingStrategy
from trip_meta_data import TripMetaData

class DefaultPricingStrategy(PricingStrategy):
    def calculate_price(self, trip_meta_data : TripMetaData):
        print ("Based on default strategy, price is 100")
        return 100.0